import os
import glob
import subprocess
import time
from pynput import keyboard
import sys

username = os.getenv("USERNAME") or os.getenv("USER")
if not username:
    print("Could not determine username from environment variables.")
    sys.exit(1)

screenshots_path = f"C:/Users/{username}/Pictures/Screenshots"
if not os.path.isdir(screenshots_path):
    print("Screenshots directory does not exist.")
    sys.exit(1)

def get_latest_screenshot():
    files = glob.glob(os.path.join(screenshots_path, "*"))
    if not files:
        return None
    latest_file = max(files, key=os.path.getctime)
    wsl_path = latest_file.replace("C:", "/mnt/c").replace("\\", "/")
    return wsl_path

def paste_text(text):
    try:
        subprocess.run(["clip"], input=text, text=True, check=True, shell=True)
        time.sleep(0.2)
        ctrl = keyboard.Controller()
        ctrl.press(keyboard.Key.ctrl)
        ctrl.press('v')
        ctrl.release('v')
        ctrl.release(keyboard.Key.ctrl)
        print(f"Pasted: {text}")
    except subprocess.CalledProcessError:
        print("Failed to paste text")
    except Exception as e:
        print(f"Error pasting: {e}")

def on_hotkey():
    latest_screenshot = get_latest_screenshot()
    if latest_screenshot:
        paste_text(latest_screenshot)
    else:
        print("No screenshots found")

def main():
    print("Screenshot path copier running...")
    print("Press Alt+V to paste latest screenshot path")
    print("Press Ctrl+C to exit")
    with keyboard.GlobalHotKeys({'<alt>+v': on_hotkey}):
        try:
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("\nExiting...")

if __name__ == "__main__":
    main()
