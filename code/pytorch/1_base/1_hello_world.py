'''
1、pytorch 常量、变量使用
2、pytorch 加、减、乘、除、转置数学运算
3、pytorch multiply 与 matmul 区别
'''

# 引入torch
import torch
# torch 中 Variable 模块
from torch.autograd import Variable

#定义字符串常量
print("hello world torch %s" % torch.__version__)

# 打印数字
num_int = torch.tensor(100,dtype=torch.int32)
num_float = torch.tensor(1.01,dtype=torch.float32)
print("int型数字%d" % num_int)
print("float型数字%.2f" % num_float)

# 打印变量
tensor = torch.tensor(0.2,dtype=torch.float32)
var1 = Variable(tensor)
print("打印变量结果 %.2f" % var1)
for i in range(5):
    #给变量赋值
    var1 = var1.assign(i+1)
    print("更新变量值%s" % var1.numpy())
#
# print("算数运算：")
# #字符串运算
# con1 = tf.constant("hello")
# con2 = tf.constant("world")
# add = tf.add(con1,con2)
# print("str加法结果：%s" % add.numpy().decode())
#
# # #int运算
# con_int_1 = tf.constant(2)
# con_int_2 = tf.constant(4)
# add_int = tf.add(con_int_1,con_int_2)
# sub_int = tf.subtract(con_int_1,con_int_2)
# mul_int = tf.multiply(con_int_1,con_int_2)
# div_int = tf.divide(con_int_1,con_int_2)
# # 打印int运算结果
# print("int加法结果：%d" % add_int.numpy())
# print("int减法结果：%d" % sub_int.numpy())
# print("int乘法结果：%d" % mul_int.numpy())
# print("int除法结果：%d" % div_int.numpy())
#
# #float运算
# con_float_1 = tf.constant(2.2)
# con_float_2 = tf.constant(4.4)
# add_float = tf.add(con_float_1,con_float_2)
# sub_float = tf.subtract(con_float_1,con_float_2)
# mul_float = tf.multiply(con_float_1,con_float_2)
# div_float = tf.divide(con_float_1,con_float_2)
# # 打印float运算结果
# print("float加法结果：%f" % add_float.numpy())
# print("float减法结果：%f" % sub_float.numpy())
# print("float乘法结果：%f" % mul_float.numpy())
# print("float除法结果：%f" % div_float.numpy())
#
# #矩阵运算
# con_arr_int1 = tf.constant([[1,1],[2,2]])
# con_arr_int2 = tf.constant([[3,3],[4,4]])
# con_int3 = tf.constant(2)
# con_arr_int3 = tf.constant([[3,3],[4,4],[5,5]])
# con_arr_int4 = tf.constant([[3,3,3],[4,4,4]])
# add_arr = tf.add(con_arr_int1,con_arr_int2)
# sub_arr = tf.subtract(con_arr_int1,con_arr_int2)
# mul_arr = tf.matmul(con_arr_int1,con_arr_int2)
# div_arr = tf.divide(con_arr_int1,con_arr_int2)
# # 打印矩阵运算结果
# print("arr加法结果：\n%s" % add_arr.numpy())
# print("arr减法结果：\n%s" % sub_arr.numpy())
# print("arr乘法结果：\n%s" % mul_arr.numpy)
# print("arr除法结果：\n%s" % div_arr.numpy)
#
# # 单数*矩阵、矩阵/单数
# con_mul_arr = tf.multiply(con_int3,con_arr_int1)
# con_div_arr = tf.divide(con_arr_int2,con_int3)
# print("int*arr结果：\n%s" % con_mul_arr.numpy())
# print("arr/int结果：\n%s" % con_div_arr.numpy())
#
# #不同维度m*n矩阵  * n*k的矩阵,第一个矩阵的列数必须等于第二个矩阵的行数
# arr_mul_arr = tf.matmul(con_arr_int3,con_arr_int4)
# print("arr*arr结果：\n%s" % arr_mul_arr.numpy())
#
# #矩阵转置
# arr_trans = tf.transpose(con_arr_int1)
# print("矩阵转置效果前：\n%s" % con_arr_int1.numpy())
# print("矩阵转置效果后：\n%s" % arr_trans.numpy())
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
# print("变量*矩阵结果：\n%s" % arr_mul_var.numpy())
# print("变量矩阵*变量矩阵：\n%s" % var_mul_var.numpy())
#
# # #############################################################################################################
#
# # tf.multiply()与tf.matmul()区别
# # multiply()两个矩阵中对应元素各自相乘，matmul()将矩阵a乘以矩阵b，生成a * b,必须满足矩阵相乘的条件。
# # multiply 支持单数*矩阵，其他要求两个矩阵是同型矩阵
# con_arr_int1 = tf.constant([[1,1],[2,2]])
# con_arr_int2 = tf.constant([[3,3],[4,4]])
# con_arr_multiply = tf.multiply(con_arr_int1,con_arr_int2)
# con_arr_matmul = tf.matmul(con_arr_int1,con_arr_int2)
# print("int*arr multiply结果：\n%s" % con_arr_multiply.numpy())
# print("int*arr matmul结果：\n%s" % con_arr_matmul.numpy())
