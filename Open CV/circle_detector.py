import cv2
import numpy as np

image=cv2.imread(r"C:\Users\maxsc\Open CV\images\circle.jfif")
cv2.imshow("iamge",image)
cv2.waitKey(0)
gimage=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
bimage=cv2.blur(gimage,(9,9))
cv2.imshow("blur",bimage)
cv2.waitKey(0)
halfresult=cv2.HoughCircles(bimage,cv2.HOUGH_GRADIENT,1,10,param1=50,param2=30,minRadius=5,maxRadius=100)
print(halfresult)
rr=np.uint16(np.around(halfresult))
#print(rr)
for i in rr[0,:]:
    x=i[0]
    y=i[1]
    r=i[2]
    nimage=cv2.circle(image,(x,y),r,(0,255,0),2)
    cv2.imshow("show the circles!",nimage)
    cv2.waitKey(0)

