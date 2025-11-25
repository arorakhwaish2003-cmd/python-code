import cv2
cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")  # haarcascascade classifier dede

while True:
    ret,frame= cap.read() 
    if ret==False: 
        continue

    faces=face_cascade.detectMultiScale(frame,1.3,5)
    # detectMultipleScale me facaes ko detect krte h multiple
    # 1.3 means img ko 1.3 times zoom krde taki face visible ho
    #5 means agar sth sth box slide hoega to ek face ko bht baatdega
    # 5 means hum chahte h dur dur jake box bane thdi duri pe.

    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),[255,0,0],2) 
        # 255 rgb ka color 
        # x,y phla popint
        # x+w y+h dusra pt
        # 2 me box ki thickness 2px ho
    
    cv2.imshow('Image',frame)
   
    key=cv2.waitKey(1) 
    if key==ord('q'):  
        break

cap.release()
cv2.destroyAllWindows()