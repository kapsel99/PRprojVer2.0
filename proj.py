import os

import cv2
import face_recognition
import pyttsx3
import numpy as np
import time
import sys
from mylib import *

def main():
    green = (0, 255, 0)
    red = (0, 0, 255)
    blue = (255, 0, 0)  # colors

    synthesizer = pyttsx3.init()
    synthesizer.setProperty('rate', 200)
    synthesizer.setProperty('volume', 0.5)
    setLanguage(synthesizer,'polish')
    # setLanguage(synthesizer, 'english')
    path = "zdjecia\\"
    lines = getFile(path + "data.txt")
    images, taunts = getImages(path, lines)
    encodeListKnown = findEncodings(images)
    print('Encoding Complete')

    cam = cv2.VideoCapture(0)  # front camera
    if not cam.isOpened():
        print("Could not open video")
        sys.exit()

    lastTime = time.time()

    while True:
        success, img = cam.read()

        facesCurFrame, encodesCurFrame = recognition(img)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            drawRec(img, faceLoc, green)

            id, target = identification(encodeFace, encodeListKnown)

            if target:
                text = taunts[id].upper()
                print(text)
                drawRec(img, faceLoc, red)
                speak(synthesizer, text)


        fps, lastTime = getFPS(lastTime)
        cv2.putText(img, "FPS : " + str(round(fps, 2)), (50, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)

        cv2.imshow('webcam', img)
        k = cv2.waitKey(1)
        # Ponaciśnieciu przycisku 1 (przy raspberry jakis przycisk, przy GUI podobnie)
        if k == 49:
                addingFace(img)
        #if k == 32: #po nacisnieciu spacji resetuje kamere
         #   print("Restarting camera, please wait!")
          #  os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
        #powyzsza czesc programu dziala tylko wtedy gdy zmienie ustawienia w 'EDIT CONFIGURATION', klikajac 'RUN WITH PYTHON CONSOLE'
        #ale wtedy nie dziala zamykanie pliku xD
        if k == 27:
            break
    cam.release()

if __name__ == "__main__":
    main()