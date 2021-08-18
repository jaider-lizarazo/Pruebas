from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\chromedriver\chromedriver")
driver.get("http://pyton.org")
driver.close()

