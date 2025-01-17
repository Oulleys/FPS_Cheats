import logging
from PIL import ImageGrab
import numpy as np
import cv2

# Create a named window for screen capture (optional, only for displaying capture)
cv2.namedWindow("Captured Screen", cv2.WINDOW_NORMAL)

def capture_screen():
    """
    Capture the center of the screen using native system APIs (Pillow).
    """
    try:
        logging.debug("Starting screen capture...")

        # Define screen dimensions
        screen_width = 1920
        screen_height = 1080
        region_width = 800
        region_height = 600

        # Calculate centered region
        left = (screen_width - region_width) // 2
        top = (screen_height - region_height) // 2
        right = left + region_width
        bottom = top + region_height

        # Capture the screen using Pillow
        screen = ImageGrab.grab(bbox=(left, top, right, bottom))
        screen_np = np.array(screen)

        # Debugging: Display the captured screen
        cv2.imshow("Captured Screen", screen_np)
        cv2.waitKey(1)  # Allow window to refresh without creating new ones

        # Log screen shape and dtype
        logging.debug(f"Captured screen shape: {screen_np.shape}, dtype: {screen_np.dtype}")
        logging.info(f"Screen captured successfully at region: top={top}, left={left}, width={region_width}, height={region_height}")
        return screen_np
    except Exception as e:
        logging.error(f"Error capturing screen: {e}", exc_info=True)
        return None