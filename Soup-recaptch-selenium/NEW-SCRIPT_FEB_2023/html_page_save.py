import pyautogui
from selenium import webdriver
import time
d = webdriver.Chrome()
d.get('https://www.grainger.com/product/WOOSTER-Anti-Slip-Tape-Very-Coarse-12E910')
pyautogui.hotkey('ctrl', 's')
time.sleep(5)
pyautogui.typewrite('grainger1' + '.html')
pyautogui.press('enter')
time.sleep(20)
d.close()