#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/5 6:08 下午
# @Author  : song
# @Email   : song_gis@163.com
# @gitee    : gitee.com/songliuchen
# @File    : 2_simple_linear_regression.py

import tensorflow as tf
from example_code.tools.utils.file_utils import read_file
from example_code.tools.utils.matlab_utils import draw_line, draw
import random
import os

# 设置日志级别0 全部，1提示，2警告，3错误
os.environ["TF_CPP_MIN_LOG_LEVEL"] = '3'


# 读取训练集和测试集
def read_data(item):
    return {"x": float(item.split(",")[0]), "y": float(item.split(",")[1])}


train_data = read_file(path="../../data/simple_linear_data_train.txt", custon_convert=read_data)
test_data = read_file(path="../../data/simple_linear_data_test.txt", custon_convert=read_data)

r = random.random
random.seed(123456)
random.shuffle(train_data, random=r)
random.shuffle(test_data, random=r)

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


class LossHistory(tf.keras.callbacks.Callback):
    def __init__(self, model):
        self.current_index = 0
        self.model = model

    def on_batch_start(self, batch, logs={}):
        print("dddddddddddddddddddddddddd" + str(batch))
        self.current_index += 1
        current_index = self.current_index
        # if current_index % 100 == 0:
        #     print("train loss:%s" % self.model)
        #     # 获取当前模型预测 k，b的值
        #     print("k_val:%s b_val:%s" % (w.numpy(), b.numpy()))
        #     loss_train_x.append(len(loss_train_x))
        #     loss_train_y.append(loss)
        #
        #     # 测试集部分
        #     x.assign(test_data_arr_x)
        #     y.assign(test_data_arr_y)
        #     loss_test_x.append(len(loss_train_x) - 1)
        #
        #     loss_test_y.append(loss)
        #     print("test loss:%s" % loss.numpy())
        #     print("")


def create_model():
    """
    相当于y= ax+b
    :return:
    """
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(1, input_dim=1, input_shape=(1,)))
    return model


# 创建模型
model = create_model()

# 设置梯度下降优化器
optimizer = tf.keras.optimizers.SGD(learning_rate=0.1)
model.compile(optimizer=optimizer, loss='mse')

# 进行模型训练
model.fit(train_data_arr_x, train_data_arr_y, epochs=5, batch_size=100, validation_steps=100,
          validation_data=(test_data_arr_x, test_data_arr_y), callbacks=[LossHistory(model)])

# 保存模型
checkpoint = tf.train.Checkpoint(optimizer=optimizer, linear_model=model)
saved_folder = "../../output/tf2_keras/"
if not os.path.exists(saved_folder):
    os.mkdir(saved_folder)
checkpoint.save(saved_folder + "linear_regression.ckpt")

# 实例化Checkpoint，指定恢复对象为model
new_model = create_model()
checkpoint_new = tf.train.Checkpoint(linear_model=new_model)
checkpoint_new.restore(tf.train.latest_checkpoint(saved_folder))
test_y = new_model.predict(test_data_arr_x)

# # 绘制loss折线图
# draw_line([{"x":loss_train_x,"y":loss_train_y,"name":"train_loss","color":"blue"},{"x":loss_test_x,"y":loss_test_y,"name":"test_loss","color":"red"}],{"x_name":"step","y_name":"loss","title":"loss/step"})
#
# 绘制离散点效果图
draw_data = [{"x": test_data_arr_x, "y": test_data_arr_y, "name": "real_val", "type": "point", "color": "blue"},
             {"x": test_data_arr_x, "y": test_y, "name": "pre_val", "type": "line", "color": "red"}]
draw(draw_data, {"x_name": "x", "y_name": "y", "title": "linear_regression"})
