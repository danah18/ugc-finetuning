import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

profile_path = os.path.expanduser("~/Library/Application Support/Google/Chrome")

options = Options()
options.add_argument(f"user-data-dir={profile_path}")
options.add_argument("profile-directory=Profile 6")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

wait = WebDriverWait(driver, 2)

try:
    driver.get("https://app.foreplay.co/discovery-experts/uQRWPmAuzAVZHkOA1ncFkSjCWGk1")
    print("Navigation successful.")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class*="main-content"]')))
    print("Page loaded.")
except Exception as e:
    print(f"Error during navigation or waiting: {e}")
