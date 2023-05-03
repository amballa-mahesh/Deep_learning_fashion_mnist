# -*- coding: utf-8 -*-
"""Deep_learning_fashion_mnist.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C99epROwhj0CdumKYKsN0DhkJ_C5vKbc
"""

import tensorflow

from tensorflow.keras.datasets import fashion_mnist
import numpy as np

(x_train,y_train),(x_test,y_test) = fashion_mnist.load_data()

dic = {0:'T-shirt/top',
       1:'Trouser',
       2:'Pullover',
       3: 'Dress',
       4:'Coat',
       5:'Sandal',
       6:'Shirt',
       7:'Sneaker',
       8:'Bag',
       9:'Ankle boot'}

import matplotlib.pyplot as plt

x_train.shape

plt.figure(figsize = (3,3))
plt.imshow(x_train[0])
plt.show()
print(dic[y_train[0]])

x_train.shape,x_test.shape,y_train.shape,y_test.shape

x_train = x_train.reshape(60000,28*28)
x_test  = x_test.reshape(10000,28*28)
x_train = x_train/255
x_test  = x_test/255

x_train.shape,x_test.shape

y_train = tensorflow.keras.utils.to_categorical(y_train)
y_test  = tensorflow.keras.utils.to_categorical(y_test)

y_train.shape,y_test.shape

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout

model = Sequential()
model.add(Dense(784, activation = 'leaky_relu',input_shape = [x_train.shape[1],]))

model.add(Dense(20, activation = 'leaky_relu'))
model.add(Dropout(rate= 0.2))

model.add(Dense(15, activation = 'leaky_relu'))
model.add(Dropout(rate= 0.2))

model.add(Dense(10, activation = 'softmax'))

model.compile(optimizer ='adam',
              loss= 'categorical_crossentropy',
              metrics = 'accuracy')

model.fit(x_train, y_train, epochs =50, validation_data = (x_test,y_test),batch_size = 64)

y_pred = model.predict(x_test).round()

from sklearn.metrics import classification_report,accuracy_score,multilabel_confusion_matrix

print(classification_report(y_test,y_pred))

print(accuracy_score(y_test,y_pred))

l1 = list(dic.values())
l1

print(multilabel_confusion_matrix(y_test,y_pred))

for i in range (20,30):
  plt.figure(figsize = (2,2))
  plt.imshow(x_test[i].reshape(28,28))
  plt.show()
  print(dic[np.argmax(y_pred[i])],'\n')