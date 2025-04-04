import cv2
import numpy as np
import time
import pyautogui

# Function to capture the screen
def capture_screen():
    screenshot = pyautogui.screenshot()
    screen = np.array(screenshot)
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
    return screen

# Function to detect the image on the screen
def detect_image_on_screen(screen, template_path):
    # Read the template image you want to find on the screen
    template = cv2.imread(template_path)
    w, h = template.shape[1], template.shape[0]

    # Perform template matching
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8  # Adjust this value for better accuracy
    loc = np.where(result >= threshold)

    detected_points = []  # List to store detected points and their center coordinates

    # Draw a red rectangle around detected template and calculate center points
    for pt in zip(*loc[::-1]):
        top_left = pt
        bottom_right = (pt[0] + w, pt[1] + h)

        # Calculate center of the bounding box
        center_x = (top_left[0] + bottom_right[0]) // 2
        center_y = (top_left[1] + bottom_right[1]) // 2
        detected_points.append({'top_left': top_left, 'center': (center_x, center_y)})

        # Draw a red rectangle around the detected template
        cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    return screen, detected_points

# Function to detect the image on the screen without passing scaling parameters
def detect_image_on_any_screen(screen, template_path, threshold=0.8):
    # Read the template image you want to find on the screen
    template = cv2.imread(template_path)
    w, h = template.shape[1], template.shape[0]

    # Get the screen dimensions
    screen_height, screen_width = screen.shape[:2]

    # Automatically calculate the min and max scale based on the template and screen size
    min_scale = 0.1  # Start with 10% of the original size
    max_scale = min(screen_width / w, screen_height / h)  # The maximum scale based on the screen size

    # Step size: automatically calculate a reasonable step
    step = 0.05  # Step size of 5% of the scale (you can adjust this if needed)

    detected_points = []  # List to store detected points and their center coordinates
    found = False  # To track if any match is found

    # Perform template matching for different scales of the template
    for scale in np.arange(min_scale, max_scale, step):
        # Resize the template image to the current scale
        resized_template = cv2.resize(template, (int(w * scale), int(h * scale)))
        rw, rh = resized_template.shape[1], resized_template.shape[0]

        # Perform template matching
        result = cv2.matchTemplate(screen, resized_template, cv2.TM_CCOEFF_NORMED)
        
        # Get locations where the match is above the threshold
        loc = np.where(result >= threshold)

        # If any match is found, draw a red rectangle around it
        for pt in zip(*loc[::-1]):
            top_left = pt
            bottom_right = (pt[0] + rw, pt[1] + rh)

            # Calculate center of the bounding box
            center_x = (top_left[0] + bottom_right[0]) // 2
            center_y = (top_left[1] + bottom_right[1]) // 2
            detected_points.append({'top_left': top_left, 'center': (center_x, center_y)})

            # Draw a red rectangle around the detected template
            cv2.rectangle(screen, pt, (pt[0] + rw, pt[1] + rh), (0, 0, 255), 2)
            found = True  # Mark that a match was found

    if not found:
        print("No matches found!")

    return screen, detected_points

# Real-time detection loop
def real_time_detection(template_path):
    while True:
        start_time = time.time()  # Measure FPS

        # Capture screen
        screen = capture_screen()
        
        # Detect image
        result_screen, detected_points = detect_image_on_screen(screen, template_path)

        # Move the mouse to the first detected point (if found)
        if detected_points:
            center_point = detected_points[0]['center']
            print(f"Detected at: {detected_points[0]['top_left']}, Center: {center_point}")
            pyautogui.moveTo(center_point[0], center_point[1])

        # Show the detection result
        # cv2.imshow("Real-time Detection", result_screen)

        # FPS calculation
        end_time = time.time()
        fps = 1 / (end_time - start_time)
        print(f"FPS: {fps:.2f}")

        # Break loop on 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # cv2.destroyAllWindows()

# Function to detect the object in the live video feed
def detect_image_in_video(frame, template, threshold=0.8):
    h, w = template.shape[:2]

    # Perform template matching
    result = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)

    detected_points = []
    for pt in zip(*loc[::-1]):
        top_left = pt
        bottom_right = (pt[0] + w, pt[1] + h)

        # Calculate the center of the detected box
        center_x = (top_left[0] + bottom_right[0]) // 2
        center_y = (top_left[1] + bottom_right[1]) // 2
        detected_points.append({'top_left': top_left, 'center': (center_x, center_y)})

        # Draw a red rectangle around the detected template
        cv2.rectangle(frame, top_left, bottom_right, (0, 0, 255), 2)

    return frame, detected_points

# Real-time detection from webcam
def real_time_object_detection(template_path, camera_index=0):
    # Load the template image
    template = cv2.imread(template_path)
    if template is None:
        print("Error: Template image not found!")
        return

    # Open the camera
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print("Error: Could not open camera!")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame!")
            break

        # Detect the object in the frame
        result_frame, detected_points = detect_image_in_video(frame, template)

        # Move the mouse to the first detected object
        if detected_points:
            center_point = detected_points[0]['center']
            print(f"Detected at: {detected_points[0]['top_left']}, Center: {center_point}")
            pyautogui.moveTo(center_point[0], center_point[1])

        # Display the detection result
        cv2.imshow("Real-time Object Detection", result_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()