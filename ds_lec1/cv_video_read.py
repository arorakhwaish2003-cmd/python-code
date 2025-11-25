import cv2
cap=cv2.VideoCapture(0) # source lake de camera ka device pe
# 0 islie ki device pe bhot sare cams h default cam lake dede
ret,frame= cap.read() # jo bi cam me dikhra h use lake de

cv2.imshow('Image',frame) # agar kuchni dikhra hoga to return krega false

cap.release() #cam band ni hoga jab tk ye ni krenge band krne ke bad bi
cv2.waitKey()
cv2.destroyAllWindows()