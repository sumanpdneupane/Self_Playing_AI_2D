import pyautogui
import detect_object_on_screen as doos
import keyboard

# source ai_venv/bin/activate

# Main function
def main():
    template_path = 'res/lunchpad.png'  # Replace with the path of your template image
    # screen = doos.capture_screen()

    # # Detect the image on the screen
    # result_screen, detected_points = doos.detect_image_on_screen(screen, template_path)
    # # result_screen, detected_points = detect_image_on_any_screen(screen, template_path)
    
    # # Print the detected points and center points
    # for point in detected_points:
    #     print(f"Detected at: {point['top_left']}, Center: {point['center']}")
    
    # # Get the first detected point (top_left and center)
    # first_point = detected_points[0]
    # center_point = first_point['center']
    
    # # Move the mouse to the center of the first detected point
    # pyautogui.moveTo(center_point[0]/2, center_point[1]/2, 2)
    # pyautogui.click()

    # # Display the result
    # cv2.imshow("Detected Image", result_screen)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    # doos.real_time_detection(template_path) 
    # doos.real_time_object_detection(template_path)
    # Bind the detection to a hotkey (F2)
    keyboard.add_hotkey("F2", lambda: doos.detect_image_on_screen(template_path))

    print("Press F2 to detect the image on screen. Press ESC to exit.")

    # Keep the script running to listen for hotkeys
    keyboard.wait("esc")  # Stops when 'ESC' is pressed

if __name__ == "__main__":
    main()
