import cv2

img_file = "../pythonProject6/image.jpg"
save_file = "../pythonProject6/save.jpg"
img = cv2.imread(img_file, cv2.IMREAD_COLOR)

if img is not None:
    cv2.imshow(img_file,img)
    cv2.imwrite(save_file,img);
    cv2.waitKey()
    cv2.destroyWindow()
else:
    print('No image file')