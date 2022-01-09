#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/5 7:37 下午
# @Author  : song
# @Email   : song_gis@163.com  
# @gitee    : gitee.com/songliuchen
# @File    : image_utils.py

from PIL import Image
def resize_image():
    """
    resize图片大小
    @return:
    """
    pic = Image.open("../../../resources/images/simple_linear_graph.png")
    # pic = pic.resize((int(pic.size[0]/2), int(pic.size[1]/2)))
    pic = pic.resize((320, 240))
    pic.save("../../../resources/images/simple_linear_graph.png")

if __name__ == '__main__':
    resize_image()