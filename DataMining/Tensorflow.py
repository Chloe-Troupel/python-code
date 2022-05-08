import tensorflow as tf #Tensorflow is a deep learning library. scikit-learn is a more traditional machine learning library.
from sklearn import datasets
import matplotlib.pyplot as plot
    
digits = datasets.load_digits()
training_size = int(digits.images.shape[0]/2)

training_images = digits.images[0:training_size]
training_images = training_images.reshape((training_images.shape[0], -1))

training_target = digits.target[0:training_size]

classifier = tf.contrib.learn.DNNClassifier(
     feature_columns=[tf.contrib.layers.real_valued_column("", dtype=tf.float64)],
     # 2 hidden layers of 50 nodes each
     hidden_units=[50, 50],
     # 10 classes: 0, 1, 2...9
     n_classes=10)

#training
classifier.fit(training_images, training_target, steps=100)

#prediction
predict_images = digits.images[training_size+1:]

predict = classifier.predict(predict_images[1].reshape(1,-1))
print("\n",list(predict))
plot.imshow(predict_images[1], cmap=plot.cm.gray_r)
plot.show()
