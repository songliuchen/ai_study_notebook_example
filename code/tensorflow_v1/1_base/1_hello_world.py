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
#tensorflow1.0默认使用静态图方式，直接、印d得不到结果
print("打印原始text对象")
print(text)

#tensorflow1.0默认需要创建会话，才能获取最终结果
# 会话创建方式1，直接创建，用完关闭
sess = tf.Session()
print("写法1——在会话中打印结果")
result = sess.run(text)
#不加str貌似答应的byte类型
print(str(result,'utf-8'))
sess.close()

# 会话创建方式2，with创建，自动关闭（默认采用第二种方式）
with tf.Session() as sess:
    print("写法2——在会话中打印结果")
    result = sess.run(text)
    print(str(result,'utf-8'))

# 打印数字
num_int = tf.constant(100,dtype=tf.int32)
num_float = tf.constant(1.01,dtype=tf.float32)
with tf.Session() as sess:
    result = sess.run(num_int)
    print("int型数字%d" % result)

    result = sess.run(num_float)
    print("float型数字%f" % result)


# 打印变量
var1 = tf.Variable(0.,dtype=tf.float32)
#变量需要初始化
init = tf.initialize_all_variables()
var2 = tf.Variable(0.,dtype=tf.float32)
with tf.Session() as sess:
    #必须先执行变量初始化，不然报错
    sess.run(init)
    result = sess.run(var1)
    print("打印变量原始结果")
    print(result)
    for i in range(5):
        #给变量赋值
        update1 = tf.assign(var1, i+1)
        #需要执行一下更新才能真正实现赋值
        sess.run(update1)
        #获取更新后变量的值
        result = sess.run(var1)
        print("更新变量值%s" % result)

#占位符的使用
#占位符使用run时需要先喂数据，sess.run(feed_dict=)参数指定
x = tf.placeholder(dtype=tf.int32)
var1 = tf.Variable(5,dtype=tf.int32)
init = tf.initialize_all_variables()
with tf.Session() as sess:
    result = sess.run(x,feed_dict={x:[12]})
    print("打印矩阵占位符结果%s" % result)

    print("打印变量中占位符结果")
    sess.run(init)
    # 将变量结果赋值给占位符
    val1 = sess.run(var1)
    #此处常出现的的一个问题是feed_dict 的key不能用"x",而需要用上面定义的变量x，否则会报错
    result = sess.run(x, feed_dict={x: val1})

    # 将占位符结果赋值给变量并打印
    update = tf.assign(var1,result+1)
    sess.run(update)
    val1 = sess.run(var1)
    print("将占位符的结果更新到变量中：%d" % val1)

#############################################################################################################

print("算数运算：")
#字符串运算
con1 = tf.constant("hello")
con2 = tf.constant("world")
add = tf.add(con1,con2)

#int运算
con_int_1 = tf.constant(2)
con_int_2 = tf.constant(4)
add_int = tf.add(con_int_1,con_int_2)
sub_int = tf.subtract(con_int_1,con_int_2)
mul_int = tf.multiply(con_int_1,con_int_2)
div_int = tf.divide(con_int_1,con_int_2)

#float运算
con_float_1 = tf.constant(2.2)
con_float_2 = tf.constant(4.4)
add_float = tf.add(con_float_1,con_float_2)
sub_float = tf.subtract(con_float_1,con_float_2)
mul_float = tf.multiply(con_float_1,con_float_2)
div_float = tf.divide(con_float_1,con_float_2)

#矩阵运算
con_arr_int1 = tf.constant([[1,1],[2,2]])
con_arr_int2 = tf.constant([[3,3],[4,4]])
con_int3 = tf.constant(2)
con_arr_int3 = tf.constant([[3,3],[4,4],[5,5]])
con_arr_int4 = tf.constant([[3,3,3],[4,4,4]])
#矩阵加减乘除
add_arr = tf.add(con_arr_int1,con_arr_int2)
sub_arr = tf.subtract(con_arr_int1,con_arr_int2)
mul_arr = tf.multiply(con_arr_int1,con_arr_int2)
div_arr = tf.divide(con_arr_int1,con_arr_int2)

# 单数*矩阵、矩阵/单数
con_mul_arr = tf.multiply(con_int3,con_arr_int1)
con_div_arr = tf.divide(con_arr_int2,con_int3)

#不同维度m*n矩阵  * n*k的矩阵,第一个矩阵的列数必须等于第二个矩阵的行数
arr_mul_arr = tf.matmul(con_arr_int3,con_arr_int4)

#矩阵转置
arr_trans = tf.transpose(con_arr_int1)

with tf.Session() as sess:
    result = sess.run(add)
    print("str加法结果：%s" % str(result,"utf-8"))

    # int 数学运算
    result = sess.run(add_int)
    print("int加法结果：%d" %result)
    result = sess.run(sub_int)
    print("int减法结果：%d" % result)
    result = sess.run(mul_int)
    print("int乘法结果：%d" % result)
    result = sess.run(div_int)
    print("int除法结果：%d" % result)

    # float数学运算
    result = sess.run(add_float)
    print("float加法结果：%f" % result)
    result = sess.run(sub_float)
    print("float减法结果：%f" % result)
    result = sess.run(mul_float)
    print("float乘法结果：%f" % result)
    result = sess.run(div_float)
    print("float除法结果：%f" % result)

    # 矩阵数学运算
    result = sess.run(add_arr)
    print("arr加法结果：\n%s" % result)
    result = sess.run(sub_arr)
    print("arr减法结果：\n%s" % result)
    result = sess.run(mul_arr)
    print("arr乘法结果：\n%s" % result)
    result = sess.run(div_arr)
    print("arr除法结果：\n%s" % result)

    # 单数 与矩阵相乘/除效果
    result = sess.run(con_mul_arr)
    print("int*arr结果：\n%s" % result)
    result = sess.run(con_div_arr)
    print("arr/int结果：\n%s" % result)

    #2*2的矩阵 * 2*3的矩阵 得到 3*3矩阵
    result = sess.run(arr_mul_arr)
    print("arr*arr结果：\n%s" % result)

    #矩阵转置效果
    result = sess.run(con_arr_int1)
    print("矩阵转置效果前：\n%s" % result)
    result = sess.run(arr_trans)
    print("矩阵转置效果后：\n%s" % result)