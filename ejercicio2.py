from selenium import  webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://dev.keepworking.online/")
driver.find_element(By.CSS_SELECTOR, "body > app-root > app-main-home > app-nav-bar > nav > div.options-menu > div > div.options-menu__loginwrap.options-menu__wrapper--item > button").click()
usuario = driver.find_element(By.CSS_SELECTOR, "#input-loginUser")
usuario.send_keys("dylan.ariza@insoftar.com")
time.sleep(3)
clave = driver.find_element(By.CSS_SELECTOR, "#input-password")
clave.send_keys("m0N0CuC0#")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "body > ngb-modal-window > div > div > app-login > div > div > form > div.btnInic > button").click()
time.sleep(5)
driver.close()