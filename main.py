import keyboard
import time
from PIL import Image
import pyautogui
import numpy as np
import cv2

# Define control functions
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

# Function to capture the screen
def capture_screen(region=None):
    screenshot = pyautogui.screenshot(region=region)
    img_bgr = np.array(screenshot)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    return img_rgb

# Function to find and move based on templates
def find_and_move(templates, screen, threshold=0.9):
    for template in templates:
        result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val > threshold:
            center_x = max_loc[0] + template.shape[1] // 2
            center_y = max_loc[1] + template.shape[0] // 2

            # Differentiate between stones and trees based on max_val
            if max_val > 0.8:  # High confidence in identification
                if 0 <= center_x < 200:
                    if car_x == 1:
                        move_right()
                        car_x = 2
                        continue
                elif 200 <= center_x < 400:
                    if car_x == 2:
                        move_right()
                        car_x = 3
                        continue
                else:
                    if car_x == 3:
                        move_left()
                        car_x = 2
                        continue
            else:
                # Low confidence in identification, treat as unknown
                pass

# Main function
def main():
    template_paths = ["templates/stone_1.png", "templates/stone_2.png", "templates/stone_3.png",
                      "templates/tree_1.png", "templates/tree_2.png", "templates/tree_3.png"]
    templates = [cv2.imread(path, cv2.IMREAD_COLOR) for path in template_paths]

    if any(t is None for t in templates):
        print("One or more template images not found. Please ensure all templates are in the correct location.")
        return

    cv2.namedWindow("Screen Capture", cv2.WINDOW_NORMAL)
    print("To exit, press 'q' on the Screen Capture Window")

    global car_x
    car_x = 2  # Initialize car position in the middle

    # Define the region to capture (left, top, width, height)
    region = (666, 293, 587, 492)
    
    while True:
        screen = capture_screen()
        find_and_move(templates, screen)

        cv2.imshow("Screen Capture", cv2.cvtColor(screen, cv2.COLOR_RGB2BGR))
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            print("Exiting loop...")
            break

    cv2.destroyAllWindows()
    print("Exited gracefully")

# Start the program
print("Press R to start")
keyboard.wait('r')
main()
