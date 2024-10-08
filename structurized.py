import unittest
import time
import random, string
from telnetlib import EC

from faker import Faker
from selenium.webdriver.support.ui import Select
from pywinauto.keyboard import send_keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec, wait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

fake = Faker()

piradi_nomeri = str(random.randint(10000000000, 99999999999))
sabutis_nomeri = str(random.randint(10, 99)) + "ID" + str(random.randint(10000, 99999))
teleponis_nomeri = "555" + str(random.randint(100000, 999999))

georgian_letters = ['ა', 'ბ', 'გ', 'დ', 'ე', 'ვ', 'ზ', 'თ', 'ი', 'კ', 'ლ', 'მ', 'ნ', 'ო', 'პ', 'ჟ', 'რ', 'ს',
                    'ტ', 'უ', 'ფ', 'ქ', 'ღ', 'ყ', 'შ', 'ჩ', 'ც', 'ძ', 'წ', 'ჭ', 'ხ', 'ჯ', 'ჰ']


def generate_georgian_name(length=4):
    return ''.join(random.choice(georgian_letters) for _ in range(length))


def generate_georgian_surname(length=8):
    return ''.join(random.choice(georgian_letters) for _ in range(length))


saxeli = generate_georgian_name()
gvari = generate_georgian_surname()


# 01234567835 #01234567841 #01234567842 #01234567843 #01234567844 #01234567845- სსგს

