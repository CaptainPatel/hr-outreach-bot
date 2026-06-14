from pathlib import Path
import time
import sys, subprocess, os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ---------- Browser Setup ----------

def create_driver():

    options = Options()

    profile_path = Path.cwd() / "browser_profile"

    options.add_argument(
        f"user-data-dir={profile_path}"
    )

    driver = webdriver.Chrome(options=options)

    return driver

# ---------- Function ----------

def send_message(driver, phone, message):

    url = f"https://web.whatsapp.com/send?phone={phone}"

    driver.get(url)

    message_box = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//div[@contenteditable="true"][@data-tab="10"]'
            )
        )
    )

    message_box.send_keys(message)

    message_box.send_keys(Keys.ENTER)
    
    time.sleep(5)

def copy_resume_to_clipboard(resume_path):
    """
    Copy resume PDF file to system clipboard
    
    Why we need this:
    - pyautogui.hotkey("ctrl", "v") pastes from clipboard
    - We need to copy the file there BEFORE we try to paste
    - This function does that
    """
    
    # Step 1: Check if file exists
    if not os.path.exists(resume_path):
        raise FileNotFoundError(f"Resume not found at: {resume_path}")
    
    # Step 2: Get absolute path (in case relative path given)
    resume_path = os.path.abspath(resume_path)
    
    # Step 3: Copy to clipboard (works on Windows, Mac, Linux)
    if sys.platform == "win32":
        # Windows: Use PowerShell
        subprocess.run([
            "powershell",
            "-Command",
            f'Set-Clipboard -Path "{resume_path}"'
        ], check=True)
    elif sys.platform == "darwin":
        # Mac: Use pbcopy
        subprocess.run(["cp", resume_path, "-"], stdout=subprocess.PIPE)
    else:
        # Linux: Use xclip or xsel
        subprocess.run(["xclip", "-selection", "clipboard", "-i", resume_path])
    
    print(f"✅ Resume copied to clipboard: {resume_path}")

def send_resume(driver, resume_path):
    
    # Copy resume to clipboard FIRST
    copy_resume_to_clipboard(resume_path)
    time.sleep(1)
    
    # Find textbox
    wait = WebDriverWait(driver, 30)
    textbox = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            '//div[@contenteditable="true"][@role="textbox"]'
        ))
    )
    
    # Click textbox
    textbox.click()
    time.sleep(1)
    
    # Check OS for appropriate paste method
    current_os = sys.platform
    
    if current_os in ["win32", "darwin"]:  # Windows or Mac
        # Import ONLY on Windows/Mac (has GUI)
        import pyautogui
        
        pyautogui.click()
        time.sleep(1)
        pyautogui.hotkey("ctrl", "v")
    else:
        # Linux/Docker (no GUI), use Selenium
        textbox.send_keys(Keys.CONTROL + 'v')
    
    print("Ctrl+V pressed")
    time.sleep(5)
    
    # Send resume
    if current_os in ["win32", "darwin"]:
        import pyautogui
        pyautogui.press("enter")
    else:
        textbox.send_keys(Keys.ENTER)
    
    print("Resume sent")
    time.sleep(8)

