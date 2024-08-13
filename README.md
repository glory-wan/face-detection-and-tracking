# Face Detection and Tracking Project Based on Dlib
 A repository for showing simple examples of face recognition based on the Dlib library

------

​	This project contains several Python scripts focused on face detection, landmark detection, face recognition, and tracking using the `dlib` and `cv2` libraries. Below is an overview of each script and its primary functionality.

## Scripts Overview

### 1. Face Detection

- **`face_detection/dlib_frontal_face_detector_img.py`**:
  - Detects faces in a single image using dlib's frontal face detector.
  - Displays and saves the result with detected faces outlined with rectangles.
- **`face_detection/dlib_frontal_face_detector_video.py`**:
  - Detects faces in a real-time video stream from a webcam using dlib's frontal face detector.
  - Displays the detected faces with bounding rectangles and shows the current frames per second (FPS).
- **`Haar_Cascade/CascadeClassifier_img.py`**:
  - Uses OpenCV's Haar Cascade Classifier to detect faces in an image.
  - Displays the image with detected faces outlined.

![](assets/frontal_face_detector.png)

### 2. Face Landmarks Detection

- **`face_landmark_detection_img.py`**:
  - Detects facial landmarks (e.g., eyes, nose, mouth) on faces in an image using dlib's pre-trained models.
  - Displays the image with detected landmarks marked.
- **`face_landmark_detection_video.py`**:
  - Detects facial landmarks on faces in a real-time video stream using dlib's pre-trained models.
  - Displays the video feed with detected landmarks and FPS information.
- **`face_recognition.py`**:
  - Recognizes faces in an image by detecting facial landmarks.
  - Displays the image with recognized landmarks highlighted.

![](assets/Face_Landmarks.png)

### 3. Face and Object Tracking

- **`face_tracking_dlib.py`**:
  - Tracks a face in real-time using dlib's correlation tracker and a webcam.
  - Displays the video feed with tracking rectangles and FPS information.
- **`face_tracking_info.py`**:
  - Similar to `face_tracking_dlib.py`, but includes additional on-screen information about tracking status.

<video width="640" height="360" controls autoplay>
  <source src="assets\face_tracking.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

- **`object_tracking_dlib.py`**:
  - Provides a user-interactive tracking system where the user selects an area in a video feed to be tracked.
  - Supports starting and stopping the tracking process with keyboard inputs.

```python
Firstly, Use the mouse to draw an object detection box
Then:
'1': starting tracking, '2': stop tracking, 'Esc': exit 
```

------

## Getting Started

### Prerequisites

- Python 3
- Install required packages:

```python
dlib==19.24.2
face-recognition==1.3.0
face-recognition-models==0.3.0
opencv-python==4.8.0
```

### Models

This project utilizes several pre-trained model files, including Haar feature classifiers and Dlib's facial landmark predictors. These model files have been uploaded to [Google Drive](https://drive.google.com/file/d/1fPyoU3EdS7ci2xBwMzytriceSQRk5YCM/view?usp=drive_link) and [Baidu Cloud(extraction code: dlib)](https://pan.baidu.com/s/1EjxcCdkaZGHGCSapSC9P4Q?pwd=dlib) for users to download as needed.

### Instructions

Download and extract the model files into the `models` folder within the local project directory.

```python
models
 ├── haarcascade_eye.xml
 ├── haarcascade_eye_tree_eyeglasses.xml
	······
 ├── shape_predictor_5_face_landmarks.dat
 └── shape_predictor_68_face_landmarks.dat
```

### Running the Scripts

- To run face detection on an image:

  ```python
  python face_detection/dlib_frontal_face_detector_img.py
  ```

- To start real-time face detection using the webcam:

  ```python
  python face_detection/dlib_frontal_face_detector_video.py
  ```

- To use track function ( including face tracking and object tracking):

  ```python
  python face_tracking/face_tracking_dlib.py	# for face tracking
  python face_tracking/object_tracking_dlib.py	# for object tracking
  ```

  
