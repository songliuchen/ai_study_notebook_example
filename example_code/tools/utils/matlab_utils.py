#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/7 11:50 上午
# @Author  : song
# @Email   : song_gis@163.com  
# @gitee    : gitee.com/songliuchen
# @File    : matlab_utils.py.py
import matplotlib.pyplot as plt
def draw_line(data:list,config:dict):
    """
    @param:data 数据列表
    绘制折线图 data结构[{x:[],y:[],name:"",color:""}]
    """
    for item in data:
        plt.plot(item["x"], item["y"],label = item["name"],c=item["color"])

    plt.xlabel(config["x_name"])
    plt.ylabel(config["y_name"])
    plt.title(config["title"])

    plt.legend()
    plt.show()


def draw(data:list,config:dict):
    """
    @param:data 数据列表
    @draw_line:是否绘制线
    绘制散点图 data结构[{x:[],y:[],name:"",color:"",type:"point、line"}]
    """
    # 散点图
    for item in data:
        if item["type"] == "line":
            plt.plot(item["x"], item["y"],label = item["name"],c=item["color"])
        elif item["type"] == "point":
            plt.scatter(item["x"], item["y"], s=10, c=item["color"], marker=".", alpha=1,label = item["name"])

    plt.xlabel(config["x_name"])
    plt.ylabel(config["y_name"])
    plt.title(config["title"])

    plt.legend()
    plt.show()