import cv2
import pylab
import matplotlib.pyplot as plt


def show_image(image, title, pos):
    cv2.namedWindow(title, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(title, 1600, 900)
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def plot_rectangle(image, faces):
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 3)
    return image


def main():
    img = cv2.imread("data03.png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_alt2 = cv2.CascadeClassifier("../models/haarcascade_frontalface_default.xml")
    face_alt2_detection = face_alt2.detectMultiScale(gray)
    face_alt2_result = plot_rectangle(img.copy(), face_alt2_detection)

    show_image(face_alt2_result, "face detection", 1)
    cv2.imwrite('../result/CascadeClassifier.jpg', face_alt2_result)


if __name__ == '__main__':
    main()
