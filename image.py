#this little piece  of code just 
import cv2
image = cv2.imread("image directory")
print(image.shape)
cv2.imshow("Image", image)
cv2.waitKey(0)