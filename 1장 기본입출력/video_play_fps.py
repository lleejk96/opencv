import cv2

video_file = "../pythonProject6/running.webm"

cap = cv2.VideoCapture(video_file)
if cap.isOpened():
    fps = cap.get(cv2.CAP_PROP_FPS)  ##프레임 수 구하기
    delay = int(1000/fps)
    print("FPS: %f, DELAY: %dms" %(fps, delay))

    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow(video_file,img)
            cv2.waitKey(delay)  #fps에 밎게 시간 지연
        else:
            break
else:
    print("can't open video")
cap.release()        ## 캡처 자원 반납
cv2.destroyWindow()