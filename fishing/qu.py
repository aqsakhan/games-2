#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'W.Y.P'
__version__ = '1.0.1'
__email__ = 'wyp@41ms.com'
__date__ = '2019/10/7'


import time
import pyautogui
import logging
logging.basicConfig(level=logging.INFO)


pyautogui.moveTo(980, 670)
pyautogui.click(button='left')

location_img = pyautogui.locateOnScreen('qu.png')

if location_img:
    logging.info('上鱼成功，自动入库')
    pyautogui.keyDown('ctrl')
    buttonx, buttony = pyautogui.center(location_img)
    pyautogui.moveTo(buttonx, buttony, 1)
    pyautogui.click()
    time.sleep(5)
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('enter')
    pyautogui.keyUp('space')