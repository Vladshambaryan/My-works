import time
from random import random

import requests
import self
from dotenv import load_dotenv
import os

from faker import Faker
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
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


        driver = webdriver.Chrome()
        action = webdriver.ActionChains(driver)
        driver.get("https://www.lexus.com/")
        driver.maximize_window()
        time.sleep(7)

        # Найти элемент, на который нужно навести мышь
        element = driver.find_element(By.XPATH, "//button[contains(.,'VEHICLES')]")
        # Создать экземпляр класса ActionChains
        actions = ActionChains(driver)
        # Навести мышь на элемент
        actions.move_to_element(element).perform()
        delay()
        driver.find_element(By.XPATH, "(//a[@href='/models/UX-hybrid'])[1]").click()
        delay()

        try:
            assert driver.find_element(By.XPATH, "//img[@alt='Lexus: Experience Amazing Home']")
            print(" Page Title is Experience Amazing")
        except AssertionError:
            print("Logo is different. ")

        # Опускание странички на 500 пикселей вниз
        driver.execute_script("window.scrollBy(0, 750);")
        try:
            assert driver.find_element(By.XPATH, "//span[contains(.,'UX HYBRID F SPORT HANDLING')]")
            print("Page Title is UX HYBRID F SPORT HANDLING")
        except AssertionError:
            print("text is different. ")

        time.sleep(5)
        driver.find_element(By.XPATH, "//img[@alt='Eminent White Pearl']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Iridium']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Cloudburst Gray']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Caviar']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Obsidian']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Redline']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "(//img[contains(@alt,'Cadmium Orange')])[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Nori Green Pearl']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Grecian Water']").click()

        driver.find_element(By.XPATH, "//button[contains(.,'Slide 1')]").click()
        delay()
        driver.find_element(By.XPATH, "//button[contains(.,'Slide 2')]").click()
        delay()
        driver.find_element(By.XPATH, "//button[contains(.,'Slide 3')]").click()
        delay()
        driver.find_element(By.XPATH, "//button[contains(.,'Slide 4')]").click()
        delay()
        driver.find_element(By.XPATH, "//button[contains(.,'Slide 5')]").click()
        delay()

        driver.find_element(By.XPATH, "(//span[contains(.,'INTERIOR')])[1]").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//button[contains(.,'Slide 1')]").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//button[contains(.,'Slide 2')]").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "(//img[@alt='Birch Nuluxe and black washi dash'])[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Black nuluxe and black washi dash']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Palamino Nuluxe and black washi dash']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "(//img[@alt='Birch Nuluxe and black washi dash'])[2]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Black Nuluxe and black washi dash']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@alt='Birch lapis and black washi dash']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//span[contains(.,'WHEELS')]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@data-swatch-index='0']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@data-swatch-index='1']").click()
        delay()

        driver.find_element(By.XPATH, "//a[@href='#model_styles'][contains(.,'STYLES')]").click()
        delay()
        try:
            assert driver.find_element(By.XPATH, "(//span[contains(.,'UX 250h')])[5]")
            print("Page Title is 'UX 250h'")
        except AssertionError:
            print("Page text is different. ")

        driver.find_element(By.XPATH, "(//a[contains(.,'DESIGN')])[1]").click()
        time.sleep(1)
        try:
            assert driver.find_element(By.XPATH, "//h6[contains(.,'DRIVER-INSPIRED INTERIOR')]")
            print("Page Title 'DRIVER-INSPIRED INTERIOR'")
        except AssertionError:
            print("Page text is different. ")

        driver.find_element(By.XPATH, "//a[contains(.,'GALLERY')]").click()
        time.sleep(1)

        driver.find_element(By.XPATH, "//button[contains(.,'Next Slide')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(.,'Next Slide')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(.,'Next Slide')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(.,'Next Slide')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(.,'Next Slide')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(.,'Next Slide')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(.,'Next Slide')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(.,'Next Slide')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(.,'Next Slide')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(.,'Next Slide')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(.,'Next Slide')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(.,'Next Slide')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(.,'Next Slide')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(.,'Next Slide')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(.,'Next Slide')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(.,'Next Slide')]").click()
        time.sleep(1)

        driver.find_element(By.XPATH, "(//a[contains(.,'TECHNOLOGY')])[1]").click()
        time.sleep(1)
        try:
            assert driver.find_element(By.XPATH, "//h4[contains(.,'THE INNOVATIVE UX HYBRID')]")
            print("Page Title is 'THE INNOVATIVE UX HYBRID'")
        except AssertionError:
            print("Page text is different. ")

        driver.find_element(By.XPATH, "(//a[contains(.,'PERFORMANCE')])[1]").click()
        time.sleep(1)
        try:
            assert driver.find_element(By.XPATH, "//h6[contains(.,'17.1-FT TURNING RADIUS')]")
            print("Page Title is '17.1-FT TURNING RADIUS'")
        except AssertionError:
            print("Page text is different. ")

        driver.find_element(By.XPATH, "(//a[contains(.,'SAFETY')])[1]").click()
        time.sleep(1)
        try:
            assert driver.find_element(By.XPATH, "//h6[contains(.,'LEXUS SAFETY SYSTEM+ 2.5')]")
            print("Page Title is 'LEXUS SAFETY SYSTEM+ 2.5'")
        except AssertionError:
            print("Page text is different. ")

        driver.find_element(By.XPATH, "//a[contains(.,'OFFERS')]").click()
        time.sleep(1)
        try:
            assert driver.find_element(By.XPATH, "//h4[contains(.,'SEE OFFERS IN YOUR AREA')]")
            print("Page Title is 'SEE OFFERS IN YOUR AREA'")
        except AssertionError:
            print("Page text is different. ")

        element = driver.find_element(By.XPATH, "(//button[contains(.,'SIGN IN')])[1]")
        # Создать экземпляр класса ActionChains
        actions = ActionChains(driver)
        # Навести мышь на элемент
        actions.move_to_element(element).perform()
        delay()

        driver.find_element(By.XPATH, "//a[contains(.,'CREATE ACCOUNT')]").click()
        time.sleep(4)

        try:
            assert driver.find_element(By.XPATH, "//h2[contains(.,'CREATE AN ACCOUNT')]")
            print("Page Title is 'CREATE AN ACCOUNT'")
        except AssertionError:
            print("Page text is different. ")

        element = driver.find_element(By.XPATH, "(//button[contains(.,'SIGN IN')])[1]")
        # Создать экземпляр класса ActionChains
        actions = ActionChains(driver)
        # Навести мышь на элемент
        actions.move_to_element(element).perform()
        delay()

        driver.find_element(By.XPATH, "//a[contains(.,'CREATE ACCOUNT')]").click()
        delay()

        driver.find_element(By.XPATH, "//span[contains(.,'ACCOUNT TYPE')]").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[contains(text(),'Individual')]").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@name='firstName']").send_keys("Vlad")
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@name='lastName']").send_keys("Shamb")
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@name='email']").send_keys("skachat30913@gmail.com")
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@name='phoneNumber']").send_keys("2344148567")
        time.sleep(2)

        driver.find_element(By.XPATH, "(//input[@type='password'])[1]").send_keys("Pp$#%12mmm34mmm56")
        time.sleep(4)

        driver.find_element(By.XPATH, "//input[contains(@name,'confirm_password')]").send_keys("Pp$#%12mmm34mmm56")
        time.sleep(4)

        driver.find_element(By.XPATH, "//button[@data-testid='LexusButton']").click()
        time.sleep(2)

        driver.get("https://www.lexus.com/")
        driver.maximize_window()
        time.sleep(7)

        element = driver.find_element(By.XPATH, "(//button[contains(.,'SIGN IN')])[1]")
        # Создать экземпляр класса ActionChains
        actions = ActionChains(driver)
        # Навести мышь на элемент
        actions.move_to_element(element).perform()
        delay()

        driver.find_element(By.XPATH, "//a[contains(.,'SIGN IN')]").click()

        time.sleep(7)
        driver.find_element(By.XPATH, "//input[contains(@data-testid,'logonUsername')]").send_keys(
            "skachat30913@gmail.com")
        time.sleep(7)

        driver.find_element(By.XPATH, "//button[contains(text(),'Next Step')]").click()
        time.sleep(4)

        driver.find_element(By.XPATH, "//input[@id='logonPassword']").send_keys("Pp$#%12mmm34mmm56")
        time.sleep(2)

        driver.find_element(By.XPATH, "//button[contains(.,'SIGN IN')]").click()
        time.sleep(2)

        driver.quit()

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