# show krenge dog img using terminal
import cv2
img=cv2.imread('./dog.png')
cv2.imshow('Dog Image',img)
cv2.waitKey(5000) # wait till other key is pressed
cv2.destroyAllWindows() # like quit in selenium
