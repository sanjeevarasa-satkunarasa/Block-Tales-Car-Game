import keyboard
import time
from PIL import Image
import pyautogui
import numpy as np
import cv2

# DEFINING DIFFERENT CRUCIAL 

def move_left():
    keyboard.press('a')
    time.sleep(0.1)
    keyboard.release('a')
    time.sleep(0.1)

def move_right():
    keyboard.press('d')
    time.sleep(0.1)
    keyboard.release('d')
    time.sleep(0.1)


#BBOX DEFINING 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
top_left1 = (100, 100)
bottom_right1 = (600, 500)

width1 = bottom_right1[0] - top_left1[0]
height1 = bottom_right1[1] - top_left1[1]

bbox1 = (top_left1[0], top_left1[1], width1, height1)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
top_left2 = (100, 100)
bottom_right2 = (600, 500)         # BBOX 2 INPUT

width2 = bottom_right2[0] - top_left2[0]
height2 = bottom_right2[1] - top_left2[1]

bbox2 = (top_left2[0], top_left2[1], width2, height2)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

screenshot1 = pyautogui.screenshot(region=bbox1)
screenshot2 = pyautogui.screenshot(region=bbox2)

# START
print("Press R to start")
keyboard.wait('r')

# New Code
# Need a variable to know where on the screen the car is
def capture_screen(region=None):
    screenshot = pyautogui.screenshot(region=region)
    img_bgr = np.array(screenshot)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    return img_rgb

def find_and_move(template, screen, threshold=0.9):
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Check if the match is above the threshold
    if max_val > threshold:  
        # Calculate the center of the template match location
        center_x = max_loc[0] + template.shape[1] // 2
        center_y = max_loc[1] + template.shape[0] // 2
        # Need to have a if sentence to decide where the rock is out of the 3 positions
        pyautogui.click(center_x, center_y) # Change this to move either left or right


def main():
    # Load the template image
    template = cv2.imread("needle.png", cv2.IMREAD_COLOR) # Change to template of obstacle

    while True:
        screen = capture_screen()

        find_and_move(template, screen)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

main()