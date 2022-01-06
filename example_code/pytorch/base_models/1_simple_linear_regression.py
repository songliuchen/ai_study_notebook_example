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
    return {"x":item.split(",")[0],"y":item.split(",")[1]}

train_data = read_file(path = "../../data/simple_linear_data_train.txt",custon_convert = read_data)
test_data = read_file(path = "../../data/simple_linear_data_test.txt",custon_convert = read_data)

test_data_arr_x = []
test_data_arr_y = []
for item in test_data:
    test_data_arr_x.append((float(item["x"])))
    test_data_arr_y.append((float(item["y"])))

# x = tf.placeholder(dtype=tf.float32)
# y = tf.placeholder(dtype=tf.float32)
#
# k = tf.Variable(dtype=tf.float32)
# b = tf.Variable(dtype= tf.float32)
# y1 = k*x+b
#
# # 实际值 - 预测值
# loss = tf.reduce_mean(tf.square(y-y1))
# optimizer = tf.train.GradientDescentOptimizer(0.1)
# train  = optimizer.minimize(loss)
#
# with tf.Session() as sess:
#     for (index,item) in enumerate(train_data):
#         sess.run(train,feed_dict={x:float(item["x"]),y:float(item["y"])})
#         if index % 100 ==0:
#             loss_val = sess.run(loss,feed_dict={x:item["x"],y:item["y"]})
#             print("train loss %f" % loss_val)
#             loss_val_test = sess.run(loss, feed_dict={x: test_data_arr_x, y: test_data_arr_y})
#             print("test loss %f" % loss_val_test)





