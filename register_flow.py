import time

from pywinauto.keyboard import send_keys
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
time.sleep(3)

# REGISTER BUTTON
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/ufe-customer"
                              "-list/a").click()
time.sleep(4)

# REGISTER FLOW
# FIRST PAGE
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[1]/div[1]/form/div["
                              "1]/div[1]/input").send_keys("აკაკი")
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[1]/div[1]/form/div["
                              "1]/div[2]/input").send_keys("წერეთელი")
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[1]/div[1]/form/div["
                              "1]/div[3]/input").send_keys("98765432100")
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[1]/div[1]/form/div["
                              "2]/div[1]/input").send_keys("123")

# TRIPLE CLICK
element_to_triple_click = driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
                                                        "/main/div/as-customer-create/kendo-tabstrip/div["
                                                        "2]/as-customer-general/div/div/div[1]/div[1]/form/div["
                                                        "2]/div[2]/kendo-datepicker/kendo-dateinput/input")
actions = ActionChains(driver)
actions.click(element_to_triple_click).click(element_to_triple_click).click(element_to_triple_click).perform()
time.sleep(3)

# CHOOSE DATE
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
                              "/main/div/as-customer-create/kendo-tabstrip/div["
                              "2]/as-customer-general/div/div/div[1]/div[1]/form/div["
                              "2]/div[2]/kendo-datepicker/kendo-dateinput/input").send_keys("01012000")
# UPLOAD FILE
# driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer-create"
#                               "/kendo-tabstrip/div[2]/as-customer-general/div/div/div[1]/div[2]/div[1]/button").click()
# time.sleep(3)
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[1]/div[2]/div["
                              "1]/input").send_keys("C:\\Users\\b"
                                                    ".bitarashvili"
                                                    "\\Desktop\\UFE"
                                                    "\\Freeze.png")
# სგს BUTTON
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[1]/div[2]/div["
                              "2]/button").click()
time.sleep(3)
# CLOSE ERROR MESSAGE
driver.find_element(By.XPATH, "/html/body/ufe-root/div/as-dialog/div/ufe-base-dialog/div/div/div/div["
                              "2]/ufe-danger-dialog/div[2]/div/button").click()
# SCROLL PAGE DOWN
driver.find_element(By.TAG_NAME, 'html').click()
i = 8
while i > 0:
    achi = send_keys('{DOWN}')
    i -= 1

