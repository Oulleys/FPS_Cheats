import pyautogui
import time
import logging

def smooth_move(x, y, duration=0.1):
    """
    Smoothly move the mouse to the given coordinates (x, y) over a certain duration.
    :param x: Target x-coordinate
    :param y: Target y-coordinate
    :param duration: Time to take to move the mouse to the target (in seconds)
    """
    try:
        pyautogui.moveTo(x, y, duration=duration)
        logging.info(f"Moved mouse to ({x}, {y})")
    except Exception as e:
        logging.error(f"Error in smooth_move: {e}", exc_info=True)

def click_target(target_coords, firing_rate=0.1):
    """
    Simulate continuous mouse clicks at the target coordinates.
    :param target_coords: (x, y) coordinates where the target is located
    :param firing_rate: Delay between each shot in seconds (adjust as needed)
    """
    try:
        # Move the mouse to the target position
        pyautogui.moveTo(target_coords[0], target_coords[1])

        # Simulate continuous firing by clicking repeatedly
        while True:
            # Perform the mouse click (left-click)
            pyautogui.click()

            # Log the click event for debugging
            logging.info(f"Firing at target {target_coords}")

            # Add a small delay between shots (to prevent over-clicking too fast)
            time.sleep(firing_rate)

    except Exception as e:
        logging.error(f"Error during auto-firing: {e}", exc_info=True)