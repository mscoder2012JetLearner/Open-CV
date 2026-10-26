import cv2
import os
image=cv2.imread(r"C:\Users\maxsc\Open CV\images\imagehw1.jfif")
cv2.imshow("The Image...",image)
cv2.waitKey(0)
greyimage=cv2.imread(r"C:\Users\maxsc\Open CV\images\imagehw1.jfif",0)
cv2.imshow("Greyscale image",greyimage)
cv2.waitKey(0)
part=r"C:\Users\maxsc\Open CV\images"
os.chdir(part)
cv2.imwrite("homeworkimage1.jpg",image)
