import cv2
import dlib
import numpy as np
import matplotlib.pyplot as plt


def main():
    image = cv2.imread("data01.jpg")
    detector = dlib.get_frontal_face_detector()

    # http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
    # http://dlib.net/files/shape_predictor_5_face_landmarks.dat.bz2
    predictor = dlib.shape_predictor("../models/shape_predictor_68_face_landmarks.dat")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = detector(gray, 1)

    for face in faces:  # (x, y, w, h)
        cv2.rectangle(image, (face.left(), face.top()), (face.right(), face.bottom()), (255, 255, 255), 3)  # 4代表矩形框的粗细
        shape = predictor(image, face)
        for pt in shape.parts():
            pt_position = (pt.x, pt.y)
            cv2.circle(image, pt_position, 3, (0, 255, 0), -1)  # 5代表关键点的大小   -1 代表关键点是实心的

    cv2.namedWindow("face detection", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("face detection", 1280, 960)  # 调整窗口尺寸
    cv2.imshow("face detection ", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('../result/landmarks_68.jpg', image)


if __name__ == '__main__':
    main()