class TestWebsite(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_experimental_option("detach", True)

        # chromedriver_path = "C:/Users/b.bitarashvili/Downloads/chromedriver_win64/chromedriver.exe"
        chromedriver_path = "C:/Users/b.bitarashvili/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
        service = Service(chromedriver_path)
        cls.driver = webdriver.Chrome(service=service, options=options)

        # cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_01_login(self):
        self.driver.get("https://ufe-int.crystal.ge")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/main/div/main/div/div[2]/form/div[1]/input").send_keys(
            "BEKAB")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/main/div/main/div/div[2]/form/div[2]/input").send_keys(
            "12345678")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/main/div/main/div/div[2]/form/div[5]/button").click()
        # assert "UFE" in self.driver.title

    def test_02_register_button(self):
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/ufe"
                                 "-customer-list/div[1]/button").click()

        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[1]/div[1]/form/div["
                                 "1]/div[1]/input").send_keys(saxeli)
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[1]/div[1]/form/div["
                                 "1]/div[2]/input").send_keys(gvari)
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[1]/div[1]/form/div["
                                 "1]/div[3]/input").send_keys(piradi_nomeri)
        dropdown_document_type = self.driver.find_element(By.XPATH,
                                                          "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
                                                          "/main/div/as-customer-create/kendo-tabstrip/div["
                                                          "2]/as-customer-general/div/div/div[1]/div[1]/form/div["
                                                          "2]/div["
                                                          "1]/kendo-dropdownlist/button")

        dropdown_document_type.click()
        time.sleep(2)
        # CHOOSE FROM DROPDOWN_DOC_TYPE
        for _ in range(8):
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
                                 "2]/div[3]/input").send_keys(sabutis_nomeri)
        # თანხმობის ატვირთვა
        # self.driver.find_element(By.XPATH,
        #                          "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
        #                          "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[1]/div[2]/div["
        #                          "1]/button").click()
        # self.driver.find_element(By.XPATH,
        #                          "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
        #                          "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[1]/div[2]/div["
        #                          "1]/div/kendo-popup/div/div/ufe-application-consent-form/input").send_keys(
        #     "C:\\Users\\b"
        #     ".bitarashvili"
        #     "\\Desktop\\UFE"
        #     "\\Freeze.png")
        # self.driver.find_element(By.XPATH,
        #                          "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
        #                          "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[1]/div[2]/div["
        #                          "1]/div/kendo-popup/div/div/ufe-application-consent-form/div[2]/button[1]").click()
        # სგს BUTTON
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[1]/div[2]/div["
                                 "2]/div/button").click()
        # wait until button is clickable
        wait.WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(
            (By.XPATH, "/html/body/ufe-root/div/as-dialog/div/ufe-base-dialog/div/div/div/div["
                       "1]/div/"
                       "button")))
        # # CLOSE ERROR MESSAGE
        self.driver.find_element(By.XPATH, "/html/body/ufe-root/div/as-dialog/div/ufe-base-dialog/div/div/div/div["
                                           "1]/div/"
                                           "button").click()
        time.sleep(3)

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
                                 "1]/div[1]/div[1]/input").send_keys(saxeli)
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[1]/div["
                                 "1]/div[1]/div[2]/input").send_keys(gvari)
        # FATHER NAME
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[1]/div["
                                 "1]/div[1]/div[3]/input").send_keys("გუჯა")
        # PERSONAL NUMBER
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[1]/div["
                                 "1]/div[1]/div[4]/input").send_keys(piradi_nomeri)

        # BIRTHPLACE
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[1]/div["
                                 "1]/div[2]/div[4]/input").send_keys("სართიჭალა")
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
        for _ in range(8):
            dropdown_doc_type.send_keys(Keys.DOWN)

        time.sleep(1)

        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[1]/div["
                                 "1]/div[4]/div[2]/input").send_keys(sabutis_nomeri)
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[1]/div["
                                 "1]/div[4]/div[3]/input").send_keys("იუსტიცია")
        # მოქალაქეობა

        # moqalaqe = self.driver.find_element(By.XPATH,"/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
        #                                              "/main/div/as-customer-create/kendo-tabstrip/div["
        #                                              "2]/as-customer-general/div/div/div[3]/form/div[1]/div[1]/div["
        #                                              "4]/div[4]/kendo-dropdownlist/button")
        # moqalaqe.click()
        # time.sleep(1)
        # moqalaqe.send_keys("iran")
        # time.sleep(1)
        # moqalaqe.send_keys(Keys.ENTER)

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

    def test_05_scroll_page2(self):
        self.driver.find_element(By.TAG_NAME, 'html').click()
        i = 12
        while i > 0:
            send_keys('{DOWN}')
            i -= 1
        time.sleep(2)

    def test_06_address1(self):
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[3]/div/div["
                                 "2]/div/div/div[2]/input").send_keys("სართიჭალა")
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[3]/div/div["
                                 "2]/div/div/div[3]/input").send_keys("სოფელი ძველი")

        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[3]/div/div["
                                 "4]/div/div/div[2]/input").send_keys("სართიჭალა")
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[3]/div/div["
                                 "4]/div/div/div[3]/input").send_keys("სოფელი ძველი")
        otpinput = self.driver.find_element(By.XPATH,
                                            "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as"
                                            "-customer"
                                            "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div["
                                            "3]/form/div[5]/div["
                                            "1]/div/div[1]/kendo-maskedtextbox/input")
        for _ in range(1):
            otpinput.click()
        otpinput.send_keys(teleponis_nomeri)
        time.sleep(3)

    # def test_07_scroll_page3(self):
    #     self.driver.find_element(By.TAG_NAME, 'html').click()
    #     i = 10
    #     while i > 0:
    #         send_keys('{DOWN}')
    #         i -= 1
    #     time.sleep(3)

    def test_08_otp(self):
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-general/div/div/div[3]/form/div[5]/div["
                                 "2]/div/button").click()
        time.sleep(10)
        # CLOSE OTP MESSAGE
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/as-dialog/div/ufe-base-dialog/div/div/div/div[1]/div/butto"
                                 "n").click()
        time.sleep(3)

    def test_09_types(self):
        # ADDITIONAL INFORMATION
        # mainpage = self.driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
        #                                               "/main/div/as-customer-create/kendo-tabstrip/div[1]/ul/li["
        #                                               "3]/span")
        # mainpage.click()
        # send_keys(Keys.LEFT)

        typespage = self.driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
                                                       "/main/div/as"
                                                       "-customer"
                                                       "-create/kendo-tabstrip/div[1]/ul/li[2]/span")
        typespage.click()
        time.sleep(1.5)

        # ქვეტიპი
        dropdown_qvetype = self.driver.find_element(By.XPATH,
                                                    "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
                                                    "/main/div/as-customer-create/kendo-tabstrip/div["
                                                    "2]/as-customer-additional-info/div/div/form/div[1]/div/div/div["
                                                    "2]/kendo-dropdownlist/button")
        dropdown_qvetype.click()
        time.sleep(2)
        # CHOOSE FROM DROPDOWN_QVE_TYPE
        dropdown_qvetype.send_keys(Keys.DOWN)
        time.sleep(2)

        # ტიპი/დარგი
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-additional-info/div/div/form/div["
                                 "1]/div/div/div[3]/div/div[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-additional-info/div/div/form/div["
                                 "1]/div/div/div[3]/div/kendo-popup/div/div/ufe-tree/div/div/div/div/input").send_keys(
            "ვაჭრობა")
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-additional-info/div/div/form/div["
                                 "1]/div/div/div[3]/div/kendo-popup/div/div/ufe-tree/div/div/div/ufe-tree-selector["
                                 "1]/div/li/ul/ufe-tree-selector/div/li/ul/ufe-tree-selector/div/li/div/div/label"
                                 "/input").click()

    def test_10_scroll_page4(self):
        self.driver.find_element(By.TAG_NAME, 'html').click()
        i = 13
        while i > 0:
            send_keys('{DOWN}')
            i -= 1
        time.sleep(2)

    def test_11_fatca(self):
        dropdown_work_type = self.driver.find_element(By.XPATH,
                                                      "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
                                                      "/main"
                                                      "/div/as-customer-create/kendo-tabstrip/div["
                                                      "2]/as-customer-additional-info/div/div/form/div[5]/div/div["
                                                      "1]/div[2]/kendo-dropdownlist/button")
        dropdown_work_type.click()
        time.sleep(2)
        dropdown_work_type.send_keys(Keys.DOWN)

        # შემოსავლის წყარო
        dropdown_income_source = self.driver.find_element(By.XPATH,
                                                          "/html/body/ufe-root/div/div/as-customers/ufe-body-layout"
                                                          "/div/main/div/as-customer-create/kendo-tabstrip/div["
                                                          "2]/as-customer-additional-info/div/div/form/div["
                                                          "5]/div/div[1]/div[3]/kendo-dropdownlist/button")
        dropdown_income_source.click()
        time.sleep(2)
        dropdown_income_source.send_keys(Keys.DOWN)

        # წლიური ბრუნვა
        dropdown_annual_income = self.driver.find_element(By.XPATH,
                                                          "/html/body/ufe-root/div/div/as-customers/ufe-body-layout"
                                                          "/div/main/div/as-customer-create/kendo-tabstrip/div["
                                                          "2]/as-customer-additional-info/div/div/form/div["
                                                          "5]/div/div[2]/div[3]/kendo-dropdownlist/button")
        dropdown_annual_income.click()
        time.sleep(2)
        dropdown_annual_income.send_keys(Keys.DOWN)

    def test_12_clicks(self):
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-additional-info/div/div/form/div["
                                 "5]/div/div[4]/div[2]/div/div[2]/input").click()
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-additional-info/div/div/form/div["
                                 "5]/div/div[5]/div[2]/div/div[2]/input").click()
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-additional-info/div/div/form/div["
                                 "5]/div/div[6]/div[2]/div/div[2]/input").click()
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-additional-info/div/div/form/div["
                                 "5]/div/div[7]/div[2]/div/div[2]/input").click()
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-additional-info/div/div/form/div["
                                 "5]/div/div[8]/div[2]/div/div[2]/input").click()
        time.sleep(3)
        self.driver.find_element(By.TAG_NAME, 'html').click()
        i = 13
        while i > 0:
            send_keys('{UP}')
            i -= 1
        time.sleep(2)

    def test_13_attributes(self):
        self.driver.find_element(By.XPATH, "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as"
                                           "-customer-create/kendo-tabstrip/div[1]/ul/li[3]/span").click()
        time.sleep(3)
        # საქმიანობის სფერო

        dropdown_attr_work = self.driver.find_element(By.XPATH,
                                                      "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
                                                      "/main/div/as-customer-create/kendo-tabstrip/div["
                                                      "2]/as-customer-attributes/div/div/div/div/form/div/div/div["
                                                      "1]/div[1]/kendo-dropdownlist/button")
        dropdown_attr_work.click()
        time.sleep(1.5)
        dropdown_attr_work.send_keys(Keys.DOWN)

        # ბიზნეს ქალაქი
        dropdown_attr_city = self.driver.find_element(By.XPATH,
                                                      "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
                                                      "/main/div/as-customer-create/kendo-tabstrip/div["
                                                      "2]/as-customer-attributes/div/div/div/div/form/div/div/div["
                                                      "1]/div[2]/kendo-dropdownlist/button")
        dropdown_attr_city.click()
        time.sleep(1.5)
        dropdown_attr_city.send_keys(Keys.DOWN)

        # შემოსავალი
        dropdown_attr_income = self.driver.find_element(By.XPATH,
                                                        "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
                                                        "/main/div/as-customer-create/kendo-tabstrip/div["
                                                        "2]/as-customer-attributes/div/div/div/div/form/div/div/div["
                                                        "2]/div[1]/kendo-dropdownlist/button")
        dropdown_attr_income.click()
        time.sleep(1.5)
        dropdown_attr_income.send_keys(Keys.DOWN)

        # ინფორმაციის წყარო
        dropdown_attr_info = self.driver.find_element(By.XPATH,
                                                      "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
                                                      "/main/div/as-customer-create/kendo-tabstrip/div["
                                                      "2]/as-customer-attributes/div/div/div/div/form/div/div/div["
                                                      "2]/div[2]/kendo-dropdownlist/button")
        dropdown_attr_info.click()
        time.sleep(1.5)
        dropdown_attr_info.send_keys(Keys.DOWN)

        # ადგილობრივი სტატუსი
        dropdown_attr_status = self.driver.find_element(By.XPATH,
                                                        "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
                                                        "/main/div/as-customer-create/kendo-tabstrip/div["
                                                        "2]/as-customer-attributes/div/div/div/div/form/div/div/div["
                                                        "3]/div[1]/kendo-dropdownlist/button")
        dropdown_attr_status.click()
        time.sleep(1.5)
        dropdown_attr_status.send_keys(Keys.DOWN)

        # საცხოვრებელი სტატუსი
        dropdown_attr_home = self.driver.find_element(By.XPATH,
                                                      "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
                                                      "/main/div/as-customer-create/kendo-tabstrip/div["
                                                      "2]/as-customer-attributes/div/div/div/div/form/div/div/div["
                                                      "3]/div[2]/kendo-dropdownlist/button")
        dropdown_attr_home.click()
        time.sleep(1.5)
        dropdown_attr_home.send_keys(Keys.DOWN)

        # business address
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div["
                                 "2]/as-customer-attributes/div/div/div/div/form/div/div/div[1]/div["
                                 "3]/input").send_keys("აბასთუმანი")

    def test_14_files(self):
        # FILES PAGE
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[1]/ul/li[4]/span").click()
        time.sleep(1.5)

        # პირადობის ატვირთვა
        dropdown_upload_id = self.driver.find_element(By.XPATH,
                                                      "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div"
                                                      "/main"
                                                      "/div/as-customer-create/kendo-tabstrip/div["
                                                      "2]/as-customer-attachments/div/div/div[3]/div["
                                                      "1]/ufe-attachment-upload/form/div[3]/div[2]/select/option[2]")
        dropdown_upload_id.click()
        time.sleep(1.5)
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-attachments/div/div/div[3]/div["
                                 "1]/ufe-attachment-upload/form/input").send_keys(
            "C:\\Users\\b"
            ".bitarashvili"
            "\\Desktop"
            "\\default.jpg")

        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/kendo-tabstrip/div[2]/as-customer-attachments/div/div/div[3]/div["
                                 "1]/ufe-attachment-upload/form/div[1]/ufe-ufe-toolbar/div[2]/button").click()
        time.sleep(2)

    def test_15_register_button(self):
        # REGISTER BUTTON
        self.driver.find_element(By.XPATH,
                                 "/html/body/ufe-root/div/div/as-customers/ufe-body-layout/div/main/div/as-customer"
                                 "-create/div/div/button").click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWebsite)
    unittest.TextTestRunner(verbosity=2).run(suite)
