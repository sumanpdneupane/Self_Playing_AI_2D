import numpy as np
import cv2

""" Contains helper functions like image preprocessing, logging, or timing.
    Keeps the core modules clean and reusable by offloading generic tasks.
"""

def preprocess_frame(frame, greyScale= True, resize= None):
    """ Preprocess the frame before passing to the agent (e.g., resize, grayscale).
    Args:
        frame (array): frame from the screen.
        greyScale (bool, optional): Convert to grayscale. Defaults to True.
        resize (tuple(int, int), optional): Resize to given dimensions (tuple(width, height)), e.g., (84, 84). Defaults to None.
    """
    if greyScale and len(frame.shape) == 3:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if resize:
        frame = cv2.resize(frame, resize)
    return frame

def compute_fitness(frame, threshold= 100):
    """ A simple fitness function based on the average brightness of the frame.
        If the screen is too dark, it could represent failure or the need for action.
    Args:
        frame  (array): The current game screen.
        threshold (int, optional): The brightness level below which action is required. Defaults to 100.
    """
    avg_brightness = np.mean(frame)
    return avg_brightness < threshold # True if action is needed

def show_frame(frame, delay= 1):
    """ Display the current frame in a window.
        Useful for debugging and testing.
    Args:
        frame (array): The current game screen.
        delay (int, optional): seconds to wait. Defaults to 1.
    """
    cv2.imshow("Game Screen", frame)
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        return False
    return True