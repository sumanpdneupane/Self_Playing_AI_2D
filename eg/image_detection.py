import cv2 as cv
import numpy as np
import pyautogui
import time
import mss

# For static images
def detect(original_image_path, detector_image_path):
    # Load Image
    original_image = cv.imread(original_image_path, cv.IMREAD_UNCHANGED)
    detector_image = cv.imread(detector_image_path, cv.IMREAD_UNCHANGED)
    
    # Detect/Match Image
    result = cv.matchTemplate(original_image, detector_image, cv.TM_CCORR_NORMED)
    
    # Get Best Locations of Matched Image
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    
    print(min_val, max_val)
    print(str(min_loc), str(max_loc))
    
    threshold = 0.8
    if max_val >= threshold:
        print("Image Found")
        
        # Drawing rectangle where image is found
        detector_image_w = detector_image.shape[1]
        detector_image_h = detector_image.shape[0]
        
        top_left = max_loc
        bottom_right = (top_left[0] + detector_image_w, top_left[1] + detector_image_h)
        
        cv.rectangle(original_image, top_left, bottom_right, 
                    color= (0, 255, 0), thickness= 2, lineType= cv.LINE_4)
        
        # cv.imshow("Result", original_image)
        # cv.waitKey()
        cv.imwrite("res/result.png", original_image)
    else:
        print("Image Not Found")

def findClickPoints(original_image_path, detector_image_path, threshold = 0.5, debug_mode = None):
    # Load Image
    original_image = cv.imread(original_image_path, cv.IMREAD_UNCHANGED)
    detector_image = cv.imread(detector_image_path, cv.IMREAD_UNCHANGED)
    niddle_w = detector_image.shape[1]
    niddle_h = detector_image.shape[0]
    
    # for debug_mode
    line_color = (0, 255, 0)
    line_type = cv.LINE_4
    marker_color = (0, 255, 0)
    marker_type = cv.MARKER_CROSS
    
    # Detect/Match Image
    method = cv.TM_SQDIFF_NORMED
    result = cv.matchTemplate(original_image, detector_image, method)   
    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))
    
    # first we need to create the list of [x, y, w, h] rectangles
    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), niddle_w, niddle_h]
        rectangles.append(rect)
    rectangles, weights = cv.groupRectangles(rectangles, 1, 0.5)
    
    points = []
    if len(rectangles):
        print("Found Needle")
        # need to look over all the locations and draw their rectangle
        for (x, y, w, h) in rectangles:
            center_X = x + int(w / 2)
            center_Y = y + int(h / 2)
            #Save the points
            points.append((center_X, center_Y))
            
            if debug_mode == 'rectangles':
                # determine box location
                top_left = (x, y)
                bottom_right = (x + w, y + h)
                # draw box
                cv.rectangle(original_image, top_left, bottom_right, line_color, line_type)
            elif debug_mode == 'points':
                cv.drawMarker(original_image, (center_X, center_Y), marker_color, marker_type)
        
        if debug_mode:
            cv.imshow("Matches", original_image)
            cv.waitKey()
        
    return points


# For Real time
def fastWindowCapture():
    loop_time = time.time()
    w, h = pyautogui.size()
    monitor = {"top": 0, "left": 0, "width": w, "height": h}
    
    # Create a named window before the loop starts
    cv.namedWindow("Computer Vision", cv.WINDOW_GUI_NORMAL)
    while(True):
        # Get Screenshots
        screenshot = mss.mss().grab(monitor)
        screenshot = np.array(screenshot)
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR) # Convert RBG to BGR
        
        # Get Click points
        # debug_mode= 'rectangles'
        # original = 'res/albion/result_click_point.jpg'
        # needle = 'res/albion/albion_cabbage.jpg'
        # findClickPoints(original, needle, threshold= 0.5, debug_mode= debug_mode)
        
        
        cv.imshow("Computer Vision", screenshot)
        
        print("FPS: {}".format(1 / (time.time() - loop_time)))
        loop_time = time.time()
        
        if cv.waitKey(1) == ord('q'):
            break
    
    cv.destroyAllWindows()
    print("Done")