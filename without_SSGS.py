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

piradi_nomeri = "00000002027"
sabutis_nomeri = "9000375"
teleponis_nomeri = "571135951"

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
time.sleep(4)

# REGISTER FLOW
# FIRST PAGE
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[1]/div[1]/form/div["
                              "1]/div[1]/input").send_keys("ზვიად")
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[1]/div[1]/form/div["
                              "1]/div[2]/input").send_keys("გამსახურდია")
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[1]/div[1]/form/div["
                              "1]/div[3]/input").send_keys({piradi_nomeri})

# CHOOSE DOC TYPE
dropdown_document_type = driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
                                                       "/main/div/as-customer-create/kendo-tabstrip/div["
                                                       "2]/as-customer-general/div/div/div[1]/div[1]/form/div[2]/div["
                                                       "1]/kendo-dropdownlist/button")

dropdown_document_type.click()
time.sleep(2)
# CHOOSE FROM DROPDOWN_DOC_TYPE
dropdown_document_type.send_keys(Keys.DOWN)
dropdown_document_type.send_keys(Keys.DOWN)

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

driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[1]/div[1]/form/div["
                              "2]/div[3]/input").send_keys({sabutis_nomeri})

# UPLOAD FILE driver.find_element(By.XPATH,
# "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer-create" "/kendo-tabstrip/div[
# 2]/as-customer-general/div/div/div[1]/div[2]/div[1]/button").click() time.sleep(3)
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[1]/div[2]/div["
                              "1]/button").click()
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[1]/div[2]/div["
                              "1]/div/kendo-popup/div/div/ufe-application-consent-form/input").send_keys(
    "C:\\Users\\b"
    ".bitarashvili"
    "\\Desktop\\UFE"
    "\\Freeze.png")
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[1]/div[2]/div["
                              "1]/div/kendo-popup/div/div/ufe-application-consent-form/div[2]/button[1]").click()
# სგს BUTTON
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[1]/div[2]/div["
                              "2]/div/button").click()
time.sleep(5)
# # CLOSE ERROR MESSAGE
driver.find_element(By.XPATH, "/html/body/ufe-root/div/as-dialog/div/ufe-base-dialog/div/div/div/div[1]/div/"
                              "button").click()

# SCROLL PAGE DOWN
driver.find_element(By.TAG_NAME, 'html').click()
i = 8
while i > 0:
    scroll_element = send_keys('{DOWN}')
    i -= 1
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[1]/div["
                              "1]/div[1]/div[1]/input").send_keys("ზვიად")
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[1]/div["
                              "1]/div[1]/div[2]/input").send_keys("გამსახურდია")
# FATHER NAME
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[1]/div["
                              "1]/div[1]/div[3]/input").send_keys("კონსტანტინე")
# PERSONAL NUMBER
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[1]/div["
                              "1]/div[1]/div[4]/input").send_keys({piradi_nomeri})

# BIRTHPLACE
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[1]/div["
                              "1]/div[2]/div[4]/input").send_keys("თბილისი")
# TRIPLE CLICK
elemento_to_triple_click = driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout"
                                                         "/div/main/div/as-customer-create/kendo-tabstrip/div["
                                                         "2]/as-customer-general/div/div/div[3]/form/div[1]/div["
                                                         "1]/div[3]/div[1]/kendo-datepicker/kendo-dateinput/input")
actions = ActionChains(driver)
actions.click(elemento_to_triple_click).click(elemento_to_triple_click).click(elemento_to_triple_click).perform()
time.sleep(3)

# CHOOSE DATE
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[1]/div["
                              "1]/div[3]/div[1]/kendo-datepicker/kendo-dateinput/input").send_keys("01012000")

dropdown_sex_type = driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main"
                                                  "/div/as-customer-create/kendo-tabstrip/div["
                                                  "2]/as-customer-general/div/div/div[3]/form/div[1]/div[1]/div["
                                                  "3]/div[2]/kendo-dropdownlist/button")

dropdown_sex_type.click()
time.sleep(2)
# CHOOSE FROM DROPDOWN_DOC_TYPE
dropdown_sex_type.send_keys(Keys.DOWN)
time.sleep(2)

# CHOOSE FAMILY STATUS
dropdown_family_type = driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
                                                     "/main/div/as-customer-create/kendo-tabstrip/div["
                                                     "2]/as-customer-general/div/div/div[3]/form/div[1]/div[1]/div["
                                                     "3]/div[3]/kendo-dropdownlist/button")

dropdown_family_type.click()
time.sleep(2)
# CHOOSE FROM DROPDOWN_DOC_TYPE
dropdown_family_type.send_keys(Keys.DOWN)
time.sleep(2)

# DROPDOWN BIRTH COUNTY
dropdown_cntr_type = driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main"
                                                   "/div/as-customer-create/kendo-tabstrip/div["
                                                   "2]/as-customer-general/div/div/div[3]/form/div[1]/div[1]/div["
                                                   "3]/div[4]/kendo-dropdownlist/button")

dropdown_cntr_type.click()
time.sleep(2)
# CHOOSE FROM DROPDOWN_DOC_TYPE
dropdown_cntr_type.send_keys(Keys.DOWN)
time.sleep(2)

