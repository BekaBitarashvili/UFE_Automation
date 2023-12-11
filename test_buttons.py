import time

from selenium.webdriver.support.ui import Select
from pywinauto.keyboard import send_keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
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
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/main/div/div[2]/form/div[1]/input").send_keys("ALEXANDREB")
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/main/div/div[2]/form/div[2]/input").send_keys("12345678")
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/main/div/div[2]/form/div[5]/button").click()
print("TEST PASSED")
time.sleep(3)

# REGISTER BUTTON
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/ufe-customer"
                              "-list/a").click()

# SECOND PAGE
# ADDITIONAL INFORMATION
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[1]/ul/li[2]/span").click()

# ქვეტიპი
dropdown_qvetype = driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main"
                                                 "/div/as-customer-create/kendo-tabstrip/div["
                                                 "2]/as-customer-additional-info/div/div/form/div[1]/div/div/div["
                                                 "2]/kendo-dropdownlist/button")
dropdown_qvetype.click()
time.sleep(2)
# CHOOSE FROM DROPDOWN_QVE_TYPE
dropdown_qvetype.send_keys(Keys.DOWN)
time.sleep(2)

# ტიპი/დარგი
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-additional-info/div/div/form/div["
                              "1]/div/div/div[3]/div/div[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-additional-info/div/div/form/div["
                              "1]/div/div/div[3]/div/kendo-popup/div/div/ufe-tree/div/div/div/div/input").send_keys(
    "ვაჭრობა")
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-additional-info/div/div/form/div["
                              "1]/div/div/div[3]/div/kendo-popup/div/div/ufe-tree/div/div/div/ufe-tree-selector["
                              "1]/div/li/ul/ufe-tree-selector/div/li/ul/ufe-tree-selector/div/li/div/div/label/input"
                              "").click()

time.sleep(3)