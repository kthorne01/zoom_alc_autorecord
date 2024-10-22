import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# Step 1: Install webdriver-manager if it's not installed
try:
    from webdriver_manager.chrome import ChromeDriverManager
except ModuleNotFoundError:
    print("Installing webdriver-manager...")
    os.system('pip install webdriver-manager')
    from webdriver_manager.chrome import ChromeDriverManager  # Try to import again

# Step 2: Load environment variables from .env file
load_dotenv()

# Step 3: Get credentials from environment variables
ZOOM_EMAIL = os.getenv('ZOOM_EMAIL')
ZOOM_PASSWORD = os.getenv('ZOOM_PASSWORD')
MEETING_ID = os.getenv('MEETING_ID')

PMI_URL = f'https://zoom.us/j/{MEETING_ID}'

# Step 4: Set up WebDriver using webdriver-manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Step 5: Navigate to Zoom's login page
driver.get('https://zoom.us/signin')

# Step 6: Log in to Zoom
email_field = driver.find_element(By.ID, 'email')
password_field = driver.find_element(By.ID, 'password')
email_field.send_keys(ZOOM_EMAIL)
password_field.send_keys(ZOOM_PASSWORD)
password_field.send_keys(Keys.RETURN)

# Wait for login to complete
time.sleep(5)

# Step 7: Join the personal meeting room (PMI)
driver.get(PMI_URL)

# Allow time for the meeting to load
time.sleep(10)

# Step 8: Start recording (if available)
try:
    record_button = driver.find_element(By.XPATH, '//button[contains(text(), "Record")]')
    record_button.click()
    print("Recording started successfully.")
except Exception as e:
    print(f"Failed to start recording: {e}")

# Keep the browser open for 30 minutes
time.sleep(30 * 60)

# Step 9: Close the browser
driver.quit()

