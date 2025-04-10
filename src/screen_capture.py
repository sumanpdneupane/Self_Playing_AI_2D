import mss
import numpy as np
import cv2


class ScreenCapture:
    """ Captures the current screen (or a region) as image data for the AI to analyze.
        Acts as the visual input source for the GameDecisionAgent.
    """
    
    def __init__(self, top=100, left= 100, width= 640, height= 480):
        """ Initialize the screen capture area.
        Args:
            top (int, optional): _description_. Defaults to 100.
            left (int, optional): _description_. Defaults to 100.
            width (int, optional): _description_. Defaults to 640.
            height (int, optional): _description_. Defaults to 480.
        """
        self.monitor = {
            "top": top,
            "left": left,
            "width": width,
            "height": height,
        }
        self.sct = mss.mss()
    
    def grab_frame(self, greyScale= True, resize= None):
        """ Captures a single frame from the screen.
        Args:
            greyScale (bool, optional): whether to convert the frame to grayscale. Defaults to True.
            resize (tuple (width, height), optional): tuple (width, height) to resize the image. Defaults to None.
        """
        frame = np.array(self.sct.grab(self.monitor))
        
        # Optional convert to greyScale
        if greyScale:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Option resize
        if resize:
            frame = cv2.resize(frame, resize)
            
        return frame
    
    def preview(self, delay= 1):
        """ Continuously show the screen preview in a window.
            Press 'q' to quit.
        Args:
            delay (int, optional): _description_. Defaults to 1.
        """
        while True:
            frame = self.garb_frame()
            cv2.imshow("Game Screen", frame)
            
            if cv2.waitKey(delay) & 0xFF == ord('q'):
                break 
        
        cv2.destroyAllWindows()