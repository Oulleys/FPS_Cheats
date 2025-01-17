import cv2
from utils.detection import find_target

def test_find_target():
    # Load a sample image with a known target for testing
    screen = cv2.imread("test_images/test_target.png")

    # Detect the target
    coords = find_target(screen)

    # Assert that target is detected
    assert coords is not None, "Target detection failed"
    print(f"Target detected at: {coords}")