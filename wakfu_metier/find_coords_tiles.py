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
from screenshot_captcha import screenshot_cha,screenshot_carac
import pyautogui as pg
import time
import cv2
import numpy as np
from pyclick import HumanClicker
import concurrent.futures

# ----------------------INITIALISATION----------------------#
    # Function to simplify the image
def simplify_image(input_path, output_path, threshold_value):
    image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    _, thresholded = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
    cv2.imwrite(output_path, cv2.cvtColor(thresholded, cv2.COLOR_GRAY2BGR))

def find_img(path):
    # List of image paths
    image_paths = ["wakfu_metier/img/1.png", "wakfu_metier/img/2.png", "wakfu_metier/img/3.png", "wakfu_metier/img/4.png",
                "wakfu_metier/img/5.png", "wakfu_metier/img/6.png", "wakfu_metier/img/7.png", "wakfu_metier/img/8.png"]

    # Load template images outside the loop
    template_images = [cv2.imread(image_path) for image_path in image_paths]

    # Initialize a list to store the counts
    pic_counts = [0] * len(image_paths)

    # Number of iterations
    num_iterations = 50

    # Function to match template
    def match_template(args):
        template, screenshot_remember = args
        result = cv2.matchTemplate(screenshot_remember, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)
        return max_val

    # Loop over the images
    for i in range(num_iterations):
        screenshot_cha()
        screenshot_carac()
        #input_image_path = "wakfu_metier/img/trapezoidal_screenshot_cha.png"
        #output_image_path = "wakfu_metier/img/trapezoidal_screenshot_cha.png"
        threshold_value = 150  # Adjust this threshold value based on your needs
        simplify_image(path, path, threshold_value)

        screenshot_remember = cv2.imread(path)
        cv2.imwrite(f'wakfu_metier\\img\\test_cha\\{i+217}.png', screenshot_remember)
        # Match templates using parallel processing
        with concurrent.futures.ThreadPoolExecutor() as executor:
            scores = list(executor.map(match_template, zip(template_images, [screenshot_remember] * len(template_images))))

        # Update counts based on match scores
        threshold = 0.5
        for idx, score in enumerate(scores):
            if score >= threshold:
                pic_counts[idx] += 1

    # Print the results
    for idx, count in enumerate(pic_counts):
        print(f"pic{idx + 1}: {count}")

path = "wakfu_metier/img/trapezoidal_screenshot_cha.png"
find_img(path)