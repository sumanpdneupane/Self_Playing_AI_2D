import pyautogui
import time
import threading

class InputController:
    """ Simulates keyboard and mouse inputs programmatically.
        Used to send actions to the game just like a human player would.
    """
    
    def __init__(self, delay= 0.01):
        """ Initialize Input Controller for keyboard and mouse
        Args:
            delay (float, optional): seconds to wait after each key/mouse action. Defaults to 0.01.
        """
        self.delay = delay
    
    # ========== KEYBOARD CONTROLS ==========   
    
    def press_key(self, key):
        """ Capture press keyboard key
        Args:
            key (string): Press and release a single key (like 'space', 'up', 'left')
        """
        pyautogui.press(key)
        time.sleep(self.delay)
        
    def hold_key(self, key, hold_time= 0.01):
        """ Capture press and hold keyboard key at once. 
        Args:
            key (string): Press and release a single key (like 'space', 'up', 'left')
            hold_time (float, optional): Hold a single key for a short duration. Defaults to 0.01.
        """
        pyautogui.keyDown(key)
        time.sleep(hold_time)
        
    def press_multiple_keys(self, keys):
        """ Capture press multiple keyboard keys
        Args:
            keys ([string]): Press and release a multiple keys (like 'space', 'up', 'left')
        """
        pyautogui.keys(keys)
        time.sleep(self.delay)
        
    def hold_multiple_keys(self, keys, hold_time= 0.01):
        """ Capture press and hold multiple keyboard keys at once. 
        Args:
            keys ([string]): Press and release a multiple keys (like 'space', 'up', 'left')
            hold_time (float, optional): Hold multiple keys simultaneously for a short duration. Defaults to 0.01.
        """
        for key in keys:
            pyautogui.keyDown(key)
        time.sleep(hold_time)
        for key in keys:
            pyautogui.keyUp(key)
        time.sleep(self.delay)
        
    # ========== MOUSE CONTROLS ==========
    
    def click_mouse(self, x= None, y= None):
        """ Click at the current or specific (x, y) location.
        Args:
            x (int, optional): X coordinate of screen. Defaults to None.
            y (int, optional): Y coordinate of screen. Defaults to None.
        """
        if x is not None and y is not None:
            pyautogui.click(x, y)
        else:
            pyautogui.click()
        time.sleep(self.delay)
        
    def move_mouse(self, x, y):
        """ Move at the current or specific (x, y) location.
        Args:
            x (int): X coordinate of screen.
            y (int): Y coordinate of screen.
        """   
        pyautogui.moveTo(x, y)
        time.sleep(self.delay)
        
    def move_and_click_mouse(self, x, y):
        """Move and Click at the current or specific (x, y) location.
        Args:
            x (int): X coordinate of screen.
            y (int): Y coordinate of screen.
        """
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(self.delay)
        
    def move_and_hold_mouse(self, x, y, hold_time= 0.01):
        """Move and Hold at the current or specific (x, y) location.
        Args:
            x (int): X coordinate of screen.
            y (int): Y coordinate of screen.
            hold_time (float, optional): Move the mouse and hold a click. Defaults to 0.01.
        """
        pyautogui.moveTo(x, y)
        pyautogui.mouseDown()
        time.sleep(hold_time)
        pyautogui.mouseUp()
        time.sleep(self.delay)
        
    # ========== COMBINED KEYBOARD AND MOUSE HANDLING ==========
    
    def handle_key_and_mouse(self, keys, x= None, y= None, hold_time= 0.01):
        """ Handle both key presses and mouse actions at the same time.
        Args:
            keys ([string]): List of keys to press or hold (like 'space', 'up', 'left')
            x (int, optional): X coordinates for mouse actions. Defaults to None.
            y (int, optional): Y coordinates for mouse actions. Defaults to None.
            hold_time (float, optional): Duration to hold keys or mouse click. Defaults to 0.01.
        """
        def keyboard_thread():
            if isinstance(keys, list):
                self.hold_multiple_keys(keys, hold_time)
            else:
                self.hold_key(keys, hold_time)
            
        def mouse_thread():
            if x is not None and y is not None:
                self.move_and_click_mouse(x, y)
            else:
                self.move_mouse(0, 0)
        
        # Create and start threads for simultaneous key and mouse handling
        kThread = threading.Thread(target= keyboard_thread)
        mThread = threading.Thread(target= mouse_thread)
        
        kThread.start()
        mThread.start()
        
        kThread.join()
        mThread.join()