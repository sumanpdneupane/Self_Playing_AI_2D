import pyautogui
import detect_object_on_screen as doos
import image_detection as imd

# source ai_venv/bin/activate

def fromChatGPT():
    # 1.
    template_path = 'res/lunchpad.png'  # Replace with the path of your template image
    screen = doos.capture_screen()

    # Detect the image on the screen
    result_screen, detected_points = doos.detect_image_on_screen(screen, template_path)
    # result_screen, detected_points = detect_image_on_any_screen(screen, template_path)
    
    # Print the detected points and center points
    for point in detected_points:
        print(f"Detected at: {point['top_left']}, Center: {point['center']}")
    
    # Get the first detected point (top_left and center)
    first_point = detected_points[0]
    center_point = first_point['center']
    
    # Move the mouse to the center of the first detected point
    pyautogui.moveTo(center_point[0]/2, center_point[1]/2, 2)
    pyautogui.click()

    # # Display the result
    # cv2.imshow("Detected Image", result_screen)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    # 2.
    # doos.real_time_detection(template_path) 
    # doos.real_time_object_detection(template_path)

def findClickPoints():
    debug_mode= 'rectangles'
    # debug_mode= 'points'
    
    # original = 'res/desktop.png'
    # needle = 'res/ee.png'
    
    original = 'res/albion/result_click_point.jpg'
    needle = 'res/albion/albion_cabbage.jpg'
    
    imd.findClickPoints(original,needle, threshold= 0.4, debug_mode= debug_mode)

def fastWindowCapture():
    imd.fastWindowCapture()

# Main function
def main():
    # fromChatGPT()
    # findClickPoints()
    fastWindowCapture()
    

if __name__ == "__main__":
    main()
