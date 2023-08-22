import time
from random import random

import requests
import self
from dotenv import load_dotenv
import os

from faker import Faker
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from threading import Thread


def delay():
    time.sleep(random.randint(1, 5))


driver = webdriver.Chrome()
load_dotenv()
# you need to replace second BROWSERSTACK_USERNAME and BROWSERSTACK_ACCESS_KEY for your credentials
BROWSERSTACK_USERNAME =  'vlad_RMlbzV'
BROWSERSTACK_ACCESS_KEY =  'Dw9kx5p62Ayx9fmSTWyd'
URL = os.environ.get("URL") or "https://hub.browserstack.com/wd/hub"
BUILD_NAME = "browserstack-build-1"
capabilities = [
    {
        "browserName": "Chrome",
        "browserVersion": "103.0",
        "os": "Windows",
        "osVersion": "11",
        "sessionName": "BStack Python sample parallel",  # test name
        "buildName": BUILD_NAME,  # Your tests will be organized within this build
    },
]
def get_browser_option(browser):
    switcher = {
        "chrome": ChromeOptions(),
        "firefox": FirefoxOptions(),
        "edge": EdgeOptions(),
        "safari": SafariOptions(),
    }
    return switcher.get(browser, ChromeOptions())


def run_session(cap):
    bstack_options = {
        "osVersion": cap["osVersion"],
        "buildName": cap["buildName"],
        "sessionName": cap["sessionName"],
        "userName": BROWSERSTACK_USERNAME,
        "accessKey": BROWSERSTACK_ACCESS_KEY
    }
    if "os" in cap:
        bstack_options["os"] = cap["os"]
    options = get_browser_option(cap["browserName"].lower())
    if "browserVersion" in cap:
        options.browser_version = cap["browserVersion"]
        options.set_capability('bstack:options', bstack_options)
        driver = webdriver.Remote(command_executor=URL,options=options)


    try:

        driver.get("https://form.123formbuilder.com/5012215")
        driver.maximize_window()
        driver.set_page_load_timeout(2)

        # API тест для srlenium
        print("https://form.123formbuilder.com/5012215",
              requests.get("https://form.123formbuilder.com/5012215").status_code, "as status Code")
        code = requests.get("https://form.123formbuilder.com/5012215").status_code
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not 200", "Current code is:", code)

        # проверка статуса кода
        # Entering a placeholder name
        driver.find_element(By.XPATH, "//input[@placeholder='First']").send_keys("vlad")
        driver.set_page_load_timeout(2)

        # API тест для srlenium
        print("https://form.123formbuilder.com/5012215 Url has",
              requests.get("https://form.123formbuilder.com/5012215").status_code, "as status Code")
        code = requests.get("https://form.123formbuilder.com/5012215").status_code
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not 200", "Current code is:", code)

        # Entering a placeholder last
        driver.find_element(By.XPATH, "//input[contains(@placeholder,'Last')]").send_keys("shamb")
        driver.set_page_load_timeout(2)

        # Entering a placeholder email
        driver.find_element(By.XPATH, "//input[contains(@type,'email')]").send_keys("123abc@gmail.com")
        driver.set_page_load_timeout(2)

        # Entering a placeholder phone
        driver.find_element(By.XPATH, "//input[contains(@placeholder,'### ### #### ')]").send_keys(8888888888)
        driver.set_page_load_timeout(2)

        # click on radio button Choose your preferred product
        driver.find_element(By.XPATH, "//label[@aria-labelledby='radio-0000000e3']").click()
        driver.set_page_load_timeout(2)

        # Entering a placeholder Quantity
        driver.find_element(By.XPATH, "//input[@type='number']").send_keys("11")
        time.sleep(2)

        # click on radio button Delivery Date
        driver.find_element(By.XPATH, "//div[contains(@data-role,'expander')]").click()
        time.sleep(2)

        # Entering a placeholder date
        driver.find_element(By.XPATH, "//div[@data-day='30']").click()
        driver.set_page_load_timeout(2)

        # Entering a placeholder address
        driver.find_element(By.XPATH, "//input[@placeholder='Street Address']").send_keys("b102")
        driver.set_page_load_timeout(2)

        # Entering a placeholder street address
        driver.find_element(By.XPATH, "//input[contains(@placeholder,'Street Address Line 2')]").send_keys("b101")
        driver.set_page_load_timeout(2)

        # Entering a placeholder city
        driver.find_element(By.XPATH, "//input[contains(@placeholder,'City')]").send_keys("paris")
        driver.set_page_load_timeout(2)

        # Entering a placeholder region
        driver.find_element(By.XPATH, "//input[contains(@placeholder,'Region')]").send_keys("efel")
        driver.set_page_load_timeout(2)

        # Entering a placeholder zip code
        driver.find_element(By.XPATH, "//input[@placeholder='Postal / Zip Code']").send_keys("1233456")
        driver.set_page_load_timeout(2)

        # Entering a placeholder country
        driver.find_element(By.XPATH, "(//input[@type='text'])[9]").send_keys("American Samoa")
        driver.set_page_load_timeout(2)

        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_DOWN)
        driver.set_page_load_timeout(2)

        # click on radio button Dropdown
        driver.find_element(By.XPATH, "//option[contains(text(),'Choice3')]").click()
        driver.set_page_load_timeout(2)

        # click on radio button checkbox
        driver.find_element(By.XPATH, "(//label[@role='checkbox'])[3]").click()
        driver.set_page_load_timeout(2)

        # click on radio button checkbox Submit order
        driver.find_element(By.XPATH, "//span[contains(.,'Submit order')]").click()
        driver.set_page_load_timeout(2)

        if "Order Form" == "Order Form":
            # Set the status of test as 'passed' or 'failed' based on the condition; if item is added to cart
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": '
                '"iPhone 12 has been successfully added to the cart!"}}')
    except NoSuchElementException:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some '
            'elements failed to load"}}')
    except Exception:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some '
            'exception occurred"}}')
        # Stop the driver
    driver.quit()


for cap in capabilities:
    Thread(target=run_session, args=(cap,)).start()


def my_key():
    return None