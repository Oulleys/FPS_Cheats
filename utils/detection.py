import cv2
import numpy as np
import logging

# Remove or comment out the debug windows:
# cv2.namedWindow("Detection Debug", cv2.WINDOW_NORMAL)
# cv2.namedWindow("Mask Debug", cv2.WINDOW_NORMAL)
# cv2.namedWindow("HSV Screen Debug", cv2.WINDOW_NORMAL)

def find_target(screen):
    logging.debug("Attempting to find target...")
    try:
        # Convert screen to HSV for better color filtering
        hsv = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)

        # Log HSV value at the center of the screen (helpful for debugging)
        center_hsv = hsv[hsv.shape[0] // 2, hsv.shape[1] // 2]
        logging.debug(f"Sample HSV value at center: {center_hsv}")

        # Define the HSV range for bot color (adjust these based on your observations)
        lower_bot_color = np.array([10, 50, 50])  # Adjust to match bot's colors
        upper_bot_color = np.array([30, 255, 255])  # Adjust to match bot's colors
        logging.debug(f"HSV thresholds for bot: lower={lower_bot_color}, upper={upper_bot_color}")

        # Create a mask for the bot's color
        mask = cv2.inRange(hsv, lower_bot_color, upper_bot_color)

        # Optional: Remove the mask display
        # cv2.imshow("Mask Debug", mask)
        # cv2.waitKey(1)

        # Log the number of pixels detected by the mask
        mask_pixels = np.count_nonzero(mask)
        logging.debug(f"Mask non-zero pixels: {mask_pixels}")

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Process contours to find valid targets (bots)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            logging.debug(f"Detected contour at ({x}, {y}) with size ({w}x{h})")

            # Filter out invalid sizes (too small or too large)
            if w < 10 or h < 10:
                logging.info("Target ignored (too small)")
                continue
            if w > 500 or h > 500:
                logging.info("Target ignored (too large)")
                continue

            # Draw a rectangle around the detected bot
            cv2.rectangle(screen, (x, y), (x + w, y + h), (0, 255, 0), 2)
            logging.info(f"Valid target detected at: ({x + w // 2}, {y + h // 2})")

            # Show the detection debug window with overlays (optional, can be commented out)
            # cv2.imshow("Detection Debug", screen)
            # cv2.waitKey(1)  # Allow window to refresh without creating new ones

            return x + w // 2, y + h // 2

        # Update the detection window if no valid targets are found (optional)
        # cv2.imshow("Detection Debug", screen)
        # cv2.waitKey(1)
        logging.warning("No valid targets found")
        return None
    except Exception as e:
        logging.error(f"Error in target detection: {e}", exc_info=True)
        return None