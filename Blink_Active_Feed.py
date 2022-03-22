continue_button_x_value = ENTER VALUE HERE
##########################################
continue_button_y_value = ENTER VALUE HERE 
##########################################
continue_button_red_value = ENTER VALUE HERE 
##########################################
continue_button_green_value = ENTER VALUE HERE 
##########################################
continue_button_blue_value = ENTER VALUE HERE 
##########################################
play_button_x_value = ENTER VALUE HERE 
##########################################
play_button_y_value = ENTER VALUE HERE 
##########################################
play_button_red_value = ENTER VALUE HERE 
##########################################
play_button_green_value = ENTER VALUE HERE 
##########################################
play_button_blue_value = ENTER VALUE HERE
##########################################
# Do not touch below text unless you know what you are doing! #
##########################################


import time
import pyautogui

while True:
    continueButton = pyautogui.pixelMatchesColor(continue_button_x_value, continue_button_y_value, (continue_button_red_value, continue_button_green_value, continue_button_blue_value))
    playButton = pyautogui.pixelMatchesColor(play_button_x_value, play_button_y_value, (play_button_red_value, play_button_green_value, play_button_blue_value))
    if continueButton == True:
        pyautogui.click(continue_button_x_value, continue_button_y_value)
    elif playButton == True:
        pyautogui.click(play_button_x_value, play_button_y_value)
    else:
       time.sleep(5) 