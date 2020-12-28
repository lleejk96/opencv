import cv2

video_file = "../pythonProject6/running.webm"

cap = cv2.VideoCapture(0)  ##0번을 통해서 웹캠에 접근

if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow('camera', img)
            if cv2.waitKey(1) != -1:
                break
        else:
            break

else:
    print("can't open video")
cap.release()
cv2.destroyAllWindow()