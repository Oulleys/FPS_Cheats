from utils.screen_capture import capture_screen

def test_capture_screen():
    screen = capture_screen()
    assert screen is not None, "Screen capture failed"
    print("Screen capture test passed")