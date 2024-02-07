ROBOFLOW_API_KEY="OZl3KsB8q1q0v6L5PIqi"

import inference#?
import roboflow
import random
from pyclick import HumanClicker
hc = HumanClicker()
import keyboard
import pyautogui as pg
import time


""" def ai_captcha(pic_analyse_ai):
    rf = roboflow.Roboflow(api_key=ROBOFLOW_API_KEY)

    project = rf.workspace().project("wakfu_captcha")
    model = project.version("3").model

    # optionally, change the confidence and overlap thresholds
    # values are percentages
    model.confidence = 50
    model.overlap = 25

    # predict on a local image
    data = model.predict(pic_analyse_ai)
    print(data)
    middle_coordinates_numbers = []
    for entry in data:
        #for caracter coordinates x and y and each number associated with
        middle_x = entry["width"] / 2 + entry["x"]
        middle_y = entry["height"] / 2 + entry["y"]
        number= entry["class"]
        middle_coordinates_numbers.append({"Middle_X": middle_x, "Middle_Y": middle_y,"class":number})

    return middle_coordinates_numbers
 """

""" def ai_captcha(pic_analyse_ai):
    rf = roboflow.Roboflow(api_key=ROBOFLOW_API_KEY)

    project = rf.workspace().project("wakfu_captcha")
    model = project.version("3").model

    # optionally, change the confidence and overlap thresholds
    # values are percentages
    model.confidence = 50
    model.overlap = 25

    # predict on a local image
    data = model.predict(pic_analyse_ai)
    # Filter out duplicate classes and keep only the one with the highest confidence
    class_confidences = {}
    
    for entry in data:
        class_label = entry["class"]
        confidence = entry["confidence"]

        if class_label not in class_confidences or confidence > class_confidences[class_label]["confidence"]:
            class_confidences[class_label] = {"confidence": confidence, "entry": entry}

    # Retrieve the filtered entries with the highest confidence for each class
    filtered_data = [value["entry"] for value in class_confidences.values()]

    middle_coordinates_numbers = []
    for entry in filtered_data:
        # For character coordinates x and y and each number associated with
        middle_x = entry["width"] / 2 + entry["x"]
        middle_y = entry["height"] / 2 + entry["y"]
        number = entry["class"]
        middle_coordinates_numbers.append({"Middle_X": middle_x, "Middle_Y": middle_y, "class": number})
    return middle_coordinates_numbers

import inference
model = inference.load_roboflow_model("wakfu_captcha/3")
a=model.infer(image="wakfu_metier/img/trapezoidal_screenshot_cha.png")
print(a) """

from inference_sdk import InferenceHTTPClient

"""in this code, we will have 2 things to do, collect data about bottom part
being so called "cha" for captcha, and for the player one, being called
"carac" for caracter. So for cha we will need to know which cells to press
when you are on the player side.
"""

path_cha = "wakfu_metier/img/trapezoidal_screenshot_cha.png"
path_carac= "wakfu_metier/img/trapezoidal_screenshot_carac.png"

#prog about docker call run locally
def docker_call_carac(url_img): 

  # Replace ROBOFLOW_API_KEY with your Roboflow API Key
  client = InferenceHTTPClient(
      api_url="http://localhost:9001", # or https://detect.roboflow.com for Hosted API
      api_key="OZl3KsB8q1q0v6L5PIqi"
  )
  with client.use_model("wakfu_captcha/3"):#model ai trained on
      data = client.infer(url_img)

  #print(data)

  best_predictions = {}

  # Iterate through predictions and update the best ones
  for prediction in data['predictions']:
      class_id = prediction['class_id']
      current_confidence = prediction['confidence']

      if class_id not in best_predictions or current_confidence > best_predictions[class_id]['confidence']:
          #getting rid of bad and low confidence values, keeping the best
          #or the unique
          best_predictions[class_id] = prediction

  # Convert the dictionary values back to a list
  best_predictions_list = list(best_predictions.values())
  lists=[]
  # Print or use the best predictions as needed
  for prediction in best_predictions_list:
    lists.append(prediction)
  return lists#returning best_predictions list, for this project at most 8 inputs

