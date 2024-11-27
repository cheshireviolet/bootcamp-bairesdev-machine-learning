import os
import random
import numpy as np
import keras
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
from keras.api.preprocessing import image
from keras.api.applications.imagenet_utils import preprocess_input
from keras.api.models import Sequential
from keras.api.layers import Dense, Dropout, Flatten, Activation
from keras.api.layers import Conv2D, MaxPooling2D
from keras.api.models import Model
import tensorflow as tf
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import pandas as pd
import seaborn as sns

# helper function to load image and return it and input vector
def get_image(path):
    img = image.load_img(path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return img, x

# Loads pre-trained model
model = tf.keras.models.load_model('cfvtest.keras')

#adding dataset
root = 'cfv_validation'
train_split, val_split = 0.7, 0.15

categories = [x[0] for x in os.walk(root) if x[0]][1:]
categories = [c for c in categories]

data = []
for c, category in enumerate(categories):
    images = [os.path.join(dp, f) for dp, dn, filenames
              in os.walk(category) for f in filenames
              if os.path.splitext(f)[1].lower() in ['.jpg','.png','.jpeg']]
    for img_path in images:
        img, x = get_image(img_path)
        data.append({'x':np.array(x[0]), 'y':c})

num_classes = len(categories)

random.shuffle(data)

idx_val = int(train_split * len(data))
idx_test = int((train_split + val_split) * len(data))
train = data[:idx_val]
val = data[idx_val:idx_test]
test = data[idx_test:]

x_train, y_train = np.array([t["x"] for t in train]), [t["y"] for t in train]
x_val, y_val = np.array([t["x"] for t in val]), [t["y"] for t in val]
x_test, y_test = np.array([t["x"] for t in test]), [t["y"] for t in test]

#Predict
y_pred = np.argmax(model.predict(x_test),axis=1)
classes = ['pale moon', 'kagero', 'narukami']

#Metrics
print(f"Accuracy: {accuracy_score(y_test,y_pred)}")
print(f"Sensitivity: {recall_score(y_test,y_pred,average='weighted')}")
print(f"Specificity: {recall_score(np.logical_not(y_test) , np.logical_not(y_pred))}")
print(f"Precision: {precision_score(y_test,y_pred,average='weighted')}")
print(f"f1: {f1_score(y_test,y_pred,average='weighted')}")

#Confusion Matrix
con_mat = confusion_matrix(y_true=y_test,y_pred=y_pred)
con_mat_norm = np.around(con_mat.astype('float')/ con_mat.sum(axis=1)[:,np.newaxis], decimals=2)

con_mat_df = pd.DataFrame(con_mat_norm, index = classes, columns = classes)

figure = plt.figure(figsize=(5,5))
sns.heatmap(con_mat_df,annot=True,cmap=plt.cm.PuRd)
plt.tight_layout()
plt.ylabel('True Label')
plt.xlabel('Predicted label')
plt.show()