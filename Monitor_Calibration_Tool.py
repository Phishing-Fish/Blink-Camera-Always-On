from multiprocessing.connection import Listener
import time
import pyautogui
import platform
import os
import pynput
import math



#Determine OS#
Windows = False
Clear_Screen = "clear"
OS = platform.system()
if OS == "Windows":
    Windows = True
    Clear_Screen = "cls"

#Intro Page#
print(" __  ___            _ _               _____       _ _ _               _   _               _____           _ ")
print("|  \/  |           (_) |             /  __ \     | (_) |             | | (_)             |_   _|         | |")
print("| .  . | ___  _ __  _| |_ ___  _ __  | /  \/ __ _| |_| |__  _ __ __ _| |_ _  ___  _ __     | | ___   ___ | |")
print("| |\/| |/ _ \| '_ \| | __/ _ \| '__| | |    / _` | | | '_ \| '__/ _` | __| |/ _ \| '_ \    | |/ _ \ / _ \| |")
print("| |  | | (_) | | | | | || (_) | |    | \__/\ (_| | | | |_) | | | (_| | |_| | (_) | | | |   | | (_) | (_) | |")
print("|_|  |_/\___/|_| |_|_|\__\___/|_|     \____/\__,_|_|_|_.__/|_|  \__,_|\__|_|\___/|_| |_|   \_/\___/ \___/|_|")
print(" ")
input("To begin, press 'enter'")
os.system(Clear_Screen)
print("Instructions")
print(" ")
print("There are a couple of different places that the script will need to click.")
print("Because the script does not do image recognition, but instead checks a specific pixel color, calibrating the script to your monitor's exact resolution is neccessary")
print("This script will take you through a series of questions, use the mouse to click on the requested button")
print("Picture references for the different kinds of buttons can be found in in the GitHub repository, incase you are unsure of what the tool is asking you")
print("Once you have started a test, you will have 5 seconds to set your Blink app to full screen before your mouse click will be registered")
print(" ")
input("Once you have read the above directions, press 'enter' to begin")
os.system(Clear_Screen)
#Calibrate Continue button#
calibrating = True
print("You are going to click on the continue button at the bottom of the screen")
print("Once you have clicked the continue button, exit fullscreen and navigate back to the calibration tool window")
input("Once you have read the above directions, press 'enter' to begin your 5 second countdown")
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("If you are seeing this, you are too late. Please restart the tool and try again")
def on_click(x, y, button, pressed):
    global continue_button_x
    global continue_button_y
    continue_button_x = x
    continue_button_y = y
    if not pressed:
        # Stop listener
        return False
with pynput.mouse.Listener(
        on_click=on_click) as listener:
    listener.join()

continue_button_x = math.trunc(continue_button_x)
continue_button_y = math.trunc(continue_button_y)
pyautogui.moveTo(100, 100)
continue_button_color = pyautogui.pixel(continue_button_x, continue_button_y)
os.system(Clear_Screen)
#Calibrate Play Button#
print("Continue button data successfully collected!")
print("You are now going to click on the play button in the middle of the screen")
print("You can view the play button by waiting for the camera feed to time out. Let the feed run without clicking the continue button.")
print("Once you have clicked the play button, exit fullscreen and navigate back to the calibration tool window")
input("Once you have read the above directions, press 'enter' to begin your 5 second countdown")
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("If you are seeing this, you are too late. Please restart the tool and try again")
def on_click(x, y, button, pressed):
    global play_button_x
    global play_button_y
    play_button_x = x
    play_button_y = y
    if not pressed:
        # Stop listener
        return False
with pynput.mouse.Listener(
        on_click=on_click) as listener:
    listener.join()
play_button_x = math.trunc(play_button_x)
play_button_y = math.trunc(play_button_y)
pyautogui.moveTo(100, 100)
play_button_color = pyautogui.pixel(play_button_x, play_button_y)
os.system(Clear_Screen)
#Wait to continue if needed
print("Play button data successfully collected!")
print("Below are the locations of the buttons on your screen and the associated RGB values.")
print("Copy these values down and return to the Instructions PDF")
print(" ")
print("Continue Button X Value = " + str(continue_button_x))
print(" ")
print("Continue Button Y Value = " + str(continue_button_y))
print(" ")
print("Continue Button RGB values = " + str(continue_button_color))
print(" ")
print("Play Button X Value = " + str(play_button_x))
print(" ")
print("Play Button X Value = " + str(play_button_y))
print(" ")
print("Play Button RGB values = " + str(play_button_color))





 
    


    












                                                                                                            