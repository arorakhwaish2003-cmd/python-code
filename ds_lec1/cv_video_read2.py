# phle sirf img ai video lao
import cv2
cap=cv2.VideoCapture(0) # source lake de camera ka device pe
while True:
    ret,frame= cap.read() # jo bi cam me dikhra h use lake de
    if ret==False: # kuch img na bi ae tb bi continue rahe
        continue
    cv2.imshow('Image',frame) # agar kuchni dikhra hoga to return krega false
    #key=cv2.waitKey(0) # agar hum waitkey 0 denge to infinite hojaega multiple keys ka wait krega to stop
    key=cv2.waitKey(1) # 1 ms ke lie wait krega
    if key==ord('q'):  # ord means q ko ascii value me convert krde
        # q press krne ke bad cam ruk jaega or vid show honi band
        break

cap.release()
cv2.destroyAllWindows()