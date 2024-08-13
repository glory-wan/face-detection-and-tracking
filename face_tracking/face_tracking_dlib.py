import cv2
import dlib
import time


def main():
    capture = cv2.VideoCapture(0)
    detector = dlib.get_frontal_face_detector()
    tracker = dlib.correlation_tracker()

    tracking_state = False

    frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
    frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
    frame_fps = capture.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    output = cv2.VideoWriter("record.avi", fourcc, int(frame_fps), (int(frame_width), int(frame_height)), True)

    while True:
        ret, frame = capture.read()
        cv2.namedWindow("face tracking", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("face tracking", 2 * 640, 2 * 480)  # 调整窗口尺寸
        start_time = time.time()  # 记录起始时间
        if tracking_state is False:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            detect_result = detector(gray, 1)  # 返回检测到的人脸
            if len(detect_result) > 0:
                tracker.start_track(frame, detect_result[0])
                tracking_state = True

        if tracking_state is True:
            tracker.update(frame)  # 更新画面
            position = tracker.get_position()  # 获取人脸的坐标
            cv2.rectangle(frame, (int(position.left()), int(position.top())),
                          (int(position.right()), int(position.bottom())), (0, 255, 0), 3)

        current_time = time.time()  # 更新当前帧的时间
        fps = 1 / (current_time - start_time)  # 计算帧率
        cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("face tracking", frame)
        output.write(frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("\x1b"):
            break

    capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
