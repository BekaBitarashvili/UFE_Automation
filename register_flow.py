import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.implicitly_wait(3)
driver.get("https://ufe-int.crystal.ge")
driver.maximize_window()
time.sleep(3)


# TRY LOGIN
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/main/div/div[2]/form/div[1]/input").send_keys("demnag")
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/main/div/div[2]/form/div[2]/input").send_keys("123ASDasd@")
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/main/div/div[2]/form/div[5]/button").click()
print("TEST PASSED")