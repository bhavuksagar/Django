from django.shortcuts import render,redirect
import cv2
from PIL import Image
import numpy as np
import cv2
from PIL import Image
import numpy as np

# Create your views here.
def home(request):
    return render(request,'home.html')


def out(request):

    face=cv2.CascadeClassifier("/Users/sahilsagar/Desktop/Django/test/web/face/face.xml")
    cam=cv2.VideoCapture(0)

    while True:
        check,frame=cam.read()
        faces=face.detectMultiScale(frame,1.3,5)
        for x,y,w,h in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,220),2)
        cv2.imshow("face",frame)
        key=cv2.waitKey(1)
        if key==ord('q'):
            break
    cam.release()
    cv2.destroyAllWindow()

    return redirect('/')
