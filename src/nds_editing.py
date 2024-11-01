import os, subprocess
import time
import mouse
import pyautogui
import win32gui
import pyperclip

from src.battle_class import*

# mouse.click('left')
# mouse.click('right')
# mouse.click('middle')
# mouse.get_position()

# scroll down
# mouse.wheel(-1)
# scroll up
# mouse.wheel(1)

# drag from (0, 0) to (100, 100) relatively with a duration of 0.1s
# mouse.drag(0, 0, 100, 100, absolute=False, duration=0.1)
# move 100 right & 100 down
# mouse.move(100, 100, absolute=False, duration=0.2)

"""
This will move the mouse relatively for 0.2 seconds. Let's break down what each parameter in this function call means:

(100, 100): These are the x and y coordinates to which you want to move the mouse cursor. In this case, both are set to 100.
absolute=False: This parameter determines the nature of the movement:
When absolute is set to False, the movement is relative. This means the cursor will move 100 pixels to the right (x-coordinate) and 100 pixels down (y-coordinate) from its current position.
If absolute were set to True, the cursor would move to the absolute position (100, 100) on the screen, where (0, 0) is typically the top-left corner of the screen.
duration=0.2: This parameter specifies the duration of the movement in seconds. It's set to 0.2, meaning the cursor will take 0.2 seconds to complete the movement. This creates a smooth, animated cursor movement rather than an instantaneous jump. If the duration were set to 0, the movement would be immediate.
"""

def get_active_window_title():
    return win32gui.GetWindowText(win32gui.GetForegroundWindow())
def get_active_window_rect()->list[int]:
    return win32gui.GetWindowRect(win32gui.GetForegroundWindow())

def edit_nds(filepath:str, filename:str, battles:list[PokemonBattle]):
    dspre_relative_path = "./dspre/DSPRE.exe"
    dspre_path = os.path.realpath(dspre_relative_path)
    subprocess.Popen(dspre_path)
    
    # Going to the DSPRE window -------------------------------------------------------------------
    correct_window_title = "DS Pokémon Rom Editor Reloaded 1.11.1 (Nømura, AdAstra/LD3005, Mixone)"
    alt_tab_counter = 0
    while get_active_window_title()!= correct_window_title:
        pyautogui.keyDown('alt')
        for i in range(alt_tab_counter):
            pyautogui.press('tab')
        pyautogui.keyUp('alt')
        alt_tab_counter += 1
        if alt_tab_counter > 10:
            raise Exception("DSPRE window not found. Too many windows opened?")
        
    # Put the mouse at the top left of the current window -----------------------------------------
    [window_tl_x, window_tl_y, window_dr_x, window_dr_y] = win32gui.GetWindowRect(win32gui.GetForegroundWindow())

    # Open ROM (the input file, manually extracted by user) ---------------------------------------
    mouse.move(window_tl_x, window_tl_y, absolute=True, duration=0)
    mouse.move(50, 100, absolute=False, duration=0)
    mouse.click('left')
    while get_active_window_title() != "Ouvrir":
        time.sleep(0.5)
    current_rect = get_active_window_rect()
    mouse.move(current_rect[0] + 550, current_rect[1] + 75, absolute=True, duration=0)
    mouse.click('left')
    rom_file_path = os.path.realpath(filepath)
    pyperclip.copy(rom_file_path)
    pyautogui.hotkey('ctrl', 'V')
    pyautogui.press('enter')
    mouse.move(current_rect[0] + 300, current_rect[1] + 515, absolute=True, duration=0)
    mouse.click('left')
    pyperclip.copy(filename)
    pyautogui.hotkey('ctrl', 'V')
    pyautogui.press('enter')
    pyautogui.press('enter')

    # Processing the given data -------------------------------------------------------------------


    pass