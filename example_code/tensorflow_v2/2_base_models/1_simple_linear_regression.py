#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/5 6:08 下午
# @Author  : song
# @Email   : song_gis@163.com  
# @gitee    : gitee.com/songliuchen
# @File    : 2_simple_linear_regression.py

import tensorflow as tf
from example_code.tools.utils.file_utils import read_file


def read_data(item):
    return {"x": float(item.split(",")[0]), "y": float(item.split(",")[1])}


train_data = read_file(path="../../data/simple_linear_data_train.txt", custon_convert=read_data)
test_data = read_file(path="../../data/simple_linear_data_test.txt", custon_convert=read_data)

test_data_arr_x = []
test_data_arr_y = []
for item in test_data:
    test_data_arr_x.append((item["x"]))
    test_data_arr_y.append((item["y"]))

x = tf.Variable(0.)
y = tf.Variable(0.)

k = tf.Variable(0.)
b = tf.Variable(0.)
variables = [k, b]
y1 = k * x + b

# 实际值 - 预测值
optimizer = tf.keras.optimizers.SGD(learning_rate=0.1)
for (index, item) in enumerate(train_data):
    x.assign(item["x"])
    y.assign(item["y"])
    with tf.GradientTape() as tape:
        y1 = k * x + b
        loss = tf.reduce_mean(tf.square(y - y1))
    grads = tape.gradient(loss,variables)
    if index % 100 == 0:
        optimizer.apply_gradients(grads_and_vars=zip(grads, variables))
        print("train loss %f" % loss)
        x_test = tf.constant(test_data_arr_x)
        y_test = k * x_test + b
        loss_val_test = tf.reduce_mean(tf.square(test_data_arr_y - y_test))
        print("test loss %f" % loss_val_test)
