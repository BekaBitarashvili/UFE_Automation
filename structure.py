import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def login(driver):
    driver.get("https://ufe-int.crystal.ge")
    driver.maximize_window()
    time.sleep(3)

    username = "ALEXANDREB"
    password = "12345678"

    driver.find_element(By.XPATH, "/html/body/div[2]/main/div/main/div/div[2]/form/div[1]/input").send_keys(username)
    driver.find_element(By.XPATH, "/html/body/div[2]/main/div/main/div/div[2]/form/div[2]/input").send_keys(password)
    driver.find_element(By.XPATH, "/html/body/div[2]/main/div/main/div/div[2]/form/div[5]/button").click()
    print("Logged in successfully")
    time.sleep(3)


def register_user(driver, piradi_nomeri, sabutis_nomeri, teleponis_nomeri):
    # Your registration process here...
    pass


def scroll_page(driver, scrolls):
    body = driver.find_element(By.TAG_NAME, 'html')
    for _ in range(scrolls):
        body.send_keys(Keys.DOWN)
        time.sleep(0.5)


def run_automation():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(3)

    piradi_nomeri = "00000002027"
    sabutis_nomeri = "9000375"
    teleponis_nomeri = "571135951"

    login(driver)
    register_user(driver, piradi_nomeri, sabutis_nomeri, teleponis_nomeri)

    # Continue with the rest of your automation steps...
    # Example:
    # scroll_page(driver, 8)
    # perform_other_actions(driver)

    driver.quit()


if __name__ == "__main__":
    run_automation()
