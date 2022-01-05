'''
1、tensorflow 常量、变量使用
2、tensorflow 加、减、乘、除、转置数学运算
3、tensorflow multiply 与 matmul 区别
notices:
1、tensorflow2中删除了占位符的概念，使用占位符的话，需要通过tf.compat.v1.placeholder切换到1.0版本
2、此处的除法，是同元素逐个相除，非真正的矩阵除法
3、tensorflow2 加减乘除支持 直接用数学符号运算，例如 + - * /
'''

# 引入tensorflow，一般给个简称
import tensorflow as tf
import os

#设置日志级别0 全部，1提示，2警告，3错误
os.environ["TF_CPP_MIN_LOG_LEVEL"]='3'

#定义字符串常量
text = tf.constant("hello word")
print("tensorflow版本 %s" % tf.__version__)
print("打印原始text对象")
print(text)


# python3.x str变量默认采用unicode类型，需要调用decode()
print(text.numpy().decode())
#可通过tf.print打印结果，但性能不高
# tf.print(text)

# 打印数字
num_int = tf.constant(100,dtype=tf.int32)
num_float = tf.constant(1.01,dtype=tf.float32)
print("int型数字%d" % num_int)
print("float型数字%.2f" % num_float)

# 打印变量
var1 = tf.Variable(99,dtype=tf.int32)
print("打印变量结果 %d" % var1)
for i in range(5):
    #给变量赋值
    var1.assign(i+1)
    print("更新变量值 %d" % var1)

print("算数运算：")
#字符串运算
con1 = tf.constant("hello")
con2 = tf.constant("world")
add = tf.add(con1,con2)
print("str加法结果：%s" % add)

# #int运算
con_int_1 = tf.constant(2)
con_int_2 = tf.constant(4)
add_int = con_int_1+ con_int_2
add_int2 = tf.add(con_int_1,con_int_2)
sub_int = tf.subtract(con_int_1,con_int_2)
mul_int = tf.multiply(con_int_1,con_int_2)
div_int = tf.divide(con_int_1,con_int_2)
# 打印int运算结果
print("int加法结果：%d" % add_int)
print("int加法结果2：%d" % add_int2)
print("int减法结果：%d" % sub_int)
print("int乘法结果：%d" % mul_int)
print("int除法结果：%d" % div_int)

#float运算
con_float_1 = tf.constant(2.2)
con_float_2 = tf.constant(4.4)
add_float = tf.add(con_float_1,con_float_2)
sub_float = tf.subtract(con_float_1,con_float_2)
mul_float = tf.multiply(con_float_1,con_float_2)
div_float = tf.divide(con_float_1,con_float_2)
# 打印float运算结果
print("float加法结果：%f" % add_float)
print("float减法结果：%f" % sub_float)
print("float乘法结果：%f" % mul_float)
print("float除法结果：%f" % div_float)

#矩阵运算
con_arr_int1 = tf.constant([[1,1],[2,2]])
con_arr_int2 = tf.constant([[3,3],[4,4]])
con_int3 = tf.constant(2)
con_arr_int3 = tf.constant([[3,3],[4,4],[5,5]])
con_arr_int4 = tf.constant([[3,3,3],[4,4,4]])
add_arr = tf.add(con_arr_int1,con_arr_int2)
sub_arr = tf.subtract(con_arr_int1,con_arr_int2)
mul_arr = con_arr_int1 * con_arr_int2
mul_arr2 = tf.matmul(con_arr_int1,con_arr_int2)
div_arr = tf.divide(con_arr_int1,con_arr_int2)
# 打印矩阵运算结果
print("arr加法结果：\n%s" % add_arr.numpy())
print("arr减法结果：\n%s" % sub_arr.numpy())
print("arr乘法结果：\n%s" % mul_arr.numpy())
print("arr乘法结果2：\n%s" % mul_arr2.numpy())
print("arr除法结果：\n%s" % div_arr.numpy())

# 单数*矩阵、矩阵/单数
con_mul_arr = tf.multiply(con_int3,con_arr_int1)
con_div_arr = tf.divide(con_arr_int2,con_int3)
print("int*arr结果：\n%s" % con_mul_arr.numpy())
print("arr/int结果：\n%s" % con_div_arr.numpy())

#不同维度m*n矩阵  * n*k的矩阵,第一个矩阵的列数必须等于第二个矩阵的行数
arr_mul_arr = tf.matmul(con_arr_int3,con_arr_int4)
print("arr*arr结果：\n%s" % arr_mul_arr.numpy())

#矩阵转置
arr_trans = tf.transpose(con_arr_int1)
print("矩阵转置效果前：\n%s" % con_arr_int1.numpy())
print("矩阵转置效果后：\n%s" % arr_trans.numpy())


#变量与矩阵运算
var_arr1 = tf.Variable([[2,2],[3,3]],dtype=tf.int32)
col_arr1 = tf.constant([[2,2],[3,3]])
arr_mul_var = tf.matmul(var_arr1,col_arr1)

#变量与变量矩阵运算
var_var_arr1 = tf.Variable([[2,2],[3,3]],dtype=tf.int32)
var_var_arr2 = tf.constant([[2,2],[3,3]],dtype=tf.int32)
var_mul_var = tf.matmul(var_var_arr1,var_var_arr2)
print("变量*矩阵结果：\n%s" % arr_mul_var.numpy())
print("变量矩阵*变量矩阵：\n%s" % var_mul_var.numpy())

# #############################################################################################################

# tf.multiply()与tf.matmul()区别
# *,multiply()两个矩阵中对应元素各自相乘，matmul()将矩阵a乘以矩阵b，生成a * b,必须满足矩阵相乘的条件。
# multiply 支持单数*矩阵，其他要求两个矩阵是同型矩阵
con_arr_int1 = tf.constant([[1,1],[2,2]])
con_arr_int2 = tf.constant([[3,3],[4,4]])
con_arr_ = con_arr_int1 *con_arr_int2
con_arr_multiply = tf.multiply(con_arr_int1,con_arr_int2)
con_arr_matmul = tf.matmul(con_arr_int1,con_arr_int2)
print("int*arr *结果：\n%s" % con_arr_.numpy())
print("int*arr multiply结果：\n%s" % con_arr_multiply.numpy())
print("int*arr matmul结果：\n%s" % con_arr_matmul.numpy())
