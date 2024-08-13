import cv2
import dlib


def show_image(image, title):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def plot_rectangle(image, faces):
    for face in faces:
        cv2.rectangle(image, (face.left(), face.top()), (face.right(), face.bottom()), (255, 0, 0), 4)
    return image


def main():
    img = cv2.imread("data01.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    detector = dlib.get_frontal_face_detector()
    detection_result = detector(gray)  # (gray, 1) 中 1 的作用是把图片放大一倍，可以提高识别精度

    img_result = plot_rectangle(img.copy(), detection_result)
    show_image(img_result, "face detection")
    cv2.imwrite('../result/frontal_face_detector.jpg', img_result)


if __name__ == '__main__':
    main()
