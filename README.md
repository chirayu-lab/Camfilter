Webcam Filters with OpenCV

A real-time webcam filter demo using Python and OpenCV.
Switch between different filters while viewing your webcam feed.

Features

Display webcam video in real-time.

Apply multiple filters:

Normal color

Grayscale

Edge detection (Canny)

Blur (Gaussian Blur)

Switch filters using number keys 0–3.

Quit the program using 'q'.

Installation

Make sure you have Python 3.11.15 installed.

Create a virtual environment (optional but recommended):

python -m venv venv
venv\Scripts\activate

Upgrade pip:

pip install --upgrade pip

Install required packages:

pip install opencv-python
Usage

Save the Python script as webcam_filters.py.

Run the script:

python webcam_filters.py

Controls during video:

Key	Action
0	Normal color
1	Grayscale
2	Edge detection
3	Blur
q	Quit program
Code Example
import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
mode = 0  # 0=normal, 1=grayscale, 2=edges, 3=blur

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if mode == 1:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif mode == 2:
        frame = cv2.Canny(frame, 100, 200)
    elif mode == 3:
        frame = cv2.GaussianBlur(frame, (15, 15), 0)

    cv2.imshow("Camera Filters", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('0'): mode = 0
    elif key == ord('1'): mode = 1
    elif key == ord('2'): mode = 2
    elif key == ord('3'): mode = 3
    elif key == ord('q'): break

cap.release()
cv2.destroyAllWindows()
Requirements

Python 3.11.15

OpenCV (opencv-python)

Optional (if you want more advanced filters in the future):

MediaPipe, NumPy, TensorFlow, PyTorch, Ultralytics

Author

Chirayu Mishra
