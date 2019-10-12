#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'W.Y.P'
__version__ = '1.0.1'
__email__ = 'wyp@41ms.com'
__date__ = '2019/10/7'

import time
import pygame
import pyautogui


pyautogui.moveTo(980, 670)
pyautogui.click()
# pyautogui.keyDown('t')

location_img = pyautogui.locateOnScreen('continue.png')

print(location_img)