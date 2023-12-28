import unittest
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

piradi_nomeri = "00000002027"
sabutis_nomeri = "9000375"
teleponis_nomeri = "571135951"


class TestWebsite(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_experimental_option("detach", True)
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_01_login(self):
        self.driver.get("https://ufe-int.crystal.ge")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/main/div/main/div/div[2]/form/div[1]/input").send_keys(
            "ALEXANDREB")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/main/div/main/div/div[2]/form/div[2]/input").send_keys(
            "12345678")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/main/div/main/div/div[2]/form/div[5]/button").click()
        # assert "UFE" in self.driver.title

    def test_02_register_button(self):
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/ufe-customer"
                                 "-list/a").click()

        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[1]/div[1]/form/div["
                                 "1]/div[1]/input").send_keys("ზვიად")
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[1]/div[1]/form/div["
                                 "1]/div[2]/input").send_keys("გამსახურდია")
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[1]/div[1]/form/div["
                                 "1]/div[3]/input").send_keys({piradi_nomeri})
        dropdown_document_type = self.driver.find_element(By.XPATH,
                                                          "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
                                                          "/main/div/as-customer-create/kendo-tabstrip/div["
                                                          "2]/as-customer-general/div/div/div[1]/div[1]/form/div["
                                                          "2]/div["
                                                          "1]/kendo-dropdownlist/button")

        dropdown_document_type.click()
        time.sleep(2)
        # CHOOSE FROM DROPDOWN_DOC_TYPE
        dropdown_document_type.send_keys(Keys.DOWN)
        dropdown_document_type.send_keys(Keys.DOWN)

        # TRIPLE CLICK
        element_to_triple_click = self.driver.find_element(By.XPATH,
                                                           "/html/body/ufe-root/div/div/as-customers/ufe-body-layout"
                                                           "/div"
                                                           "/main/div/as-customer-create/kendo-tabstrip/div["
                                                           "2]/as-customer-general/div/div/div[1]/div[1]/form/div["
                                                           "2]/div[2]/kendo-datepicker/kendo-dateinput/input")
        actions = ActionChains(self.driver)
        actions.click(element_to_triple_click).click(element_to_triple_click).click(element_to_triple_click).perform()
        time.sleep(3)

        # CHOOSE DATE
        self.driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
                                           "/main/div/as-customer-create/kendo-tabstrip/div["
                                           "2]/as-customer-general/div/div/div[1]/div[1]/form/div["
                                           "2]/div[2]/kendo-datepicker/kendo-dateinput/input").send_keys("01012000")

        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[1]/div[1]/form/div["
                                 "2]/div[3]/input").send_keys({sabutis_nomeri})
        # თანხმობის ატვირთვა
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[1]/div[2]/div["
                                 "1]/button").click()
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[1]/div[2]/div["
                                 "1]/div/kendo-popup/div/div/ufe-application-consent-form/input").send_keys(
            "C:\\Users\\b"
            ".bitarashvili"
            "\\Desktop\\UFE"
            "\\Freeze.png")
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[1]/div[2]/div["
                                 "1]/div/kendo-popup/div/div/ufe-application-consent-form/div[2]/button[1]").click()
        # სგს BUTTON
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[1]/div[2]/div["
                                 "2]/div/button").click()
        time.sleep(5)
        # # CLOSE ERROR MESSAGE
        self.driver.find_element(By.XPATH, "/html/body/ufe-root/div/as-dialog/div/ufe-base-dialog/div/div/div/div["
                                           "1]/div/"
                                           "button").click()

    def test_03_scroll_page1(self):
        self.driver.find_element(By.TAG_NAME, 'html').click()
        i = 8
        while i > 0:
            send_keys('{DOWN}')
            i -= 1
        time.sleep(2)

    def test_04_main_info(self):
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[1]/div["
                                 "1]/div[1]/div[1]/input").send_keys("აკაკი")
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[1]/div["
                                 "1]/div[1]/div[2]/input").send_keys("წერეთელი")
        # FATHER NAME
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[1]/div["
                                 "1]/div[1]/div[3]/input").send_keys("კონსტანტინე")
        # PERSONAL NUMBER
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[1]/div["
                                 "1]/div[1]/div[4]/input").send_keys({piradi_nomeri})

        # BIRTHPLACE
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[1]/div["
                                 "1]/div[2]/div[4]/input").send_keys("თბილისი")
        # TRIPLE CLICK
        elemento_to_triple_click = self.driver.find_element(By.XPATH,
                                                            "/html/body/ufe-root/div/div/as-customers/ufe-body-layout"
                                                            "/div/main/div/as-customer-create/kendo-tabstrip/div["
                                                            "2]/as-customer-general/div/div/div[3]/form/div[1]/div["
                                                            "1]/div[3]/div[1]/kendo-datepicker/kendo-dateinput/input")
        actions = ActionChains(self.driver)
        actions.click(elemento_to_triple_click).click(elemento_to_triple_click).click(
            elemento_to_triple_click).perform()
        time.sleep(1.5)

        # CHOOSE DATE
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[1]/div["
                                 "1]/div[3]/div[1]/kendo-datepicker/kendo-dateinput/input").send_keys("01012000")

        dropdown_sex_type = self.driver.find_element(By.XPATH,
                                                     "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main"
                                                     "/div/as-customer-create/kendo-tabstrip/div["
                                                     "2]/as-customer-general/div/div/div[3]/form/div[1]/div[1]/div["
                                                     "3]/div[2]/kendo-dropdownlist/button")

        dropdown_sex_type.click()
        time.sleep(1)
        # CHOOSE FROM DROPDOWN_DOC_TYPE
        dropdown_sex_type.send_keys(Keys.DOWN)
        time.sleep(1)

        # CHOOSE FAMILY STATUS
        dropdown_family_type = self.driver.find_element(By.XPATH,
                                                        "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
                                                        "/main/div/as-customer-create/kendo-tabstrip/div["
                                                        "2]/as-customer-general/div/div/div[3]/form/div[1]/div[1]/div["
                                                        "3]/div[3]/kendo-dropdownlist/button")

        dropdown_family_type.click()
        time.sleep(1)
        # CHOOSE FROM DROPDOWN_DOC_TYPE
        dropdown_family_type.send_keys(Keys.DOWN)
        time.sleep(1)

        # DROPDOWN BIRTH COUNTY
        dropdown_cntr_type = self.driver.find_element(By.XPATH,
                                                      "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
                                                      "/main"
                                                      "/div/as-customer-create/kendo-tabstrip/div["
                                                      "2]/as-customer-general/div/div/div[3]/form/div[1]/div[1]/div["
                                                      "3]/div[4]/kendo-dropdownlist/button")

        dropdown_cntr_type.click()
        time.sleep(1)
        # CHOOSE FROM DROPDOWN_DOC_TYPE
        dropdown_cntr_type.send_keys(Keys.DOWN)
        time.sleep(1)

        # DROPDOWN DOCUMENT TYPE2
        dropdown_doc_type = self.driver.find_element(By.XPATH,
                                                     "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main"
                                                     "/div/as-customer-create/kendo-tabstrip/div["
                                                     "2]/as-customer-general/div/div/div[3]/form/div[1]/div[1]/div["
                                                     "4]/div[1]/kendo-dropdownlist/button")

        dropdown_doc_type.click()
        time.sleep(1)
        # CHOOSE FROM DROPDOWN_DOC_TYPE
        dropdown_doc_type.send_keys(Keys.DOWN)
        dropdown_doc_type.send_keys(Keys.DOWN)
        time.sleep(1)

        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[1]/div["
                                 "1]/div[4]/div[2]/input").send_keys({sabutis_nomeri})
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[1]/div["
                                 "1]/div[4]/div[3]/input").send_keys("იუსტიცია")
        # TRIPLE CLICK FOR DATE
        # გაცემის თარიღი
        gacema_to_triple_click = self.driver.find_element(By.XPATH,
                                                          "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
                                                          "/main/div/as-customer-create/kendo-tabstrip/div["
                                                          "2]/as-customer-general/div/div/div[3]/form/div[1]/div["
                                                          "1]/div["
                                                          "5]/div[1]/kendo-datepicker/kendo-dateinput/input")
        actions = ActionChains(self.driver)
        actions.click(gacema_to_triple_click).click(gacema_to_triple_click).click(gacema_to_triple_click).perform()
        time.sleep(1.5)

        # CHOOSE DATE
        self.driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
                                           "/main/div/as-customer-create/kendo-tabstrip/div["
                                           "2]/as-customer-general/div/div/div[3]/form/div[1]/div[1]/div["
                                           "5]/div[1]/kendo-datepicker/kendo-dateinput/input").send_keys("01012020")

        # ვადის გასვლის თარიღი
        expire_to_triple_click = self.driver.find_element(By.XPATH,
                                                          "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
                                                          "/main/div/as-customer-create/kendo-tabstrip/div["
                                                          "2]/as-customer-general/div/div/div[3]/form/div[1]/div["
                                                          "1]/div["
                                                          "5]/div[2]/kendo-datepicker/kendo-dateinput/input")
        actions = ActionChains(self.driver)
        actions.click(expire_to_triple_click).click(expire_to_triple_click).click(expire_to_triple_click).perform()
        time.sleep(1.5)

        # CHOOSE DATE
        self.driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
                                           "/main/div/as-customer-create/kendo-tabstrip/div["
                                           "2]/as-customer-general/div/div/div[3]/form/div[1]/div[1]/div["
                                           "5]/div[2]/kendo-datepicker/kendo-dateinput/input").send_keys("01012026")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWebsite)
    unittest.TextTestRunner(verbosity=2).run(suite)
