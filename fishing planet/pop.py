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

move_mouse_flag = True
move_mouse_px = 0

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s')
logger = logging.getLogger(__name__)


def check_big_button():
    # 出现成就框，自动同意
    location_img = pyautogui.locateOnScreen('agree.png')
    if location_img:
        buttonx, buttony = pyautogui.center(location_img)
        pyautogui.click(buttonx, buttony)


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
    move_mouse()
    logger.info('执行自动投杆')
    pyautogui.keyDown('space')
    time.sleep(keep_time)
    pyautogui.keyUp('space')

def move_mouse():
    global move_mouse_flag
    global move_mouse_px

    if move_mouse_flag:
        move_mouse_px = random.randint(100, 200)
        pyautogui.moveRel(move_mouse_px, 0, duration=0.25)
        logger.info(move_mouse_px)
        move_mouse_flag = False
    else:
        pyautogui.moveRel(-move_mouse_px, 0, duration=0.25)
        logger.info(-move_mouse_px)
        move_mouse_flag = True


def shouxian():
    # 收线
    # logger.info('收线ing')
    # pyautogui.keyDown('space')

    pyautogui.keyDown('enter')
    time.sleep(0.02)
    pyautogui.keyDown('space')
    time.sleep(0.25)
    pyautogui.keyUp('enter')
    time.sleep(0.1)
    pyautogui.keyUp('space')
    time.sleep(1.4)




    # # stime = random.uniform(0.04, 0.045)
    # stime = 0.15
    # time.sleep(0.6)
    # pyautogui.keyDown('enter')
    # time.sleep(stime)
    # pyautogui.keyUp('enter')


def check_have_fish():
    # 检测是否上鱼
    have_fish_color_check = pyautogui.pixelMatchesColor(1623, 866, (28, 67, 193), tolerance=30)
    if have_fish_color_check:
        return True
    return False


if __name__ == '__main__':
    # 激活游戏窗口
    pyautogui.moveTo(980, 670)
    pyautogui.click()

    while True:
        # 检查是否该投杆
        if check_zero_length():
            logger.info('线距为0')
            # 检测成就提示窗
            # check_big_button()
            # 投杆
            tougan(1.4)
            # 等待鱼饵落底
            time.sleep(4)

            while True:
                if check_zero_length():
                    pyautogui.keyUp('enter')
                    pyautogui.keyUp('space')
                    logger.info('线距为0')
                    break

                shouxian()

                if check_have_fish():
                    logger.info('上鱼，自动起杆')
                    pyautogui.keyDown('enter')
                    pyautogui.keyDown('space')

                    while True:
                        # 取鱼
                        time.sleep(1)
                        if check_zero_length():
                            logger.info('收线完成，重新投杆')
                            pyautogui.keyUp('enter')
                            pyautogui.keyUp('space')
                            time.sleep(3)
                            break

        else:
            while True:
                if check_zero_length():
                    pyautogui.keyUp('enter')
                    pyautogui.keyUp('space')
                    logger.info('线距为0')
                    break

                shouxian()

                if check_have_fish():
                    logger.info('上鱼，自动起杆')
                    pyautogui.keyDown('enter')
                    pyautogui.keyDown('space')

                    while True:
                        # 取鱼
                        time.sleep(1)

                        if check_zero_length():
                            logger.info('收线完成，重新投杆')

                            pyautogui.keyUp('enter')
                            pyautogui.keyUp('space')
                            time.sleep(3)
                            break