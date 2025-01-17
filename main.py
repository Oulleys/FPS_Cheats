from utils.screen_capture import capture_screen
from utils.detection import find_target
from utils.mouse_control import smooth_move, click_target
import logging
from logging.handlers import RotatingFileHandler
import time
import cv2

# Configure logging
handler = RotatingFileHandler("logs/debug.log", maxBytes=5000000, backupCount=5)
logging.basicConfig(
    handlers=[handler],
    level=logging.DEBUG,
    format="%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def main():
    try:
        while True:
            # Capture the game screen
            screen = capture_screen()

            # Detect the target in the screen
            target_coords = find_target(screen)

            # If a target is found, move the mouse and auto-fire
            if target_coords:
                logging.info(f"Target found at: {target_coords}")
                smooth_move(*target_coords)
                click_target(target_coords, firing_rate=0.1)  # Auto fire at the target

            # Add a small delay to reduce CPU usage
            time.sleep(0.1)

    except KeyboardInterrupt:
        logging.info("Application terminated by user")
        print("Program terminated.")
    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}", exc_info=True)
    finally:
        # Ensure all OpenCV windows are closed
        cv2.destroyAllWindows()
        logging.info("All OpenCV windows closed")

if __name__ == "__main__":
    main()