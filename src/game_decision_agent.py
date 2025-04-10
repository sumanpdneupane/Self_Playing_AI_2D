import time
from src.screen_capture import ScreenCapture
from src.input_controller import InputController
from src.utils import preprocess_frame, compute_fitness, show_frame

class GameDecisionAgent:
    """ Makes decisions based on screen input using a learning strategy (e.g., Genetic Algorithm).
        It outputs actions (like key presses or mouse moves) to control the game.
    """
    
    def __init__(self):
        self.capture = ScreenCapture(top=150, left=150, width=640, height=480)
        self.controller = InputController()
        self.running = True

    def dummy_decision(self, frame):
        """
        Example logic: if screen is 'dark', press space.
        Replace with AI later.
        """
        processed_frame = preprocess_frame(frame, greyScale=True, resize=(84, 84))
        if compute_fitness(processed_frame):
            return True
        return False

    def run(self):
        print("Starting in 3 seconds...")
        time.sleep(3)

        frame_counter = 0
        while self.running:
            frame = self.capture.grab_frame()

            # Real-time processing: Avoid unnecessary display delays
            frame_counter += 1
            if frame_counter % 10 == 0:  # Only show every 10th frame for performance
                if not show_frame(frame):
                    break

            # AI/Decision making
            if self.dummy_decision(frame):
                print("🧠 Action: Pressing SPACE")
                self.controller.press_key('space')

            # Example of controlling keys and mouse simultaneously
            print("🧠 Action: Moving and clicking the mouse while pressing 'up' and 'right' keys")
            self.controller.handle_key_and_mouse(['up', 'right'], x=500, y=400, hold_time=3)

        print("Agent stopped.")
