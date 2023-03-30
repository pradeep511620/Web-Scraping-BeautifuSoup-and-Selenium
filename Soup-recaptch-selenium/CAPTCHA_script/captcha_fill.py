import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
# URL to scrape
url = "https://www.raptorsupplies.com/"

options = webdriver.FirefoxOptions()  # CLOUD

options.add_argument(
     "--user-agent=" + "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)")  # CLOUD
options.binary_location=r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path=r"C://Users//hp//Downloads//geckodriver.exe", options=options)  # CLOUD

driver.get(url)

name = driver.find_element(By.ID, "contactus_name")
name.send_keys("rahul")

email = driver.find_element(By.ID, "email")
email.send_keys("rk2153691@gmail.com")

phone = driver.find_element(By.ID, "phone")
phone.send_keys("8294966962")


WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha/api2/anchor?']")))
WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "div.recaptcha-checkbox-border"))).click()


# Waiting for CAPTCHA to be solved
time.sleep(10)
driver.switch_to.default_content()
# Locating the submit button and clicking on it
submit = driver.find_element(By.XPATH, '//*[@id="home_contact_us_form"]/div/div[1]/button')
submit.click()

time.sleep(10)
# Close the web browser
driver.quit()