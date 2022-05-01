#import mylib
import cv2
import face_recognition
import pyttsx3
import numpy as np
from mylib import getFile, findEncodings, speak, getImages, recognition, identification

def main():
    synthesizer = pyttsx3.init()

    path = "zdjecia\\"
    lines = getFile(path + "data.txt")
    images, taunts = getImages(path, lines)
    encodeListKnown = findEncodings(images)
    print('Encoding Complete')

    cam = cv2.VideoCapture(0) #front camera

    while True:
        success, img = cam.read()
        
        facesCurFrame, encodesCurFrame = recognition(img)
        
        for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
            id, target = identification(encodeFace, encodeListKnown)

            if target:
                text = taunts[id].upper()
                print (text)
                y1,x2,y2,x1 = faceLoc
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                
                speak(synthesizer,text)

        cv2.imshow('webcam',img)
        cv2.waitKey(1)

    



if __name__ == "__main__":
    main()