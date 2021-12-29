'''
1、tensorflow 常量、变量、占位符使用
2、tensorflow 加、减、乘、除数学运算
'''

# 引入tensorflow，一般给个简称
import tensorflow as tf
import os

#设置日志级别0 全部，1提示，2警告，3错误
os.environ["TF_CPP_MIN_LOG_LEVEL"]='3'

#定义字符串常量
text = tf.constant("hello word")
#tensorflow1.0默认使用静态图方式，直接答应得不到结果
print("打印原始text对象")
print(text)

#tensorflow1.0默认需要创建会话，才能获取最终结果
# 会话创建方式1，直接创建，用完关闭
sess = tf.Session()
print("写法1——在会话中答应结果")
result = sess.run(text)
print(str(result,'utf-8'))
sess.close()

# 会话创建方式2，with创建，自动关闭（默认采用第二种方式）
with tf.Session() as sess:
    print("写法2——在会话中答应结果")
    result = sess.run(text)
    print(str(result,'utf-8'))

# 打印数字
num = tf.constant(1.01,dtype=tf.float32)
with tf.Session() as sess:
    result = sess.run(num)
    print(result)

# 打印变量
val1 = tf.Variable(0.,dtype=tf.float32)
init = tf.initialize_all_variables()
with tf.Session() as sess:
    sess.run(init)
    result = sess.run(val1)
    print("打印变量原始结果")
    print(result)
    for i in range(5):
        update1 = tf.assign(val1, i+1)
        sess.run(update1)
        result = sess.run(val1)
        print("更新变量值%s" % str(i+1))
        print(result)



