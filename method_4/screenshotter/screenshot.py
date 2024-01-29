import pyautogui

def take_screenshot():
  # Get the screen size
  screen_width, screen_height = pyautogui.size()


  # Capture the screenshot
  screenshot = pyautogui.screenshot()

  # Save the screenshot to a file
  screenshot.save("screenshot.png")

  print("Screenshot captured and saved as 'screenshot.png'")
take_screenshot()