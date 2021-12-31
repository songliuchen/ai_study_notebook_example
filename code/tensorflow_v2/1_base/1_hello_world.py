'''
1、tensorflow 常量、变量、占位符使用
2、tensorflow 加、减、乘、除、转置数学运算
3、tensorflow multiply 与matmul 区别
'''

# 引入tensorflow，一般给个简称
import tensorflow as tf
import os

#设置日志级别0 全部，1提示，2警告，3错误
os.environ["TF_CPP_MIN_LOG_LEVEL"]='3'

#定义字符串常量
text = tf.constant("hello word")
#tensorflow1.0默认使用静态图方式，直接、印d得不到结果
print("打印原始text对象")
print(text)

# python3.x str变量默认采用unicode类型，需要调用decode()
print(text.numpy().decode())

# 打印数字
num_int = tf.constant(100,dtype=tf.int32)
num_float = tf.constant(1.01,dtype=tf.float32)
print("int型数字%d" % num_int.numpy())
print("float型数字%.2f" % num_float.numpy())

# 打印变量
var1 = tf.Variable(0.2,dtype=tf.float32)
print("打印变量结果 %.2f" % var1.numpy())
for i in range(5):
    #给变量赋值
    var1 = var1.assign(i+1)
    print("更新变量值%s" % var1.numpy())

#占位符的使用
#占位符使用run时需要先喂数据，sess.run(feed_dict=)参数指定
# x = tf.placeholder(dtype=tf.int32)
# var1 = tf.Variable(5,dtype=tf.int32)
# init = tf.initialize_all_variables()
# with tf.Session() as sess:
#     result = sess.run(x,feed_dict={x:[12]})
#     print("打印矩阵占位符结果%s" % result)
#
#     print("打印变量中占位符结果")
#     sess.run(init)
#     # 将变量结果赋值给占位符
#     val1 = sess.run(var1)
#     #此处常出现的的一个问题是feed_dict 的key不能用"x",而需要用上面定义的变量x，否则会报错
#     result = sess.run(x, feed_dict={x: val1})
#
#     # 将占位符结果赋值给变量并打印
#     update = tf.assign(var1,result+1)
#     sess.run(update)
#     val1 = sess.run(var1)
#     print("将占位符的结果更新到变量中：%d" % val1)
