
#   This example program shows how to use dlib's implementation of the paper:
#   One Millisecond Face Alignment with an Ensemble of Regression Trees by
#   Vahid Kazemi and Josephine Sullivan, CVPR 2014

import os
import cv2
import dlib
import glob


predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

train_path = "path\to\trainSet"

detector = dlib.get_frontal_face_detector()
print("Showing detections and predictions on the images in the faces folder...")

for f in glob.glob(os.path.join(train_path, "*.jpg")):
    print("Processing file: {}".format(f))
    img = cv2.imread(f)
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dets = detector(img2, 1)
    print("Number of faces detected: {}".format(len(dets)))
    for index01, face in enumerate(dets):
        print('face {}; left {}; top {}; right {}; bottom {}'.format(index01, face.left(), face.top(), face.right(),
                                                                     face.bottom()))

        # left = face.left()
        # top = face.top()
        # right = face.right()
        # bottom = face.bottom()
        # cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 3)
        # cv2.namedWindow(f, cv2.WINDOW_AUTOSIZE)
        # cv2.imshow(f, img)

        shape = predictor(img, face)
        # print(shape)
        # print(shape.num_parts)
        for index02, pt in enumerate(shape.parts()):
            print('Part {}: {}'.format(index02, pt))
            pt_pos = (pt.x, pt.y)
            cv2.circle(img, pt_pos, 2, (255, 0, 0), 1)
            # print(type(pt))
        # print("Part 0: {}, Part 1: {} ...".format(shape.part(0), shape.part(1)))
        cv2.namedWindow(f, cv2.WINDOW_AUTOSIZE)
        cv2.imshow(f, img)

cv2.waitKey(0)
cv2.destroyAllWindows()
