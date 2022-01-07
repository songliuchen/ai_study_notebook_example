#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/5 6:08 下午
# @Author  : song
# @Email   : song_gis@163.com  
# @gitee    : gitee.com/songliuchen
# @File    : 2_simple_linear_regression.py

import tensorflow as tf
from example_code.tools.utils.file_utils import read_file
from example_code.tools.utils.matlab_utils import draw_line,draw
import random
#读取训练集和测试集
def read_data(item):
    return {"x": float(item.split(",")[0]), "y": float(item.split(",")[1])}

train_data = read_file(path = "../../data/simple_linear_data_train.txt",custon_convert = read_data)
test_data = read_file(path = "../../data/simple_linear_data_test.txt",custon_convert = read_data)

r=random.random
random.seed(123456)
random.shuffle(train_data,random=r)
random.shuffle(test_data,random=r)

train_data_arr_x = []
train_data_arr_y = []
for item in train_data:
    train_data_arr_x.append((item["x"]))
    train_data_arr_y.append((item["y"]))

test_data_arr_x = []
test_data_arr_y = []
for item in test_data:
    test_data_arr_x.append((item["x"]))
    test_data_arr_y.append((item["y"]))

x = tf.Variable([0.])
y = tf.Variable([0.])
w = tf.Variable(0.)
b = tf.Variable(0.)
variables = [w, b]

# 保存训练集损失值
loss_train_x = []
loss_train_y = []
# 保存测试集损失值
loss_test_x = []
loss_test_y = []

#总迭代次数
epouchs = 5
#单批次大小
batch_size = 100
#预热比例
wrap_rate = 0.01

#计算总训练步数
global_steps = epouchs*(len(train_data)/batch_size)
#根据预热比例计算预热步数
wrap_step = int(global_steps*wrap_rate)

# 实际值 - 预测值
optimizer = tf.keras.optimizers.SGD(learning_rate=0.1)
# 当前步数
current_step = 0
for epouch in range(epouchs):
    current_index = 0
    #每个epouch前重新排序数据
    random.shuffle(train_data, random=r)
    random.shuffle(test_data, random=r)
    while current_index<len(train_data):
        batch_end = current_index+batch_size
        if batch_end>len(train_data):
            batch_end = len(train_data)

        x.assign(train_data_arr_x[current_index:batch_end])
        y.assign(train_data_arr_y[current_index:batch_end])
        with tf.GradientTape() as tape:
            y1 = w * x + b
            loss = tf.reduce_mean(tf.square(y - y1))
        grads = tape.gradient(loss, variables)
        # 保存loss记录
        if current_index % 100 == 0 and current_step>wrap_step:
            print("train loss:%s" % loss)
            # 获取当前模型预测 k，b的值
            print("k_val:%s b_val:%s" % (w, b))
            loss_train_x.append(len(loss_train_x))
            loss_train_y.append(loss)

            #测试集部分
            x.assign(test_data_arr_x)
            y.assign(test_data_arr_y)
            loss_test_x.append(len(loss_train_x)-1)
            loss_test_y.append(loss)
            print("test loss:%s" % loss)
            print("")

        current_index += batch_size
        current_step+=1

x.assign(test_data_arr_x)
y.assign(test_data_arr_y)
loss_val_test = loss

# 绘制loss折线图
draw_line([{"x":loss_train_x,"y":loss_train_y,"name":"train_loss","color":"blue"},{"x":loss_test_x,"y":loss_test_y,"name":"test_loss","color":"red"}],{"x_name":"step","y_name":"loss","title":"loss/step"})

#绘制离散点效果图
draw_data = [{"x":test_data_arr_x,"y":test_data_arr_y,"name":"real_val","type":"point","color":"blue"},{"x":test_data_arr_x,"y":loss_val_test,"name":"pre_val","type":"line","color":"red"}]
draw(draw_data,{"x_name":"x","y_name":"y","title":"linear_regression"})