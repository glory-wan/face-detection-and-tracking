import dlib
import cv2
import time


def plot_rectangle(image, faces):
    for face in faces:
        cv2.rectangle(image, (face.left(), face.top()), (face.right(), face.bottom()), (255, 0, 0), 4)
    return image


def main():
    capture = cv2.VideoCapture(0)

    if capture.isOpened() is False:
        print("!!!")

    while True:
        ret, frame = capture.read()
        start_time = time.time()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            detector = dlib.get_frontal_face_detector()  # 人脸检测器
            detection_result = detector(gray, 1)  # (gray, 1) 中 1 的作用是把图片放大一倍

            img_result = plot_rectangle(frame.copy(), detection_result)

            current_time = time.time()  # 更新当前帧的时间
            fps = 1 / (current_time - start_time)  # 计算帧率

            cv2.putText(img_result, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow("face detection ", img_result)

            if cv2.waitKey(1) == 27:  # 按“ESC”退出
                break

    capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
