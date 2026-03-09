import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
mode = 0  # 0 = normal, 1 = grayscale, 2 = edges, 3 = blur

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
    if key == ord('0'):
        mode = 0
    elif key == ord('1'):
        mode = 1
    elif key == ord('2'):
        mode = 2
    elif key == ord('3'):
        mode = 3
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
