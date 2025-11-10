from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import os


service = Service(r"C:\chromedriver-win64\chromedriver.exe")  
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.get("https://app.meta-path.ai/cdHome/login")
gmail=driver.find_element(By.ID,"username")
gmail.send_keys("prabhakar_QACND919160")
password=driver.find_element(By.ID,"password")
password.send_keys("8rm4JXd1")
next=driver.find_element(By.XPATH,"//input[@value='Continue']")
next.click()
time.sleep(10)
#checking for accept agreement
try:
    check=driver.find_element(By.XPATH,"//span[@class='checkmark']")
    check.click()
    time.sleep(10)
    element = driver.find_element(By.XPATH,"//button[normalize-space()='continue']")
    element.click()
except NoSuchElementException:
# Element not found — skip to next step
    print("'Continue' button not found, skipping this step...")

 #pan document
pan=driver.find_element(By.XPATH,"//div[7]//div[1]//div[1]//div[2]")
pan.click()
time.sleep(3)
#pan uploaded path
folder_path = r"C:\\Users\\prabhakaran\\Downloads\\New folder"
file_name= "pan card.jpeg"
file_path = os.path.join(folder_path, file_name)
upload_input = driver.find_element(By.XPATH, "//input[@type='file']")
upload_input.send_keys(file_path)
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='fathername']").send_keys("Ramamoorthy")
wait = WebDriverWait(driver, 3)
for _ in range(3):  # retry up to 3 times if stale
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//select[@id='gender']")))
            dropdown = driver.find_element(By.XPATH, "//select[@id='gender']")
            Select(dropdown).select_by_visible_text("Male")
            print(" Gender selected as 'Male'")
            break
        except StaleElementReferenceException:
            print(" Dropdown became stale retrying...")
driver.find_element(By.XPATH,"//input[@id='bloodgroup']").send_keys("B+")
driver.find_element(By.XPATH,"//div[@class='logo_upload_wrapper']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//label[normalize-space()='Click to upload image']").click()
time.sleep(2)
folder_path_my= r"C:\\Users\\prabhakaran\\Downloads\\New folder"
file_name_my= "my pic.jpeg"
file_path_my = os.path.join(folder_path_my, file_name_my)
upload_input = driver.find_element(By.XPATH, "//input[@type='file']")
upload_input.send_keys(file_path_my)
wait = WebDriverWait(driver, 20)

try:
    # Wait until the modal content is visible
    modal = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='modal-content']"))
    )
    print("✅ Modal content is visible.")

    # Once modal appears, wait for and click the Save button
    save_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']"))
    )
    save_button.click()
    print("💾 Save button clicked successfully!")

except Exception as e:
    print(f"⚠️ Modal or Save button not found: {e}")
"""
wait = WebDriverWait(driver, 20)
wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='modal-content']")))
time.sleep(2)
driver.find_element(By.XPATH,"//button[normalize-space()='Save']").click()
"""

time.sleep(30)

