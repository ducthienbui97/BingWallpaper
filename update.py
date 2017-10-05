# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 17:40:10 2017

@author: thienbui
"""

from urllib import request
import json
import ctypes
import os
data = request.urlopen("https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US").read().decode('utf8')
save_location = os.path.join(os.path.dirname(os.path.abspath(__file__)),"wallpaper.jpg")
request.urlretrieve("https://www.bing.com" + json.loads(data)['images'][0]['url'], save_location)
ctypes.windll.user32.SystemParametersInfoW(20, 0, save_location, 3)
