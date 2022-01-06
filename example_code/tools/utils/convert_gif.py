#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/4 5:49 下午
# @Author  : song
# @Email   : song_gis@163.com  
# @gitee    : gitee.com/songliuchen
# @File    : convert.py.py

from moviepy.editor import *
clipVideo = VideoFileClip("translation.mov").set_fps(2).resize(0.3)
newclip = clipVideo.fl_time(lambda t:  3*t , apply_to=['mask'],keep_duration=True)
print(newclip.duration)
newclip.write_gif("movie.gif")