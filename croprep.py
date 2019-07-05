import cv2
import numpy as np

face1='C:\\Users\\HP\\Desktop\\face1.jpg'
face2='C:\\Users\\HP\\Desktop\\face2.jpg'
img1=cv2.imread(face1)
print(img1)
img11=img1
img2=cv2.imread(face2)
print(img2)
img22=img2
#print(img.shape)

#cv2.imshow("face1",img) ##displays the whole picture
fc1=img1[80:130,50:170]

fc2=img2[80:130,50:170]
#cv2.waitKey(0)

cv2.imshow("cropped img1",fc1)
cv2.waitKey(0)
cv2.imshow("cropped img2",fc2)
cv2.waitKey(0)

img11[80:130,50:170]=fc2
cv2.imshow("rep1",img11)
cv2.waitKey(0)

img22[80:130,50:170]=fc1
cv2.imshow("rep2",img22)
cv2.waitKey(0)

cv2.destroyAllWindows()
