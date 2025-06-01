from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://app.foreplay.co/discovery-experts/uQRWPmAuzAVZHkOA1ncFkSjCWGk1")

wait = WebDriverWait(driver, 10)

input_elements = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "input")))
  
username_input = input_elements[0]
password_input = input_elements[1]

# Fill in credentials
username_input.send_keys("replace-with-username")
password_input.send_keys("replace-with-password")

# Click login button
login_button = wait.until(EC.element_to_be_clickable(driver.find_element(By.TAG_NAME, "button")))
login_button.click()

# Wait for dashboard or main page to load after login
experts_tab = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[text()[normalize-space()='Experts']]"))
)
experts_tab.click()

driver.get("https://app.foreplay.co/discovery-experts/uQRWPmAuzAVZHkOA1ncFkSjCWGk1")

# Wait until the play icon div is clickable
play_icon_div = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class*="rounded-full"][class*="bg-black"]') ))

print(play_icon_div)

# Click the play icon
play_icon_div.click()

# Wait for video element to appear
video = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'video')))

# Get the video URL
video_url = video.get_attribute('src')
print("Video URL:", video_url)

# # images = driver.find_element(By.TAG_NAME, "img")
# # for image in images:
# #     print(image.get_attribute("src"))

# Example: find all video sources
videos = driver.find_elements(By.TAG_NAME, "video")

for video in videos:
    print(video.get_attribute("src"))
print("done.")

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class*="main-content"]')))