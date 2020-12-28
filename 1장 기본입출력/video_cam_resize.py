import cv2

cap = cv2.VideoCapture(0)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Original width : %d, height : %d" %(width,height))

cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Resized width: %d, height : %d" %(width,height))

if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow('camera',img)
            if cv2.waitKey(1) != -1:
                cv2.imwrite("photo.jpg",img)
                break
        else:
            print('no frame!')
else:
    print("can't open camera")

cap.release()
cv2.destroyWindow()



