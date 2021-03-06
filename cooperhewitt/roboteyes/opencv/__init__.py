#!/usr/bin/env python

import cv2
import cv2.cv as cv
import numpy

def load_from_path(path):

        return cv2.imread(path, cv2.CV_LOAD_IMAGE_COLOR)
        
def load_from_camera(camera=0):

        vidcap = cv2.VideoCapture()
        vidcap.open(camera)

        retval, img = vidcap.retrieve()
        vidcap.release()
        
        return img

def detect_faces(im, rules="haarcascade_frontalface_alt.xml"):
        return detect(im, rules)

def detect_eyes(im, rules="haarcascade_eye.xml"):
        return detect(im, rules)

def detect(im, rules):

        cascade = cv2.CascadeClassifier(rules)
        rects = cascade.detectMultiScale(im, scaleFactor=1.1, minNeighbors=3, minSize=(10, 10), flags = cv.CV_HAAR_SCALE_IMAGE)
        
        if len(rects) == 0:
                return None
                
        rects[:,2:] += rects[:,:2]
        return rects

def has_faces(im, rules):

        rsp = detect(im, rules)

        if rsp is None:
                return False

        return True

def draw_rectangles(im, rects, color=(0, 255, 0)):

        for x1, y1, x2, y2 in rects:
                cv2.rectangle(im, (x1, y1), (x2, y2), color, 2)
                
def save(im, path):
        cv2.imwrite(path, im)

if __name__ == '__main__':

        import sys

        path = sys.argv[1]
        rules = sys.argv[2]

        im = load_from_path(path)
        faces = detect_faces(im, rules)

        if faces is None:
                print "no faces"
                sys.exit()

        draw_rectangles(im, faces)
        save(im, "test.png")
