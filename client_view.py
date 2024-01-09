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

piradi_nomeri = "00000002031"
sabutis_nomeri = "98234234"
teleponis_nomeri = "571135953"


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