# DROPDOWN DOCUMENT TYPE2
dropdown_doc_type = driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main"
                                                  "/div/as-customer-create/kendo-tabstrip/div["
                                                  "2]/as-customer-general/div/div/div[3]/form/div[1]/div[1]/div["
                                                  "4]/div[1]/kendo-dropdownlist/button")

dropdown_doc_type.click()
time.sleep(2)
# CHOOSE FROM DROPDOWN_DOC_TYPE
dropdown_doc_type.send_keys(Keys.DOWN)
dropdown_doc_type.send_keys(Keys.DOWN)
time.sleep(2)

driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[1]/div["
                              "1]/div[4]/div[2]/input").send_keys({sabutis_nomeri})
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[1]/div["
                              "1]/div[4]/div[3]/input").send_keys("იუსტიცია")
# TRIPLE CLICK FOR DATE
# გაცემის თარიღი
gacema_to_triple_click = driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
                                                       "/main/div/as-customer-create/kendo-tabstrip/div["
                                                       "2]/as-customer-general/div/div/div[3]/form/div[1]/div[1]/div["
                                                       "5]/div[1]/kendo-datepicker/kendo-dateinput/input")
actions = ActionChains(driver)
actions.click(gacema_to_triple_click).click(gacema_to_triple_click).click(gacema_to_triple_click).perform()
time.sleep(3)

# CHOOSE DATE
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
                              "/main/div/as-customer-create/kendo-tabstrip/div["
                              "2]/as-customer-general/div/div/div[3]/form/div[1]/div[1]/div["
                              "5]/div[1]/kendo-datepicker/kendo-dateinput/input").send_keys("01012020")

# ვადის გასვლის თარიღი
expire_to_triple_click = driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
                                                       "/main/div/as-customer-create/kendo-tabstrip/div["
                                                       "2]/as-customer-general/div/div/div[3]/form/div[1]/div[1]/div["
                                                       "5]/div[2]/kendo-datepicker/kendo-dateinput/input")
actions = ActionChains(driver)
actions.click(expire_to_triple_click).click(expire_to_triple_click).click(expire_to_triple_click).perform()
time.sleep(3)

# CHOOSE DATE
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
                              "/main/div/as-customer-create/kendo-tabstrip/div["
                              "2]/as-customer-general/div/div/div[3]/form/div[1]/div[1]/div["
                              "5]/div[2]/kendo-datepicker/kendo-dateinput/input").send_keys("01012026")

# SCROLL PAGE DOWN2
driver.find_element(By.TAG_NAME, 'html').click()
x = 12
while x > 0:
    scroll_element2 = send_keys('{DOWN}')
    x -= 1
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[3]/div/div["
                              "2]/div/div/div[2]/input").send_keys("საქართველო")
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[3]/div/div["
                              "2]/div/div/div[3]/input").send_keys("სოფელი ძველი")

driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[3]/div/div["
                              "4]/div/div/div[2]/input").send_keys("საქართველო")
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[3]/div/div["
                              "4]/div/div/div[3]/input").send_keys("სოფელი ძველი")
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[5]/div["
                              "1]/div/div[1]/input").send_keys({teleponis_nomeri})
z = 10
while z > 0:
    scroll_element2 = send_keys('{DOWN}')
    z -= 1
time.sleep(3)
# OTP BUTTON
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[5]/div["
                              "2]/div/button").click()
time.sleep(3)
# CLOSE OTP MESSAGE
driver.find_element(By.XPATH, "/html/body/ufe-root/div/as-dialog/div/ufe-base-dialog/div/div/div/div[1]/div/butto"
                              "n").click()
time.sleep(3)
print("პირველი სექცია წარმატებით შეივსო")

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

driver.find_element(By.TAG_NAME, 'html').click()
y = 13
while y > 0:
    scroll_element3 = send_keys('{DOWN}')
    y -= 1

# FATCA
dropdown_work_type = driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main"
                                                   "/div/as-customer-create/kendo-tabstrip/div["
                                                   "2]/as-customer-additional-info/div/div/form/div[5]/div/div["
                                                   "1]/div[2]/kendo-dropdownlist/button")
dropdown_work_type.click()
time.sleep(2)
dropdown_work_type.send_keys(Keys.DOWN)

# შემოსავლის წყარო
dropdown_income_source = driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
                                                       "/main/div/as-customer-create/kendo-tabstrip/div["
                                                       "2]/as-customer-additional-info/div/div/form/div[5]/div/div["
                                                       "1]/div[3]/kendo-dropdownlist/button")
dropdown_income_source.click()
time.sleep(2)
dropdown_income_source.send_keys(Keys.DOWN)

# წლიური ბრუნვა
dropdown_annual_income = driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
                                                       "/main/div/as-customer-create/kendo-tabstrip/div["
                                                       "2]/as-customer-additional-info/div/div/form/div[5]/div/div["
                                                       "2]/div[3]/kendo-dropdownlist/button")
dropdown_annual_income.click()
time.sleep(2)
dropdown_annual_income.send_keys(Keys.DOWN)

