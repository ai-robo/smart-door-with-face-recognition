''''
Capture multiple Faces from multiple users to be stored on a DataBase (dataset directory)
	==> Faces will be stored on a directory: dataset/ (if does not exist, pls create one)
	==> Each face will have a unique numeric integer ID as 1, 2, 3, etc

Based on original code by Anirban Kar: https://github.com/thecodacus/Face-Recognition
with additions by Marcelo Rovai - MJRoBot.org @ 21Feb18

'''
import subprocess
import time
import cv2
import os

#cam = cv2.VideoCapture(0)
#cam.set(3, 640) # set video width
#cam.set(4, 480) # set video height

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id
face_id = input('\n enter user id end press <return> ==>  ')

print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0

while(True):

    #ret, img = cam.read()
    subprocess.run("fswebcam --no-banner -d /dev/video0 -r 640x480 --jpeg 100 new.jpg", shell=True)
    img = cv2.imread("new.jpg")
    #img = cv2.flip(image, -1) # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #faces = face_detector.detectMultiScale(gray, 1.3, 5)
    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5
        ,
        minSize=(20, 20)
    )

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imwrite("new.jpg", img)

    print(count)
    time.sleep(0.5)
    if count >= 100: # Take 100 face sample and stop video
         break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
#cam.release()
#cv2.destroyAllWindows()
