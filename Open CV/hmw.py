import cv2
import os
image=cv2.imread(r"C:\Users\maxsc\Open CV\images\mountain image.jpg")
cv2.imshow("image1",image)
cv2.waitKey(0)
gaussianblurimage=cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("gaussian blur",gaussianblurimage)
cv2.waitKey(0)
medianblur=cv2.medianBlur(image,5)
cv2.imshow("medianblur",medianblur)
cv2.waitKey(0)
constantboarder=cv2.copyMakeBorder(gaussianblurimage,20,20,20,20,cv2.BORDER_CONSTANT,value=(255,255,255))
cv2.imshow("constantboarder",constantboarder)
cv2.waitKey(0)