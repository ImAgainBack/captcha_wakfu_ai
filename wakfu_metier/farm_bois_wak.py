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
#----------------------INITIALISATION----------------------#



def farm_ressource(ressource,action,action_collect):

    try:
        regions=(800,500,300,300)#watch if there are ressources nearby
        boolee=detect_image(ressource,regions)
        regions2=(700,400,500,500)#watch if there are ressources a bit far
        boolee2=detect_image(ressource,regions2)
        boolee3=detect_image(ressource,regions=None)#if the ressources are on screen
        
        if boolee==True:
            collect_ressource(ressource,action,action_collect,regions)
            print("close")
        elif boolee2==True:
            collect_ressource(ressource,action,action_collect,regions2)
            print("middle")
        elif boolee3==True:
            collect_ressource(ressource,action,action_collect,regions=None)
            print("far")
    except:
        pass 

def collect_ressource(ressource,action,action_collect,regions):
    
    boolee= detect_image(ressource,regions)
    coords_x, coords_y = pg.locateCenterOnScreen(ressource, confidence=0.6,region=regions)
    
    if boolee==True:
        p = random.uniform(0.3, 0.6)
        hc = HumanClicker()
        hc.move((coords_x, coords_y), p)
        pg.rightClick()
        time.sleep(1.5)
        boolee= detect_image(action_collect,regions)#couper, recup graines etc
        boolee2 = detect_image(action,regions)#couper, recup graines etc
        print(boolee,"",boolee2)
        if boolee ==True:
            coords_x, coords_y=pg.locateCenterOnScreen(action, confidence=0.9,region=regions)
            hc.move((coords_x, coords_y), p)
            pg.leftClick()
            time.sleep(2.5)
            boolee =detect_image("wakfu_metier/img/pour_prog/actions_bot/wakfu_w8ing.png",regions)
            while (boolee ==True):
                print("Waiting for")
                time.sleep(2)
        
        elif boolee2 ==True:
            coords_x, coords_y=pg.locateCenterOnScreen(action_collect, confidence=0.9,region=regions)
            hc.move((coords_x, coords_y), p)
            pg.leftClick()
            time.sleep(2)
            boolee =detect_image("wakfu_metier/img/pour_prog/actions_bot/wakfu_w8ing.png",regions)
            while (boolee ==True):
                print("Waiting for")
                time.sleep(.5)
        else:
            pass




def detect_image(image_path,regions):
    try:
        location=pg.locateOnScreen(image_path, confidence=0.9,region=regions)
        if location is not None:
            return True
        else:
            return False
    except:
        return False
    

boolee=detect_image("wakfu_metier/img/pour_prog/captcha_detect.png", (1866,80,50,50))
print(boolee)
