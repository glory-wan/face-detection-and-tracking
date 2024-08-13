import cv2
import dlib
import time


def main():
    capture = cv2.VideoCapture(0)
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("../models/shape_predictor_68_face_landmarks.dat")

    cv2.namedWindow("face detection", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("face detection", 2 * 640, 2 * 480)  # 放大窗口尺寸

    frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
    frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
    frame_fps = capture.get(cv2.CAP_PROP_FPS)
    videoFormat = cv2.VideoWriter_fourcc(*"XVID")
    output = cv2.VideoWriter("../result/landmarks.avi", videoFormat, int(frame_fps), (int(frame_width), int(frame_height)), True)

    while capture.isOpened():
        ret, frame = capture.read()  # 第一个是布尔值ret，表示是否成功读取了帧，第二个是实际的帧数据frame
        start_time = time.time()  # 记录起始时间

        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = detector(gray, 1)

            for face in faces:  # (x, y, w, h)
                cv2.rectangle(frame, (face.left(), face.top()), (face.right(), face.bottom()), (255, 192, 203), 4)  # 4代表矩形框的粗细

                shape = predictor(gray, face)
                for pt in shape.parts():
                    pt_position = (pt.x, pt.y)
                    cv2.circle(frame, pt_position, 2, (0, 255, 0), -1)  # 5代表关键点的大小   -1 代表关键点是实心的

            current_time = time.time()  # 更新当前帧的时间
            fps = 1 / (current_time - start_time)  # 计算帧率
            cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow("face detection", frame)

        output.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('\x1b'):
            break

    capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
