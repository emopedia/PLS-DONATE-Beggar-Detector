# PLS DONATE Beggar Detector

This Python script is designed to detect specific keywords in Roblox chat messages. It captures text from the top-left corner of the screen and identifies when certain keywords related to begging are mentioned. It also avoids detecting the same user multiple times.

## Prerequisites

Before you run the script, make sure you have the following installed:

- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **pip**: Python package installer (usually included with Python installation)

## Required Libraries

The script requires several Python libraries. You can install them using pip. Open a terminal or command prompt and run:

`pip install pytesseract pillow mss pyautogui opencv-python`

## Tesseract Installation

pytesseract is a Python wrapper for Google's Tesseract-OCR Engine. You need to install Tesseract separately:

    Windows: Download the installer from the official repository. After installation, add the Tesseract path to your system’s PATH variable.

    macOS: Install using Homebrew:
    brew install tesseract

    Linux: Install via package manager:
    sudo apt-get install tesseract-ocr

Run the Script: Open a terminal or command prompt, navigate to the directory where main.py is saved, and run:

    python main.py

## Notes

    Capture Area: The script captures a 400x250 pixel area from the top-left corner of the screen. Adjust the monitor dictionary in the capture_and_read_text function if necessary.
    Keyword List: Modify the keywords list in the main function to include any other keywords you wish to detect.
    Detection Frequency: The script checks for new messages every 5 seconds. Adjust the time.sleep(5) value in the main function to change the frequency.

## Troubleshooting

    No Output: Ensure Roblox is the active window when the script is running. Make sure the area being captured contains the chat.
    Tesseract Errors: Verify that Tesseract is properly installed and its path is added to your system's PATH variable.

This is still WIP and currently has many bugs, if you want to contribute to the program, make a pull request.
