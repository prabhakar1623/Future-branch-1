# test_login.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_success(setup):
    driver = setup
    driver.get("https://app.meta-path.ai/cdHome/login")  # <-- your login page URL
    
    # Locate username and password fields (change selectors as needed)
    driver.find_element(By.ID, "username").send_keys("prabhakar_QACND919160")
    driver.find_element(By.ID, "password").send_keys("8rm4JXd1")
    
    # Click Login button
    next=driver.find_element(By.XPATH,"//input[@value='Continue']")
    next.click()
    
    time.sleep(3)
    


def test_login_invalid_credentials(setup):
    driver = setup
    driver.get("https://app.meta-path.ai/cdHome/login")
    
    driver.find_element(By.ID, "username").send_keys("wronguser")
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    next=driver.find_element(By.XPATH,"//input[@value='Continue']")
    next.click()
    
    time.sleep(3)
    
    # Check for error message
    assert "Invalid credentials" in driver.page_source or "error" in driver.current_url