from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="D:\chromedriver\chromedriver")
driver.get("https://www3.animeflv.net/")

driver.maximize_window()

bus = driver.find_element_by_id("search-anime")
bus.send_keys("Tate no Yuusha no Nariagari")
bus.send_keys(Keys.ENTER)