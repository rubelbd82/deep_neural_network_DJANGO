from django.http import HttpResponse
from django.template import loader

from rest_framework.decorators import api_view
from rest_framework.response import Response

import numpy as np
import pandas as pd
import tensorflow as tf
from keras import backend as K
from keras.models import load_model


def index(request):
    template = loader.get_template('image_recognition/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def fer(request):
    template = loader.get_template('image_recognition/fer.html')
    context = {}
    return HttpResponse(template.render(context, request))

"""
@api_view(['POST'])
def recognize(request):
    try:
        queryDict = request.POST
        print(queryDict)

        # myDict = dict(queryDict)
        # print(myDict)
        # print(type(myDict))
        # from PIL import Image
        # img = Image.open(file)
        # img.show()
    except KeyError as e:
        print("Key error: " + str(e))

    return Response("{'name' : 'Farhad'}")

"""

# from django.conf import settings

import cv2
from keras.applications.vgg16 import VGG16, decode_predictions, preprocess_input
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, FileUploadParser
from image_recognition.singleton import KerasModel

@api_view(['POST'])
@parser_classes((MultiPartParser,))
def recognize(request):
    image_bytes = request.FILES['file'].read()
    img = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), -1)

    # print(request.META['HTTP_MODELNAME'])
    # print(image_bytes)

    gm = KerasModel.gModelObjs
    graph, model = gm.get('model_1')
    img_width, img_height = 224, 224

    im = cv2.resize(
        img,
        (img_width, img_height))

    im = np.expand_dims(im, axis=0).astype(np.float32)
    im = preprocess_input(im)
    print(im.shape)
    out = model.predict(im)

    model_classes = ["happy", "neutral", "sad"]
    print(model_classes[np.argmax(out)])
    print(out)
    print(model_classes[np.argmax(out)] + "Probability: ", out[0][np.argmax(out)])

    result = model_classes[np.argmax(out)] + "(" + str(out[0][np.argmax(out)]) + ")"



    return Response({
        'predictions': result
    })