def docker_call_cha(url_img):
   data=docker_call_carac(url_img)#same as before
   sorted_predictions = sorted(data, key=lambda x: x['confidence'], reverse=True)

   # Select the top 3 predictions because we only have 3 cells
   top3_predictions = sorted_predictions[:3]
   unique_classes = []

   for prediction in top3_predictions:
        unique_classes.append(prediction['class'])
   return unique_classes

#we compute the coordinates to click on cells 
def compute_coords_hc(list_coords):
    listed ={}
    listed_list=[] 

    for coord in list_coords:
        listed={
            'x':int(coord["x"]),#'x':int(coord["x"]+coord["width"]/2),
            'y':int(coord["y"]),#'y':int(coord["y"]+coord["height"]/2),
            'class': coord["class"]}#remember to which number each coord is
        #listed.append(coord["y"]+coord["height"]/2)
        listed_list.append(listed)
    return listed_list

#ai_captcha_cha= docker_call_cha(path_cha)
#ai_captcha_carac = docker_call_carac(path_carac)
#liste_hc=compute_coords_hc(ai_captcha_carac)
#print(compute_coords_hc(ai_captcha_carac))
#print(liste_hc)
#print(liste_hc)

def average_in_time(repetitions,url_img):
    stock=[]
    if url_img == "wakfu_metier/img/trapezoidal_screenshot_cha.png":
        for i in range(repetitions):

            list_cha=docker_call_cha(url_img)
            for list_1d in list_cha:
                stock.append(list_1d['class']) 
            time.sleep(0.3)     

        print(stock,'----------------liste 1d cha-----------------\n')      
        
    elif url_img == "wakfu_metier/img/trapezoidal_screenshot_carac.png":
        for i in range(repetitions):
            list_carac=docker_call_carac(url_img)
            #print(type(list_carac))

            #print(list_carac)
            for list_1d in list_carac:
                stock.append(list_1d['class']) 
            time.sleep(0.3)     
 
        print(stock,'----------------liste 1d carac-----------------\n') 
    else:
        return "Error"

average_in_time(10,'wakfu_metier/img/trapezoidal_screenshot_carac.png')





def move_hc(liste_hc,ai_captcha_cha):#simple goto prog
    ffs=[]
    for item in liste_hc: 
        #liste_hc containing all numbers from 1 to 8 with each coord
        
        if item['class'] in ai_captcha_cha:
            #here we keep only the numbers in cha part
            x_coordinate = item['x']
            y_coordinate = item['y']
            #print(type(x_coordinate))
            ffs.append([x_coordinate, y_coordinate])


    #coord_list=list(coordinate_dict)
    #print(ffs)
    # Collect x and y coordinates corresponding to class_list

    p = random.uniform(0.3, 0.8) #generate random value to not get caught
    hc = HumanClicker()#humanlike moving mouse

    for i in range(len(ffs)):
        
        #print(ffs[i][0])
        hc.move((ffs[i][0],ffs[i][1]), p*0.9) 
        keyboard.press("1")
        keyboard.release("1")
        pg.leftClick()
        time.sleep(1)










#base64 wakfu_metier/img/trapezoidal_screenshot_cha.png | curl -d @- "http://localhost:9001/wakfu_captcha/3?api_key=OZl3fsf8q1qfvfL5PIqi"
#base64 wakfu_metier/img/trapezoidal_screenshot_carac.png | curl -d @- "http://localhost:9001/wakfu_captcha/3?api_key=OZl3KsB8q1q0v6L5PIqi"


# Predict on a hosted image via file name
#prediction = model.predict("YOUR_IMAGE.jpg", hosted=True)

# Predict on a hosted image via URL
#prediction = model.predict("https://...", hosted=True)

# Plot the prediction in an interactive environment
#prediction.plot()

# Convert predictions to JSON
#prediction.json()