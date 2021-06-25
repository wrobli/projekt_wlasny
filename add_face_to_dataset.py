import cv2
import os

cam = cv2.VideoCapture(0)
cam.set(3, 1024) #video width
cam.set(4, 768) #video height

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


face_id = input('\n Wprowadz identyfikator uzytkownia /RFID/ID:   ')

print("\n ...Trwa skanowanie twarzy. Patrz prosto w kamere... ")

count = 0

while(True):

    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5,minSize=(40, 40))

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("data/ID." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('Add face to data set', img)

    k = cv2.waitKey(100) & 0xff # ESC to exit
    if k == 27:
        break
    elif count >= 50: # Define number of samples
         break


print("\n GOTOWE ! Dane zostaly zebrane. ")
cam.release()
cv2.destroyAllWindows()


