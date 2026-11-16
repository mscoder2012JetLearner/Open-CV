import cv2
image=cv2.imread(r"C:\Users\maxsc\Open CV\images\blobs.jfif")
cv2.imshow("blobs",image)
cv2.waitKey(0)
greyimage=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("grey blobs",greyimage)
cv2.waitKey(0)

