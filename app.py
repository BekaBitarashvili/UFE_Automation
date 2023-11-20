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


# CHANGE LANGUAGE
driver.find_element(By.XPATH, "/html/body/div[1]/a[1]").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[1]/a[2]").click()
time.sleep(3)

# TRY LOGIN
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/main/div/div[2]/form/div[1]/input").send_keys("demnag")
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/main/div/div[2]/form/div[2]/input").send_keys("123ASDasd@")
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/main/div/div[2]/form/div[5]/button").click()
print("TEST PASSED")
# TRY SEARCH NAME & SURNAME
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/aside/div["
                              "2]/div/ufe-customer-filter/div/div/form/div[1]/div/input").send_keys("be ka")
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/aside/div["
                              "2]/div/ufe-customer-filter/div/div/form/div[6]/button").click()
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/aside/div["
                              "2]/div/ufe-customer-filter/div/div/form/div[1]/div/input").send_keys("თამაზი ფილიშვილი")
time.sleep(2)
# TRY SEARCH ID
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/aside/div["
                              "2]/div/ufe-customer-filter/div/div/form/div[2]/div/input").send_keys("01005035489")
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/aside/div["
                              "2]/div/ufe-customer-filter/div/div/form/div[3]/div/input").send_keys("35")
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/aside/div["
                              "2]/div/ufe-customer-filter/div/div/form/div[4]/div/input").send_keys("598926660")
time.sleep(4)
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/aside/div["
                              "2]/div/ufe-customer-filter/div/div/form/div[6]/button").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/aside/div["
                              "2]/div/ufe-customer-filter/div/div/form/div[2]/div/input").send_keys("01005035489")
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/aside/div["
                              "2]/div/ufe-customer-filter/div/div/form/div[6]/div").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/ufe-customer"
                              "-list/div[2]/a").click()
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/ufe-customer-profile/ufe-body-layout/div/main/div/ufe-loan"
                              "-list/div[2]/div[1]/ufe-list-container/div[1]/div/div/label/input").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/ufe-customer-profile/ufe-body-layout/div/main/div/ufe-loan"
                              "-list/div[2]/div[1]/ufe-list-container/div[1]/div/div/label/input").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/ufe-customer-profile/ufe-body-layout/div/main/div/ufe-loan"
                              "-list/div[2]/div[2]/ufe-list-container/div[1]/div/div/label/input").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/ufe-customer-profile/ufe-body-layout/div/main/div/ufe-loan"
                              "-list/div[2]/div[2]/ufe-list-container/div[1]/div/div/label/input").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/ufe-customer-profile/ufe-body-layout/div/aside/div["
                              "2]/div/ul[1]/li[1]/div").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/ufe-customer-profile/ufe-body-layout/div/aside/div["
                              "2]/div/ul[1]/li[1]/ul/li[1]/a").click()
time.sleep(3)
# scroll to bottom
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/ufe-customer-profile/ufe-body-layout/div/main/div/as"
                              "-profile-details/kendo-tabstrip/div[1]/ul/li[2]/span").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/ufe-customer-profile/ufe-body-layout/div/main/div/as"
                              "-profile-details/kendo-tabstrip/div[1]/ul/li[3]/span").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/ufe-customer-profile/ufe-body-layout/div/main/div/as"
                              "-profile-details/kendo-tabstrip/div[1]/ul/li[4]/span").click()
time.sleep(4)
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/ufe-customer-profile/ufe-body-layout/div/main/div/as"
                              "-profile-details/kendo-tabstrip/div[1]/ul/li[1]/span").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/ufe-customer-profile/ufe-body-layout/div/aside/div["
                              "2]/div/ul[1]/li[1]/ul/li[2]/a").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/ufe-root/div/as-dialog/div/ufe-base-dialog/div/div/div/div[1]/div/"
                              "button").click()
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/ufe-customer-profile/ufe-body-layout/div/aside/div["
                              "2]/div/ul[1]/li[1]/ul/li[3]/a").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/ufe-root/div/as-dialog/div/ufe-base-dialog/div/div/div/div[1]/div/"
                              "button").click()
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/ufe-customer-profile/ufe-body-layout/div/aside/div["
                              "2]/div/ul[1]/li[2]/a").click()
# LOAN LIST AUTOMATION
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/ufe-customer-profile/ufe-body-layout/div/main/div/ufe-loan"
                              "-list/div[2]/div[1]/ufe-list-container/div[2]/div/div[1]/div/a").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/ufe-customer-profile/ufe-body-layout/div/main/div/ufe-loan"
                              "-detail/kendo-tabstrip/div[1]/ul/li[2]/span").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/ufe-customer-profile/ufe-body-layout/div/main/div/ufe-loan"
                              "-detail/kendo-tabstrip/div[2]/ufe-schedule/div/div/label/input").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/ufe-customer-profile/ufe-body-layout/div/main/div/ufe-loan"
                              "-detail/kendo-tabstrip/div[1]/ul/li[3]/span").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/ufe-customer-profile/ufe-body-layout/div/main/div/ufe-loan"
                              "-detail/kendo-tabstrip/div[1]/ul/li[4]/span").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/ufe-customer-profile/ufe-body-layout/div/main/div/ufe-loan"
                              "-detail/kendo-tabstrip/div["
                              "2]/ufe-debt-details/div/ufe-date-picker/div/div/tet-date-picker/div/kendo-datepicker"
                              "/button").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/ufe-customer-profile/ufe-body-layout/div/main/div/ufe-loan"
                              "-detail/kendo-tabstrip/div["
                              "2]/ufe-debt-details/div/ufe-date-picker/div/div/tet-date-picker/div/kendo-datepicker"
                              "/button").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/ufe-root/div/ufe-app-header/header/div/div[1]/ul/li/a/span").click()

# LOG OUT
driver.find_element(By.XPATH, "/html/body/ufe-root/div/ufe-app-header/header/div/div[2]/button").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/ufe-root/div/ufe-app-header/header/div/div[2]/ul/li/a").click()
time.sleep(5)
driver.close()
