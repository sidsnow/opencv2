import cv2
import time


def video_proc():
    left = right = 0
    cap = cv2. VideoCapture('sample.mp4')
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        ret, thresh = cv2.threshold(gray, 105, 255, cv2.THRESH_BINARY_INV)

        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                               cv2.CHAIN_APPROX_NONE)
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            centerx = x+w//2
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        h, w = frame.shape[:2]
        cv2.line(frame, (w//2, 0), (w // 2, h), (255, 0, 0), 2)

        center = w//2
        if centerx > center:
            right+=1
        elif centerx < center:
            left+=1

        cv2.putText(frame, str(f"left: {left}, right: {right}"), (0, 15), 1, 1, (255, 255, 255))

        cv2.imshow('vid', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(0.1)
    cap.release()


video_proc()
cv2.waitKey(0)
cv2.destroyAllWindows()
