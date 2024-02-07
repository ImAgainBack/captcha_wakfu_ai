#----------------------INITIALISATION----------------------#
import pyautogui as pg
#include functions.py
import time 
import random
import win32api, win32con
import keyboard
import cv2
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
from pyclick import HumanClicker
hc = HumanClicker()
import numpy as np
from matplotlib.image import imread
import mss.tools
import numpy as np
import cv2
import pyautogui
import time
from captcha_ai import docker_call_cha, docker_call_carac,move_hc,compute_coords_hc
from farm_bois_wak import farm_ressource,detect_image
from screenshot_captcha import screenshot_cha, screenshot_carac, simplify_image
#----------------------INITIALISATION----------------------#

while not keyboard.is_pressed('q')==True:
    try:
        path="wakfu_metier/img/pour_prog/captcha_detect.png"
        boolee= detect_image(path,(1866,80,50,50))
        #detect_image(path,(1866,80,50,50))


        if (boolee == False):
            farm_ressource("wakfu_metier/img/pour_prog/paysant/cactousse.png","wakfu_metier/img/pour_prog/actions_bot/recup_paysant_graine.png","wakfu_metier/img/pour_prog/actions_bot/cutters.png")
        else:
            #time.sleep(1)
            screenshot_cha()
            screenshot_carac()
            path_cha = "wakfu_metier/img/trapezoidal_screenshot_cha.png"
            path_carac= "wakfu_metier/img/trapezoidal_screenshot_carac.png"
            threshold_value = 150
            simplify_image(path_cha,path_cha,threshold_value)
            simplify_image(path_carac,path_carac,threshold_value)
            ai_captcha_cha= docker_call_cha(path_cha)
            #print(ai_captcha_cha)
            ai_captcha_carac = docker_call_carac(path_carac)
            #print("----------------------------------------------------")
            #print(ai_captcha_carac)   
            coords_hc=compute_coords_hc(ai_captcha_carac)
            print(coords_hc)   

            move_hc(coords_hc,ai_captcha_cha)
    except:
        #keyboard.press("del")
        #keyboard.release("del")
        time.sleep(.5)
        keyboard.press("enter")
        keyboard.release("enter")
        print("error")
        time.sleep(1)