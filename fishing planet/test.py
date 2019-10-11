#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'W.Y.P'
__version__ = '1.0.1'
__email__ = 'wyp@41ms.com'
__date__ = '2019/10/7'


import pymouse,pykeyboard,os,sys
from pymouse import *
from pykeyboard import PyKeyboard
import pyautogui
m = PyMouse()
# k = PyKeyboard()
#
# m.click(1111, 996)
# m.click(1111, 996)
pyautogui.moveTo(980, 670)
pyautogui.click()
pyautogui.moveRel(100, 0, duration=0.25)
pyautogui.moveRel(100, 0, duration=0.25)
pyautogui.moveRel(100, 0, duration=0.25)
pyautogui.moveRel(100, 0, duration=0.25)
pyautogui.moveRel(100, 0, duration=0.25)
pyautogui.moveTo(500, 500, duration=0.1)
m.move(200, 200)