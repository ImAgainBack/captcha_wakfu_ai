import pyautogui
import cv2
import numpy as np
    
def screenshot_cha():
    # Specify the coordinates of the trapezoidal region
    x0, y0 = 1450,400
    x1, y1 = 1750, 550
    x2, y2 = 1030, 920
    x3, y3 = 740, 760

    # Capture the screenshot of the entire screen
    screenshot = pyautogui.screenshot()

    # Convert the screenshot to a NumPy array
    image_np = np.array(screenshot)
    image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    image_bgr= cv2.convertScaleAbs(image_bgr, alpha=1, beta=0)#1.5 -30
    # Create a mask for the trapezoidal region
    mask = np.zeros_like(image_bgr[:, :, 0])
    pts = np.array([[x0, y0], [x1, y1], [x2, y2], [x3, y3]], dtype=np.int32)
    cv2.fillPoly(mask, [pts], color=(255, 255, 255))

    # Apply the mask to the image
    trapezoidal_region = cv2.bitwise_and(image_bgr, image_bgr, mask=mask)

    # Save the trapezoidal region to a file
    cv2.imwrite('wakfu_metier\\img\\trapezoidal_screenshot_cha.png', trapezoidal_region)

def screenshot_carac():
    # Specify the coordinates of the trapezoidal region
    x0, y0 = 0,0
    x1, y1 = 1250, 0
    x2, y2 = 1250, 370
    x3, y3 = 360, 800

    # Capture the screenshot of the entire screen
    screenshot = pyautogui.screenshot()

    # Convert the screenshot to a NumPy array
    image_np = np.array(screenshot)
    image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    # Create a mask for the trapezoidal region
    mask = np.zeros_like(image_bgr[:, :, 0])
    pts = np.array([[x0, y0], [x1, y1], [x2, y2], [x3, y3]], dtype=np.int32)
    cv2.fillPoly(mask, [pts], color=(255, 255, 255))

    # Apply the mask to the image
    trapezoidal_region = cv2.bitwise_and(image_bgr, image_bgr, mask=mask)

    # Save the trapezoidal region to a file
    cv2.imwrite('wakfu_metier\\img\\trapezoidal_screenshot_carac.png', trapezoidal_region)

def simplify_image(input_path, output_path, threshold_value):
    # Read the input image
    image = cv2.imread(input_path)

    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to create a binary image
    _, thresholded_image = cv2.threshold(grayscale_image, threshold_value, 255, cv2.THRESH_BINARY)

    # Save the result
    cv2.imwrite(output_path, thresholded_image)





screenshot_cha()
#screenshot_carac()

# Example usage
input_image_path = "wakfu_metier/img/trapezoidal_screenshot_cha.png"
output_image_path = "wakfu_metier/img/trapezoidal_screenshot_cha.png"
threshold_value = 150  # Adjust this threshold value based on your needs

simplify_image(input_image_path, output_image_path, threshold_value)