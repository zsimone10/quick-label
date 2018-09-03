from flask import Flask, request, Response
import json
import sys
import base64
import os
import numpy as np
import cv2 as cv

curLabelIdx = 0

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello world'

@app.route('/retrieve_labels')
def sendLabels():
    f = open("labels.txt", "r")
    labels = []
    for line in f.readlines():
        labels.append(line)
    print(labels)
    return Response(response=json.dumps({"labels": labels}), status=200, mimetype="application/json")

@app.route('/send_image', methods=['POST'])
def saveImage():
    global curLabelIdx
    #print(request.data, file=sys.stdout)
    fileDir = 'examples'
    if not os.path.exists(fileDir):
        os.makedirs(fileDir)
    d = json.loads(request.data.decode('utf-8'))
    imgEncoding = base64.b64decode(d['data'])
    #print(imgEncoding)
    img = np.fromstring(imgEncoding, np.uint8)
    img = cv.imdecode(img, cv.IMREAD_COLOR)
    #cv.imshow('image',img)
    cv.imwrite(fileDir + '/{}.jpg'.format(curLabelIdx) , img)
    curLabelIdx += 1
    return Response(response=json.dumps({"res": "recieved"}), status=200, mimetype="application/json")
