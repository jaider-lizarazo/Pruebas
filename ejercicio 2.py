from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="D:\chromedriver\chromedriver")
driver.get("https://gmail.com")

usuario = driver.find_element_by_id("identifierId")
usuario.send_keys("jaider.lizarazo@insoftar.com")
usuario.send_keys(Keys.ENTER)
time.sleep(3)

clave = driver.find_element_by_name("password")
clave.send_keys("tucontraseñapersonal")
clave.send_keys(Keys.ENTER)







