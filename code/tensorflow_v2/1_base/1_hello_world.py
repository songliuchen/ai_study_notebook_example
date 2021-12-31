'''
1、tensorflow 常量、变量使用
2、tensorflow 加、减、乘、除、转置数学运算
3、tensorflow multiply 与matmul 区别
notices:
1、tensorflow2中删除了占位符的概念，使用占位符的话，需要通过tf.compat.v1.placeholder切换到1.0版本
2、通过对象numpy()获取结果
'''

# 引入tensorflow，一般给个简称
import tensorflow as tf
import os

#设置日志级别0 全部，1提示，2警告，3错误
os.environ["TF_CPP_MIN_LOG_LEVEL"]='3'

#定义字符串常量
text = tf.constant("hello word")
print("打印原始text对象")
print(text)


# python3.x str变量默认采用unicode类型，需要调用decode()
print(text.numpy().decode())
#可通过tf.print打印结果，但性能不高
tf.print(text)

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

print("算数运算：")
#字符串运算
con1 = tf.constant("hello")
con2 = tf.constant("world")
add = tf.add(con1,con2)
print("str加法结果：%s" % add.numpy().decode())
tf.print("str加法结果2：%s" % add)

# #int运算
# con_int_1 = tf.constant(2)
# con_int_2 = tf.constant(4)
# add_int = tf.add(con_int_1,con_int_2)
# sub_int = tf.subtract(con_int_1,con_int_2)
# mul_int = tf.multiply(con_int_1,con_int_2)
# div_int = tf.divide(con_int_1,con_int_2)
#
# #float运算
# con_float_1 = tf.constant(2.2)
# con_float_2 = tf.constant(4.4)
# add_float = tf.add(con_float_1,con_float_2)
# sub_float = tf.subtract(con_float_1,con_float_2)
# mul_float = tf.multiply(con_float_1,con_float_2)
# div_float = tf.divide(con_float_1,con_float_2)
#
# #矩阵运算
# con_arr_int1 = tf.constant([[1,1],[2,2]])
# con_arr_int2 = tf.constant([[3,3],[4,4]])
# con_int3 = tf.constant(2)
# con_arr_int3 = tf.constant([[3,3],[4,4],[5,5]])
# con_arr_int4 = tf.constant([[3,3,3],[4,4,4]])
# #矩阵加减乘除
# add_arr = tf.add(con_arr_int1,con_arr_int2)
# sub_arr = tf.subtract(con_arr_int1,con_arr_int2)
# mul_arr = tf.matmul(con_arr_int1,con_arr_int2)
# div_arr = tf.divide(con_arr_int1,con_arr_int2)
#
# # 单数*矩阵、矩阵/单数
# con_mul_arr = tf.multiply(con_int3,con_arr_int1)
# con_div_arr = tf.divide(con_arr_int2,con_int3)
#
# #不同维度m*n矩阵  * n*k的矩阵,第一个矩阵的列数必须等于第二个矩阵的行数
# arr_mul_arr = tf.matmul(con_arr_int3,con_arr_int4)
#
# #矩阵转置
# arr_trans = tf.transpose(con_arr_int1)
#
#
# #变量与矩阵运算
# var_arr1 = tf.Variable([[2,2],[3,3]],dtype=tf.int32)
# col_arr1 = tf.constant([[2,2],[3,3]])
# arr_mul_var = tf.matmul(var_arr1,col_arr1)
#
# #变量与变量矩阵运算
# var_var_arr1 = tf.Variable([[2,2],[3,3]],dtype=tf.int32)
# var_var_arr2 = tf.constant([[2,2],[3,3]],dtype=tf.int32)
# var_mul_var = tf.matmul(var_var_arr1,var_var_arr2)
# init = tf.initialize_all_variables()
#
# #占位符与矩阵运算
# pla_pla_arr1 = tf.placeholder(shape=[2,2],dtype=tf.int32)
# pla_pla_arr2 = tf.placeholder(shape=[2,2],dtype=tf.int32)
# pla_mul_pla = tf.matmul(var_var_arr1,var_var_arr2)
# with tf.Session() as sess:
#     sess.run(init)
#     result = sess.run(add)
#     # python3.x str变量默认采用unicode类型，需要调用decode()
#     print("str加法结果：%s" % result.decode())
#
#     # int 数学运算
#     result = sess.run(add_int)
#     print("int加法结果：%d" %result)
#     result = sess.run(sub_int)
#     print("int减法结果：%d" % result)
#     result = sess.run(mul_int)
#     print("int乘法结果：%d" % result)
#     result = sess.run(div_int)
#     print("int除法结果：%d" % result)
#
#     # float数学运算
#     result = sess.run(add_float)
#     print("float加法结果：%f" % result)
#     result = sess.run(sub_float)
#     print("float减法结果：%f" % result)
#     result = sess.run(mul_float)
#     print("float乘法结果：%f" % result)
#     result = sess.run(div_float)
#     print("float除法结果：%f" % result)
#
#     # 矩阵数学运算
#     result = sess.run(add_arr)
#     print("arr加法结果：\n%s" % result)
#     result = sess.run(sub_arr)
#     print("arr减法结果：\n%s" % result)
#     result = sess.run(mul_arr)
#     print("arr乘法结果：\n%s" % result)
#     result = sess.run(div_arr)
#     print("arr除法结果：\n%s" % result)
#
#     # 单数 与矩阵相乘/除效果
#     result = sess.run(con_mul_arr)
#     print("int*arr结果：\n%s" % result)
#     result = sess.run(con_div_arr)
#     print("arr/int结果：\n%s" % result)
#
#     #2*2的矩阵 * 2*3的矩阵 得到 3*3矩阵
#     result = sess.run(arr_mul_arr)
#     print("arr*arr结果：\n%s" % result)
#
#     #矩阵转置效果
#     result = sess.run(con_arr_int1)
#     print("矩阵转置效果前：\n%s" % result)
#     result = sess.run(arr_trans)
#     print("矩阵转置效果后：\n%s" % result)
#
#     # 变量与矩阵运算
#     result = sess.run(arr_mul_var)
#     print("变量*矩阵结果：\n%s" % result)
#     result = sess.run(var_mul_var)
#     print("变量矩阵*变量矩阵：\n%s" % result)
#
#     # 占位符矩阵*占位符矩阵
#     result = sess.run(pla_mul_pla,feed_dict={pla_pla_arr1:[[1,1],[2,2]],pla_pla_arr2:[[3,3],[4,4]]})
#     print("占位符矩阵*占位符矩阵：\n%s" % result)
#
#
# #############################################################################################################
#
# # tf.multiply()与tf.matmul()区别
# # multiply()两个矩阵中对应元素各自相乘，matmul()将矩阵a乘以矩阵b，生成a * b,必须满足矩阵相乘的条件。
# # multiply 支持单数*矩阵，其他要求两个矩阵是同型矩阵
# con_arr_int1 = tf.constant([[1,1],[2,2]])
# con_arr_int2 = tf.constant([[3,3],[4,4]])
# con_arr_multiply = tf.multiply(con_arr_int1,con_arr_int2)
# con_arr_matmul = tf.matmul(con_arr_int1,con_arr_int2)
# with tf.Session() as sess:
#
#     result = sess.run(con_arr_multiply)
#     print("int*arr multiply结果：\n%s" % result)
#
#     result = sess.run(con_arr_matmul)
#     print("int*arr matmul结果：\n%s" % result)
