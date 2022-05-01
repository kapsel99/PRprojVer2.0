import cv2
import face_recognition
import pyttsx3
import numpy as np
import time

def getFile(path):
    DATA = []
    with open(path) as f:
        for line in f:
            data = line.strip().split(";")
            DATA.append(data)
    return DATA


def findEncodings(images):
    encodelist= []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist

def speak(synt, text):
    synt.say(text)           
    synt.runAndWait()
    synt.stop()

def getImages(path, lines):
    images = []
    taunts = []
    for person in lines:
        photo = person[0]
        curImg = cv2.imread(path+photo)
        images.append(curImg)
        taunts.append(person[1])
    return images, taunts

def recognition(frame):
    # frame = cv2.resize(frame, (0,0), None, 0.25,0.25)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    facesCurFrame = face_recognition.face_locations(frame)
    encodesCurFrame = face_recognition.face_encodings(frame,facesCurFrame)
    return facesCurFrame, encodesCurFrame

def identification(encodeFace, knownFaces):
    matches = face_recognition.compare_faces(knownFaces,encodeFace)
    faceDis = face_recognition.face_distance(knownFaces,encodeFace)
    matchIndex = np.argmin(faceDis)
    return matchIndex, matches[matchIndex]

def getFPS(lastTime):
    curTime = time.time()
    fps = 1.0 / (curTime - lastTime)
    return fps, curTime

def drawRec(frame, loc, col):
    y1,x2,y2,x1 = loc
    cv2.rectangle(frame,(x1,y1),(x2,y2),col,2)