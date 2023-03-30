from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:/chromedriver.exe")

driver.maximize_window()

driver.get('https://www.grainger.com/search/fasteners/bolts/hex-head-bolts/standard-hex-head-cap-screws?filters=webParentSkuKey&webParentSkuKey=WP13467676&gwwRemoveElement=true')
hotels = wait(driver, 15).until(EC.presence_of_all_elements_located((By.CLASS_NAME, '_3OJ8zd')))
print(len(hotels))

while True:
    # Scroll down to last name in list
    driver.execute_script('arguments[0].scrollIntoView();', hotels[-1])
    try:
        # Wait for more names to be loaded
        wait(driver, 15).until(lambda driver: len(wait(driver, 15).until(EC.presence_of_all_elements_located((By.CLASS_NAME, '_3OJ8zd')))) > len(hotels))
        # Update names list
        hotels = wait(driver, 15).until(EC.presence_of_all_elements_located((By.CLASS_NAME, '_3OJ8zd')))
    except:
        # Break the loop in case no new names loaded after page scrolled down
        break

# Print names list
print([hotel.text for hotel in hotels])