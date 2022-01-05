'''
1、pytorch 常量、变量使用
2、pytorch 加、减、乘、除、转置数学运算
3、pytorch * @ mul,mm,matmul 区别
notices:
1、此处的除法，是同元素逐个相除，非真正的矩阵除法
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
tensor = torch.tensor(0,dtype=torch.int)
var1 = Variable(tensor)
print("打印变量结果 %d" % var1)
for i in range(5):
    #给变量赋值
    tensor += 1
    print("更新变量值%d" % var1)

print("算数运算：")
# #int运算
con_int_1 = torch.tensor(2)
con_int_2 = torch.tensor(4)
add_int = con_int_1+con_int_2
sub_int = con_int_1 - con_int_2
mul_int = con_int_1*con_int_2
div_int = con_int_1/con_int_2
# 打印int运算结果
print("int加法结果：%d" % add_int)
print("int减法结果：%d" % sub_int)
print("int乘法结果：%d" % mul_int)
print("int除法结果：%d" % div_int)

#float运算
con_float_1 = torch.tensor(2.2)
con_float_2 = torch.tensor(4.4)
add_float = con_float_1+con_float_2
sub_float = con_float_1 - con_float_2
mul_float = con_float_1 * con_float_2
div_float = con_float_1 / con_float_2
# 打印float运算结果
print("float加法结果：%.2f" % add_float)
print("float减法结果：%.2f" % sub_float)
print("float乘法结果：%.2f" % mul_float)
print("float除法结果：%.2f" % div_float)

# #矩阵运算
con_arr_int1 = torch.tensor([[1,1],[2,2]])
con_arr_int2 = torch.tensor([[3,3],[4,4]])
con_int3 = torch.tensor(2)
con_arr_int3 = torch.tensor([[3,3],[4,4],[5,5]])
con_arr_int4 = torch.tensor([[3,3,3],[4,4,4]])
add_arr = con_arr_int1 + con_arr_int2
sub_arr = con_arr_int1 - con_arr_int2
#矩阵乘法不能用* ，要用@符号
mul_arr = con_arr_int1 @ con_arr_int2
div_arr = con_arr_int1 / con_arr_int2
div_arr2 = torch.div(con_arr_int1, con_arr_int2)
div_arr3 = torch.divide(con_arr_int1, con_arr_int2)
# 打印矩阵运算结果
print("arr加法结果：\n%s" % add_arr)
print("arr减法结果：\n%s" % sub_arr)
print("arr乘法结果：\n%s" % mul_arr)

print("arr除法结果：\n%s" % div_arr)
print("arr除法结果2：\n%s" % div_arr2)
print("arr除法结果3：\n%s" % div_arr3)

# 单数*矩阵、矩阵/单数
con_mul_arr = con_int3 * con_arr_int1
con_div_arr = con_arr_int2 /con_int3
print("int*arr结果：\n%s" % con_mul_arr)
print("arr/int结果：\n%s" % con_div_arr)

# 不同维度m*n矩阵  *  n*k的矩阵,第一个矩阵的列数必须等于第二个矩阵的行数
# pytorch 不同维度矩阵不能直接用 * 相乘
# pytorch 支持mm、matmul两种举证相乘方法，正常使用torch.mm即可
arr_mul_arr = torch.mm(con_arr_int3,con_arr_int4)
arr_mul_arr2 = torch.matmul(con_arr_int3,con_arr_int4)
print("arr*arr结果1：\n%s" % arr_mul_arr)
print("arr*arr结果2：\n%s" % arr_mul_arr2)

# #矩阵转置
arr_trans = con_arr_int1.T
print("矩阵转置效果前：\n%s" % con_arr_int1)
print("矩阵转置效果后：\n%s" % arr_trans)


#变量与矩阵运算
tensor = torch.tensor([[2,2],[3,3]])
var_arr1 = Variable(tensor)
col_arr1 = torch.tensor([[2,2],[3,3]])
arr_mul_var =var_arr1 *col_arr1

# #变量与变量矩阵运算
var_var_arr1 = Variable(tensor)
var_var_arr2 = torch.tensor([[2,2],[3,3]])
var_mul_var = var_var_arr1 * var_var_arr2
print("变量*矩阵结果：\n%s" % arr_mul_var)
print("变量矩阵*变量矩阵：\n%s" % var_mul_var)


# #############################################################################################################
# pytorch 矩阵相乘 与 矩阵逐个元素相乘
# *，torch.mul两个矩阵中对应元素各自相乘,支持单数*矩阵，其他要求矩阵必须是同型矩阵
# @,mm,matmul将矩阵a乘以矩阵b，生成a * b,必须满足矩阵相乘的条件。其中mm只能计算二维矩阵相乘
con_arr_int1 = torch.tensor([[1,1],[2,2]])
con_arr_int2 = torch.tensor([[3,3],[4,4]])
arr_arr_int_ = con_arr_int1 @ con_arr_int2
arr_arr_int = con_arr_int1*con_arr_int2

con_arr_mul = torch.mul(con_arr_int1,con_arr_int2)
con_arr_matmul = torch.matmul(con_arr_int1,con_arr_int2)
con_arr_mm = torch.mm(con_arr_int1,con_arr_int2)
print("矩阵逐元素相乘：")
print("arr*arr 结果：\n%s" % arr_arr_int)
print("arr*arr mul结果：\n%s" % con_arr_mul)

print("矩阵相乘：")
print("arr*arr @结果：\n%s" % arr_arr_int_)
print("arr*arr matmul结果：\n%s" % con_arr_matmul)
print("arr*arr mm结果：\n%s" % con_arr_mm)
