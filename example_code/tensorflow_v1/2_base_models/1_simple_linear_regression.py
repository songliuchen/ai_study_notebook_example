#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/5 6:08 下午
# @Author  : song
# @Email   : song_gis@163.com
# @gitee    : gitee.com/songliuchen
# @File    : 2_simple_linear_regression.py

import tensorflow as tf
import os
from example_code.tools.utils.matlab_utils import draw_line,draw
import random

#设置日志级别0 全部，1提示，2警告，3错误
os.environ["TF_CPP_MIN_LOG_LEVEL"]='3'

from example_code.tools.utils.file_utils import read_file
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

#定义线性函数需要的变量 y = wx+b
with tf.name_scope('input'):
    x = tf.placeholder(dtype=tf.float32,name="x")
    y = tf.placeholder(dtype=tf.float32,name="y")
with tf.name_scope('layer'):
    with tf.name_scope('wights'):
        w = tf.Variable(0.)
    with tf.name_scope('biases'):
        b = tf.Variable(0.)
    # 定义线性函数公式
    with tf.name_scope('wx_plus_b'):
        y1 = w*x+b

# 损失函数：(实际值 - 预测值)求平方 再取均值
with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.square(y-y1))
#梯度下降优化器
with tf.name_scope('train'):
    train = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.initialize_all_variables()

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
#预热比例,添加预热比例，避免一开始loss值过s大，loss曲线效果不明显
wrap_rate = 0.01

#计算总训练步数
global_steps = epouchs*(len(train_data)/batch_size)
#根据预热比例计算预热步数
wrap_step = int(global_steps*wrap_rate)

# 当前步数
current_step = 0
with tf.Session() as sess:
    sess.run(init)
    #保存网络图
    writer = tf.summary.FileWriter('../../output/logs/', sess.graph)
    for epouch in range(epouchs):
        current_index = 0
        #每个epouch前重新排序数据
        random.shuffle(train_data, random=r)
        random.shuffle(test_data, random=r)
        while current_index<len(train_data):
            batch_end = current_index+batch_size
            if batch_end>len(train_data):
                batch_end = len(train_data)

            # run 优化函数
            _,loss_val,w_val, b_val = sess.run([train,loss,w,b], feed_dict={x: train_data_arr_x[current_index:batch_end],y: train_data_arr_y[current_index:batch_end]})
            loss_val_test = sess.run(loss, feed_dict={x: test_data_arr_x, y: test_data_arr_y})

            # 保存loss记录
            if current_index % 100 == 0 and current_step>wrap_step:
                print("train loss:%s" % loss_val)
                # 获取当前模型预测 k，b的值
                print("k_val:%s b_val:%s" % (w_val, b_val))
                print("test loss:%s" % loss_val_test)
                print("")
                loss_train_x.append(len(loss_train_x))
                loss_train_y.append(loss_val)

                loss_test_x.append(len(loss_train_x)-1)
                loss_test_y.append(loss_val_test)

            current_index += batch_size
            current_step+=1

    #保存网络图
    writer.close()

    # 保存模型
    saved_folder = "../../output/tf1/"
    if (not os.path.exists(saved_folder)):
        os.mkdir(saved_folder)
    saver = tf.train.Saver(max_to_keep=1)
    saver.save(sess, saved_folder+"linear_regression.ckpt")

# 绘制训练集和测试集loss折线图
draw_line([{"x":loss_train_x,"y":loss_train_y,"name":"train_loss","color":"blue"},{"x":loss_test_x,"y":loss_test_y,"name":"test_loss","color":"red"}],{"x_name":"step","y_name":"loss","title":"loss/step"})

# 加载模型，执行预测整个测试集
with tf.Session() as sess_2:
    saver.restore(sess_2, tf.train.latest_checkpoint(saved_folder))

    # 获取最后测试集上效果
    test_y = sess_2.run(y1, feed_dict={x: test_data_arr_x, y: test_data_arr_y})

#绘制离散点效果图
draw_data = [{"x":test_data_arr_x,"y":test_data_arr_y,"name":"real_val","type":"point","color":"blue"},{"x":test_data_arr_x,"y":test_y,"name":"pre_val","type":"line","color":"red"}]
draw(draw_data,{"x_name":"x","y_name":"y","title":"linear_regression"})




