#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/5 7:37 下午
# @Author  : song
# @Email   : song_gis@163.com  
# @gitee    : gitee.com/songliuchen
# @File    : gen_linear_data.py.py

import torch
from file_utils import read_file
def gen_linear():
    """
    生成简单线性回归样本数据
    @return:
    """
    x =  torch.rand(1000)
    y = 2.8366*x+0.1245
    arr_x = x.data
    arr_y = y.data

    with open("../../data/simple_linear_data_dev.txt", mode="a+", encoding='utf-8') as f:
        for i in range(len(arr_x)):
            f.write("%f,%f\n" % (arr_x[i],arr_y[i]))
        f.flush()

if __name__ == '__main__':
    gen_linear()