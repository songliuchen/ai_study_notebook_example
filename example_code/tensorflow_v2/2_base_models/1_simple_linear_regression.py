# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time    : 2022/1/5 6:08 下午
# # @Author  : song
# # @Email   : song_gis@163.com
# # @gitee    : gitee.com/songliuchen
# # @File    : 2_simple_linear_regression.py
#
# import tensorflow as tf
# from example_code.tools.utils.file_utils import read_file
# from example_code.tools.utils.matlab_utils import draw_line,draw
# import random
# import os
# #设置日志级别0 全部，1提示，2警告，3错误
# os.environ["TF_CPP_MIN_LOG_LEVEL"]='3'
#
# #读取训练集和测试集
# def read_data(item):
#     return {"x": float(item.split(",")[0]), "y": float(item.split(",")[1])}
#
# train_data = read_file(path = "../../data/simple_linear_data_train.txt",custon_convert = read_data)
# test_data = read_file(path = "../../data/simple_linear_data_test.txt",custon_convert = read_data)
#
# r=random.random
# random.seed(123456)
# random.shuffle(train_data,random=r)
# random.shuffle(test_data,random=r)
#
# train_data_arr_x = []
# train_data_arr_y = []
# for item in train_data:
#     train_data_arr_x.append((item["x"]))
#     train_data_arr_y.append((item["y"]))
#
# test_data_arr_x = []
# test_data_arr_y = []
# for item in test_data:
#     test_data_arr_x.append((item["x"]))
#     test_data_arr_y.append((item["y"]))
#
# x = tf.Variable([0.],shape=[None],validate_shape=False,name="x",dtype=tf.float32)
# y = tf.Variable([0.],shape=[None],validate_shape=False,name="y",dtype=tf.float32)
# w = tf.Variable(0.,name="w")
# b = tf.Variable(0.,name="b")
# variables = [w, b]
#
# # 保存训练集损失值
# loss_train_x = []
# loss_train_y = []
# # 保存测试集损失值
# loss_test_x = []
# loss_test_y = []
#
# #总迭代次数
# epouchs = 5
# #单批次大小
# batch_size = 100
# #预热比例,添加预热比例，避免一开始loss值过大，loss曲线效果不明显
# wrap_rate = 0.01
#
# #计算总训练步数
# global_steps = epouchs*(len(train_data)/batch_size)
# #根据预热比例计算预热步数
# wrap_step = int(global_steps*wrap_rate)
#
# # 当前步数
# current_step = 0
#
# # 损失函数：(实际值 - 预测值)求平方 再取均值
# optimizer = tf.keras.optimizers.SGD(learning_rate=0.1)  # 优化器
#
# def create_model():
#     model = tf.keras.Sequential()
#     model.add(tf.keras.layers.Dense(1,input_shape=(1,),input_dim=1))
#     return model
#
# def loss(model, x, y):
#     y1 = model(x)
#     return tf.reduce_mean(tf.square(y - y1))
#
# train_model = create_model()
# def get_gred(w,x,y,b,variables):
#     with tf.GradientTape() as tape:
#         y1 = train_model(x)
#         loss = loss(train_model,)
#     grad = tape.gradient(loss, variables)
#     return grad,y1,loss
#
# for epouch in range(epouchs):
#     current_index = 0
#     #每个epouch前重新排序数据
#     random.shuffle(train_data, random=r)
#     random.shuffle(test_data, random=r)
#     while current_index<len(train_data):
#         batch_end = current_index+batch_size
#         if batch_end>len(train_data):
#             batch_end = len(train_data)
#
#         x.assign(train_data_arr_x[current_index:batch_end])
#         y.assign(train_data_arr_y[current_index:batch_end])
#         #创建梯度优化器对象
#         grads,y1,loss = get_gred(w,x,y,b,variables)
#         optimizer.apply_gradients(grads_and_vars=zip(grads, variables))
#         # 保存loss记录
#         if current_index % 100 == 0 and current_step>wrap_step:
#             print("train loss:%s" % loss.numpy())
#             # 获取当前模型预测 k，b的值
#             print("k_val:%s b_val:%s" % (w.numpy(), b.numpy()))
#             loss_train_x.append(len(loss_train_x))
#             loss_train_y.append(loss)
#
#             #测试集部分
#             x.assign(test_data_arr_x)
#             y.assign(test_data_arr_y)
#             loss_test_x.append(len(loss_train_x)-1)
#
#             # 创建梯度优化器对象
#             grads, y1,loss = get_gred(w, x, y, b, variables)
#
#             loss_test_y.append(loss)
#             print("test loss:%s" % loss.numpy())
#             print("")
#
#         current_index += batch_size
#         current_step+=1
#
# # 绘制loss折线图
# draw_line([{"x":loss_train_x,"y":loss_train_y,"name":"train_loss","color":"blue"},{"x":loss_test_x,"y":loss_test_y,"name":"test_loss","color":"red"}],{"x_name":"step","y_name":"loss","title":"loss/step"})
#
# # 保存模型
# model = tf.keras.Sequential()
# root = tf.train.Checkpoint(optimizer=optimizer, linear_model=model)
# saved_folder = "../../output/tf2/"
# if not os.path.exists(saved_folder):
#     os.mkdir(saved_folder)
# root.save(saved_folder+"linear_regression.ckpt")
#
# # # 加载模型
# # x.assign(test_data_arr_x)
# # y.assign(test_data_arr_y)
# #
# # # 创建梯度优化器对象
# # grads, y1,loss = get_gred(w, x, y, b, variables)
# #
# # loss_val_test = y1
#
# #实例化Checkpoint，指定恢复对象为model
# new_model = tf.keras.Sequential()
# checkpoint = tf.train.Checkpoint(linear_model1=new_model)
# checkpoint.restore(tf.train.latest_checkpoint(saved_folder))
#
# test_y = new_model.predict(test_data_arr_x)
# #绘制离散点效果图
# draw_data = [{"x":test_data_arr_x,"y":test_data_arr_y,"name":"real_val","type":"point","color":"blue"},{"x":test_data_arr_x,"y":test_y,"name":"pre_val","type":"line","color":"red"}]
# draw(draw_data,{"x_name":"x","y_name":"y","title":"linear_regression"})