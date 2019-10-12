#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'W.Y.P'
__version__ = '1.0.1'
__email__ = 'wyp@41ms.com'
__date__ = '2019/10/7'

import time
import pyautogui
import logging
import random
import time
import keyboard
import pygame

then = 0
now = 0
switch_flag = False
yupiao_pix = pyautogui.pixel(1762, 347)

logging.basicConfig(level=logging.INFO, filename="test.log", filemode="w", format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s')
logger = logging.getLogger(__name__)


def check_fishfort_status():
    color_check = pyautogui.pixelMatchesColor(91, 251, (250, 195, 0), tolerance=10)
    if color_check:
        pyautogui.keyDown('t')
        # location_img = pyautogui.locateOnScreen('continue.png')



        exit()
        # logger.info('鱼库满了')
        # file = '七里香.mp3'
        # pygame.mixer.init()
        # track = pygame.mixer.music.load(file)
        # pygame.mixer.music.play()
        # time.sleep(296)
        # pygame.mixer.music.stop()



        return True

    return False

def get_keybord_status():
    global switch_flag
    if keyboard.is_pressed('f9'):
        switch_flag = True
    if keyboard.is_pressed('f12'):
        switch_flag = False
    return switch_flag


def check_zero_length():
    # 钓线显示为0米时，自动投杆
    zero_color_check1 = pyautogui.pixelMatchesColor(1545, 1039, (247, 247, 247), tolerance=2)
    zero_color_check2 = pyautogui.pixelMatchesColor(1561, 1008, (247, 247, 247), tolerance=2)
    zero_color_check3 = pyautogui.pixelMatchesColor(1561, 1068, (247, 247, 247), tolerance=2)
    zero_color_check4 = pyautogui.pixelMatchesColor(1580, 1037, (247, 247, 247), tolerance=2)
    zero_color_check5 = pyautogui.pixelMatchesColor(1544, 1050, (247, 247, 247), tolerance=2)
    if zero_color_check1 and zero_color_check2 and zero_color_check3 and zero_color_check4 and zero_color_check5:
        return True
    return False


def tougan(keep_time=1.8):
    # 投杆
    logger.info('执行自动投杆')
    pyautogui.keyDown('space')
    time.sleep(keep_time)
    pyautogui.keyUp('space')


def shouxian():
    # 收线
    logger.info('收线ing')
    stime = random.uniform(0.6, 0.8)
    time.sleep(stime)
    pyautogui.keyDown('enter')
    pyautogui.press('space')


def init_yupiao():
    global yupiao_pix
    yupiao_pix = pyautogui.pixel(1762, 347)


def check_have_fish():
    # 检测是否上鱼
    global yupiao_pix

    # now_yupiao_pix = pyautogui.pixel(1762, 347)
    have_fish_color_check2 = pyautogui.pixelMatchesColor(1762, 347, yupiao_pix, tolerance=30)
    if have_fish_color_check2:
        logger.info('鱼漂动了')
        return True

    have_fish_color_check1 = pyautogui.pixelMatchesColor(1623, 866, (28, 67, 193), tolerance=30)
    if have_fish_color_check1:
        # logger.info(now_yupiao_pix)
        logger.info(yupiao_pix)
        logger.info('能量条变蓝了')
        return True

    return False


if __name__ == '__main__':
    # 激活游戏窗口
    pyautogui.moveTo(980, 670)
    pyautogui.click()

    while True:

        if check_fishfort_status():
            time.sleep(1)
            continue

        # 检查是否该投杆
        if check_zero_length():
            logger.info('线距为0')

            # 投杆
            init_yupiao()
            # tougan(1.7)
            tougan(0.1)
            then = time.time()
            # # 等待鱼饵落底
            time.sleep(5)

            while True:
                if check_zero_length():
                    logger.info('线距为0')
                    break

                # shouxian()
                time.sleep(0.01)

                now = time.time()
                diff = int(now - then) // 60

                if check_have_fish() or (diff > 10):
                    logger.info('上鱼了或者到5分钟了，自动起杆')

                    time.sleep(0.3)
                    pyautogui.keyDown('enter')
                    time.sleep(0.5)
                    pyautogui.keyDown('space')

                    while True:
                        # 取鱼
                        time.sleep(1)
                        # location_img = pyautogui.locateOnScreen('qu.png')
                        #
                        # if location_img:
                        #     logger.info('收线完成，弹出取鱼弹窗')
                        #     pyautogui.keyUp('enter')
                        #     pyautogui.keyUp('space')
                        #     time.sleep(3)
                        #     break
                        if check_zero_length():
                            logger.info('收线完成，重新投杆')
                            pyautogui.keyUp('enter')
                            pyautogui.keyUp('space')
                            time.sleep(5)
                            break