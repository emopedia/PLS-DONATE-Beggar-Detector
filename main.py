import pytesseract
from PIL import Image
import mss
import pyautogui
import time
import re

def is_roblox_active():
    return "Roblox" in pyautogui.getActiveWindowTitle()

def capture_and_read_text():
    with mss.mss() as sct:
        monitor = {"top": 0, "left": 0, "width": 400, "height": 250} 
        sct_img = sct.grab(monitor)
        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        text = pytesseract.image_to_string(img)
        return text

def process_text(text, keywords, detected_users):
    lines = text.splitlines()
    for line in lines:
        line = line.strip().lower()
        if not line:
            continue
        
        if re.match(r'^[a-z0-9]+', line):
            for keyword in keywords:
                if keyword in line:
                    username = line.split()[0] 
                    if username not in detected_users:
                        detected_users.add(username)
                        print(f"Detected: {username} mentioned {keyword}")
                    break

def main():
    keywords = ["pls donate", "dono", "come", "pls", "please", "help", "donate"]
    detected_users = set() 
    
    print("Started")
    while True:
        if is_roblox_active():
            text = capture_and_read_text()
            process_text(text, keywords, detected_users)
        time.sleep(5) 

if __name__ == "__main__":
    main()
