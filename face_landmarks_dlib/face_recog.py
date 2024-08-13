import cv2
import face_recognition


def show_image(image, title):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def show_landmarks(image, landmarks):
    for landmarks_dict in landmarks:
        for landmarks_key in landmarks_dict.keys():
            for point in landmarks_dict[landmarks_key]:
                cv2.circle(image, point, 5, (0, 255, 0), -1)
    return image


def main():
    img = cv2.imread("../face_landmarks_recognition/data01.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 'large' is for landmark_68, small is for landmark_5
    face_marks = face_recognition.face_landmarks(gray, None, "large")
    img_result = show_landmarks(img.copy(), face_marks)
    show_image(img_result, "face recognition")
    cv2.imwrite('../result/landmarks_68.jpg', img_result)


if __name__ == '__main__':
    main()
