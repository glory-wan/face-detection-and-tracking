import matplotlib.pyplot as plt
import cv2


def show_img(image1, image2, image3, num):
    image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
    image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
    image3 = cv2.cvtColor(image3, cv2.COLOR_BGR2RGB)

    fig, ax = plt.subplots(1, num, figsize=(5 * num, 5))

    ax[0].imshow(image1)
    ax[0].set_title('input')
    ax[0].axis('off')

    ax[1].imshow(image2)
    ax[1].set_title('landmarks_5')
    ax[1].axis('off')

    ax[2].imshow(image3)
    ax[2].set_title('landmarks_68')
    ax[2].axis('off')

    plt.show()


if __name__ == '__main__':
    img1 = cv2.imread('face_landmarks_dlib/data01.jpg')
    img2 = cv2.imread('face_landmarks_dlib/result_5.jpg')
    img3 = cv2.imread('face_landmarks_dlib/result_68.jpg')

    show_img(img1, img2, img3, num=3)
