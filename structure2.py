import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

from without_SSGS import driver


class UfeRegistration:
    def __init__(self):
        self.options = Options()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)

    def login(self, username, password):
        self.driver.get("https://ufe-int.crystal.ge")
        driver.find_element(By.XPATH, "/html/body/div[2]/main/div/main/div/div[2]/form/div[1]/input").send_keys(
            "ALEXANDREB")
        driver.find_element(By.XPATH, "/html/body/div[2]/main/div/main/div/div[2]/form/div[2]/input").send_keys(
            "12345678")
        driver.find_element(By.XPATH, "/html/body/div[2]/main/div/main/div/div[2]/form/div[5]/button").click()
        print("TEST PASSED")
        time.sleep(3)

    def register(self, piradi_nomeri, sabutis_nomeri, teleponis_nomeri):
        # Your registration process here
        time.sleep(3)

    def quit_driver(self):
        self.driver.quit()


if __name__ == "__main__":
    ufe_reg = UfeRegistration()
    ufe_reg.login("ALEXANDREB", "12345678")
    ufe_reg.register("00000002027", "9000375", "571135951")
    ufe_reg.quit_driver()
