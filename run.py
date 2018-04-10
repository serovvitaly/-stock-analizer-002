import tensorflow as tf
from data_generator import loader as stock_data_loader
import numpy as np
import iris_data


import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

loader = stock_data_loader('data/GAZP_180101_180331.csv')

bars_on_chunk = 10

(train_x, train_y), (test_x, test_y) = loader.load_data(1, bars_on_chunk)

features = {}
feature_columns = []
for i in range(1, bars_on_chunk+1):
    i = str(i)
    feature_columns.append(tf.feature_column.numeric_column(key='open'+i))
    feature_columns.append(tf.feature_column.numeric_column(key='high'+i))
    feature_columns.append(tf.feature_column.numeric_column(key='low'+i))
    feature_columns.append(tf.feature_column.numeric_column(key='close'+i))
    feature_columns.append(tf.feature_column.numeric_column(key='vol'+i))
    features['open'+i] = np.array([6.4, 5.0])
    features['high'+i] = np.array([6.4, 5.0])
    features['low'+i] = np.array([6.4, 5.0])
    features['close'+i] = np.array([6.4, 5.0])
    features['vol'+i] = np.array([6.4, 5.0])

classifier = tf.estimator.DNNClassifier(
        feature_columns=feature_columns,
        hidden_units=[10, 10],
        n_classes=2)


def input_fn_train():
    labels = np.array([2, 1])
    return features, labels


train, test = iris_data.load_data()
print(type(train[1]))
#features, labels = train

#classifier.train(input_fn=input_fn_train, steps=10)