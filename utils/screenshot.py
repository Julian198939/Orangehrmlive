import os

def take_screenshot(driver, file_name="screenshot.png", save_path="screenshots"):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    file_path = os.path.join(save_path, file_name)
    driver.save_screenshot(file_path)
    print(f"Screenshot saved at {file_path}")