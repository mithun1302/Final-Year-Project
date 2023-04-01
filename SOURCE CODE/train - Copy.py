import numpy as np
from tensorflow import keras

import matplotlib.pyplot as plt
import os
import cv2
import random
import sklearn.model_selection as model_selection
import datetime
from model import createModel
from contextlib import redirect_stdout
categories = ["NonDemented", "MildDemented", "ModerateDemented", "VeryMildDemented"]

SIZE = 120



def getData():
    rawdata = []
    data = []
    dir = "./data/"
    for category in categories:
        path = os.path.join(dir, category)
        class_num = categories.index(category)
        for img in os.listdir(path):
            try:
                rawdata = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                new_data = cv2.resize(rawdata, (SIZE, SIZE))

                data.append([new_data, class_num])
            except Exception as e:
                pass

    random.shuffle(data)

    img_data = []
    img_labels = []
    for features, label in data:
        img_data.append(features)
        img_labels.append(label)
    img_data = np.array(img_data).reshape(-1, SIZE, SIZE, 1)
    img_data = img_data / 255.0
    img_labels = np.array(img_labels)

    return img_data, img_labels



data, labels = getData()
print(data)
print(labels)