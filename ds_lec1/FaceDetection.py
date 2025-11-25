# phle sirf img ai video lao
import cv2
cap=cv2.VideoCapture(0)

while True:
    ret,frame= cap.read() 
    if ret==False: 
        continue
    gray_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Image',frame)
    cv2.imshow('Gray Image',gray_img)
    key=cv2.waitKey(1) 
    if key==ord('q'):  
        break

cap.release()
cv2.destroyAllWindows()