#BBOX DEFINING 
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