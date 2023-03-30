from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--allow-insecure-localhost') # differ on driver version. can ignore.
caps = options.to_capabilities()
caps["acceptInsecureCerts"] = True
driver = webdriver.Chrome(desired_capabilities=caps)
driver.get('https://reiko-store.com/images/products/4279.jpg')
driver.save_screenshot("reiko.png")

driver.quit()
