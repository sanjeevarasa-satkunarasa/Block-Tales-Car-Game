import cv2
import numpy as np
import pyautogui

def capture_screen(region=None):
    screenshot = pyautogui.screenshot(region=region)
    img_bgr = np.array(screenshot)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    return img_rgb

def find_and_click(template, screen, threshold=0.9):
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Check if the match is above the threshold
    if max_val > threshold:
        # Calculate the center of the template match location
        center_x = max_loc[0] + template.shape[1] // 2
        center_y = max_loc[1] + template.shape[0] // 2
        pyautogui.click(center_x, center_y)

def main():
    # Load the template image
    template = cv2.imread("needle.png", cv2.IMREAD_COLOR)
    if template is None:
        print("Template image not found. Please ensure 'needle.png' is in the correct location.")
        return

    cv2.namedWindow("Screen Capture", cv2.WINDOW_NORMAL)
    print("Press 'q' to exit")

    while True:
        screen = capture_screen()
        find_and_click(template, screen)

        # Display the screen capture for visualization
        cv2.imshow("Screen Capture", cv2.cvtColor(screen, cv2.COLOR_RGB2BGR))

        # Check for key press
        key = cv2.waitKey(1) & 0xFF
        if key != 255:  # Ignore 'no key pressed' value
            print(f"Key pressed: {chr(key) if key < 128 else key} (ASCII: {key})")
        if key == ord('q'):
            print("Exiting loop...")
            break

    cv2.destroyAllWindows()
    print("Exited gracefully")

if __name__ == "__main__":
    main()