# ბოლო განახლების თარიღი
# element_to_triple_click = driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
#                                                         "/main/div/as-customer-create/kendo-tabstrip/div["
#                                                         "2]/as-customer-additional-info/div/div/form/div[5]/div/div["
#                                                         "3]/div/kendo-datepicker/kendo-dateinput/input")
# actions = ActionChains(driver)
# actions.click(element_to_triple_click).click(element_to_triple_click).click(element_to_triple_click).perform()
# time.sleep(3)
#
# driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
#                               "-create/kendo-tabstrip/div[2]/as-customer-additional-info/div/div/form/div[5]/div/div["
#                               "3]/div/kendo-datepicker/kendo-dateinput/input").send_keys("07122023")

# კლიკები
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-additional-info/div/div/form/div[5]/div/div["
                              "4]/div[2]/div/div[2]/input").click()
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-additional-info/div/div/form/div[5]/div/div["
                              "5]/div[2]/div/div[2]/input").click()
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-additional-info/div/div/form/div[5]/div/div["
                              "6]/div[2]/div/div[2]/input").click()
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-additional-info/div/div/form/div[5]/div/div["
                              "7]/div[2]/div/div[2]/input").click()
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-additional-info/div/div/form/div[5]/div/div["
                              "8]/div[2]/div/div[2]/input").click()
time.sleep(4)
print("მეორე სექცია წარმატებით შეივსო")

# THIRD PAGE
# ATTRIBUTES
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[1]/ul/li[3]/span").click()
time.sleep(3)
# საქმიანობის სფერო

dropdown_attr_work = driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main"
                                                   "/div/as-customer"
                                                   "-create/kendo-tabstrip/div["
                                                   "2]/as-customer-attributes/form/div/div/div[1]/div["
                                                   "1]/kendo-dropdownlist/button")
dropdown_attr_work.click()
time.sleep(2)
dropdown_attr_work.send_keys(Keys.DOWN)

# ბიზნეს ქალაქი
dropdown_attr_city = driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main"
                                                   "/div/as-customer-create/kendo-tabstrip/div["
                                                   "2]/as-customer-attributes/form/div/div/div[1]/div["
                                                   "2]/kendo-dropdownlist/button")
dropdown_attr_city.click()
time.sleep(2)
dropdown_attr_city.send_keys(Keys.DOWN)

# შემოსავალი
dropdown_attr_income = driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
                                                     "/main/div/as-customer-create/kendo-tabstrip/div["
                                                     "2]/as-customer-attributes/form/div/div/div[2]/div["
                                                     "1]/kendo-dropdownlist/button")
dropdown_attr_income.click()
time.sleep(2)
dropdown_attr_income.send_keys(Keys.DOWN)

# ინფორმაციის წყარო
dropdown_attr_info = driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main"
                                                   "/div/as-customer-create/kendo-tabstrip/div["
                                                   "2]/as-customer-attributes/form/div/div/div[2]/div["
                                                   "2]/kendo-dropdownlist/button")
dropdown_attr_info.click()
time.sleep(2)
dropdown_attr_info.send_keys(Keys.DOWN)

# ადგილობრივი სტატუსი
dropdown_attr_status = driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
                                                     "/main/div/as-customer-create/kendo-tabstrip/div["
                                                     "2]/as-customer-attributes/form/div/div/div[3]/div["
                                                     "1]/kendo-dropdownlist/button")
dropdown_attr_status.click()
time.sleep(2)
dropdown_attr_status.send_keys(Keys.DOWN)

# საცხოვრებელი სტატუსი
dropdown_attr_home = driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main"
                                                   "/div/as-customer-create/kendo-tabstrip/div["
                                                   "2]/as-customer-attributes/form/div/div/div[3]/div["
                                                   "2]/kendo-dropdownlist/button")
dropdown_attr_home.click()
time.sleep(2)
dropdown_attr_home.send_keys(Keys.DOWN)

# business address
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-attributes/form/div/div/div[1]/div["
                              "3]/input").send_keys("აბასთუმანი")
print("მესამე სექცია წარმატებით შეივსო")

# FOURTH PAGE
# FILES PAGE
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[1]/ul/li[4]/span").click()
time.sleep(2)

# პირადობის ატვირთვა
dropdown_upload_id = driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main"
                                                   "/div/as-customer-create/kendo-tabstrip/div["
                                                   "2]/as-customer-attachments/div/div/div[3]/div["
                                                   "1]/ufe-attachment-upload/form/div[3]/div[2]/select/option[2]")
dropdown_upload_id.click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-attachments/div/div/div[3]/div["
                              "1]/ufe-attachment-upload/form/input").send_keys(
    "C:\\Users\\b"
    ".bitarashvili"
    "\\Desktop"
    "\\prof_image.jpg")

driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/kendo-tabstrip/div[2]/as-customer-attachments/div/div/div[3]/div["
                              "1]/ufe-attachment-upload/form/div[1]/ufe-ufe-toolbar/div[2]/button").click()
time.sleep(5)
# REGISTER BUTTON CLICK
driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                              "-create/div/div/button").click()

