import cv2
import os
image=cv2.imread(r"C:\Users\maxsc\Open CV\images\mountain image.jpg")
# cv2.imshow("image1",image)
# cv2.waitKey(0)
# gaussianblurimage=cv2.GaussianBlur(image,(7,7),0)
# cv2.imshow("gaussian blur",gaussianblurimage)
# medianblur=cv2.medianBlur(image,7)
# cv2.imshow("medianblur",medianblur)
# bilateralblur=cv2.bilateralFilter(image,1,255,1)
# cv2.imshow("bilateralblur",bilateralblur)
# cv2.waitKey(0)
# edges=cv2.Canny(image,100,200)
# cv2.imshow("edges",edges)
# part=r"C:\Users\maxsc\Open CV\images"
# os.chdir(part)
# cv2.imwrite("cool mountain.png",edges)
# cv2.waitKey(0)
# constantboarder=cv2.copyMakeBorder(image,50,50,50,50,cv2.BORDER_CONSTANT,value=(255,255,255))
# cv2.imshow("constantboarder",constantboarder)
# cv2.waitKey(0)
# constantboarder2=cv2.copyMakeBorder(constantboarder,25,25,25,25,cv2.BORDER_CONSTANT,value=(0,0,0))
# cv2.imshow("doubleboarder",constantboarder2)
# cv2.waitKey(0)
# reflectboarder=cv2.copyMakeBorder(image,50,50,50,50,cv2.BORDER_REFLECT)
# cv2.imshow("reflect boarder",reflectboarder)
# cv2.waitKey(0)
a=image.shape
rows=a[0]
collums=a[1]
colourchanels=a[2]
r=rows/2
c=collums/2
rm=cv2.getRotationMatrix2D((c,r),45,0.7)
rotatedimage=cv2.warpAffine(image,rm,(collums,rows))
cv2.imshow("rotatedimage",rotatedimage)
b=rotatedimage.shape
rows2=a[0]
collums2=a[1]
r2=rows2/2
c2=collums2/2
rm2=cv2.getRotationMatrix2D((c2,r2),-90,0.7)
rotatedimage2=cv2.warpAffine(rotatedimage,rm2,(collums2,rows2))
cv2.imshow("rotatedimage2",rotatedimage2)
cv2.waitKey(0)
greyscale=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("greyscale",greyscale)
cv2.waitKey(0)
hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow("hsv",hsv)
cv2.waitKey(0)