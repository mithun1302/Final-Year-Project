import tensorflow as tf
from tensorflow import keras
import cv2
import matplotlib.pyplot as plt
import  numpy as np
SIZE = 120
model = keras.models.load_model(r'C:\Users\RE_cs_3\Desktop\TECHNICAL-SOLUTIONS-FOR-VISUALLY-IMPAIRED-master\alzheimer-stage-classifier-master\model\model.h5')
categories = ["NonDemented", "MildDemented", "ModerateDemented", "VeryMildDemented"]

nimage = cv2.imread(r"C:\Users\RE_cs_3\Desktop\TECHNICAL-SOLUTIONS-FOR-VISUALLY-IMPAIRED-master\alzheimer-stage-classifier-master\test\1.jpg", cv2.IMREAD_GRAYSCALE)
image = cv2.resize(nimage,(SIZE,SIZE))
image = image/255.0
prediction = model.predict(np.array(image).reshape(-1,SIZE,SIZE,1))
pclass = np.argmax(prediction)
plt.imshow(image,cmap="gray")
pValue = "Prediction: {0}".format(categories[int(pclass)])
plt.title(pValue)
realvalue = "Real Value 1"
plt.figtext(0,0,realvalue)
plt.show()
# import os
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# from tensorflow import keras
# import tensorflow as tf
# from model import createModel


# def predict(SIZE):
#     categories = ["NonDemented", "MildDemented", "ModerateDemented", "VeryMildDemented"]

#     path = r"C:\Users\RE_cs_3\Desktop\alzheimer-stage-classifier-master\1.jpg"
#     images = []
# #     for img in os.listdir(path):
# #         data = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
# #         print(data)
# #         new_data = cv2.resize(data, (SIZE, SIZE))
# #         new_data = new_data / 255.0
# #         images.append(new_data)
# #     model = createModel()
# #     x = 0
# #     for img ,indx,value in images,enumerate(title):
#     image_1 = cv2.imread(r"C:\Users\RE_cs_3\Desktop\alzheimer-stage-classifier-master\test\1.jpg")
#     new_data = cv2.resize(image_1, (SIZE, SIZE))
#     image = np.array(new_data).reshape(-1, SIZE, SIZE, 1)
#     prediction = model.predict(image)
#     plt.imshow(image_1, cmap="gray")
#     ptitle = "Prediction: {0}".format(categories[np.argmax(prediction)])
#     title = os.listdir('./test')
    
# #     plt.figtext(0, 0, title[indx])
#     plt.title(ptitle)
#     plt.show()
#     print(prediction)


#     print(len(images), len(title))


# predict(120)
