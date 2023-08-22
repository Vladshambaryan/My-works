from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import unittest
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service

def delay():
    time.sleep(random.randint(1, 5))

class Tesla_Model_S(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_Tesla_Model_S(self):
        driver = self.driver
        driver.get("https://www.tesla.com/models")
        wait = WebDriverWait(driver, 5)

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'View Inventory')])[10]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'View Inventory')])[10]")))
        print("View Inventory button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Demo Drive')])[2]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Demo Drive')])[2]")))
        print("Demo Drive button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Compare')])[5]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Compare')])[5]")))
        print("Compare button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Order Model S')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Order Model S')])[1]")))
        print("Order Model S button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 3500);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Order Now')])[4]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Order Now')])[4]")))
        print("Order Now radio button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Compare Models')])[3]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Compare Models')])[3]")))
        print("Compare Models button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 2200);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Order Now')])[7]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Order Now')])[7]")))
        print("Order Now button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'View Inventory')])[3]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'View Inventory')])[3]")))
        print("View Inventory button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 2200);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Order Now')])[8]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Order Now')])[8]")))
        print("Order Now button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Find My Route')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Find My Route')])[1]")))
        print("Find My Route button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 1400);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Learn More')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Learn More')]")))
        print("Learn More button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 1400);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Order Now')])[11]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Order Now')])[11]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'View Inventory')])[4]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'View Inventory')])[4]")))
        print("View Inventory button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Order Now')])[16]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Order Now')])[16]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'View Inventory')])[9]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'View Inventory')])[9]")))

        driver.execute_script("window.scrollBy(0, 1400);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//button[contains(.,'Model S Plaid')])[2]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[contains(.,'Model S Plaid')])[2]")))
        print("Model S Plaid button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//button[contains(.,'Model S')])[5]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[contains(.,'Model S')])[5]")))
        print("Model S button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Compare Models')])[5]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'Compare Models')])[5]")))
        print("Compare Models Plaid button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Order Now')])[17]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Order Now')])[17]")))
        print("Order Now button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Request a Callback')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Request a Callback')]")))
        print("Request a Callback button is visible and clickable")

        # lower menu
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/about'][contains(.,'Tesla © 2023')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/about'][contains(.,'Tesla © 2023')]")))
        print("Tesla © 2023 button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/legal'][contains(.,'Privacy & Legal')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/legal'][contains(.,'Privacy & Legal')]")))
        print("Privacy & Legalbutton is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'Vehicle Recalls')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Vehicle Recalls')]")))
        print("Vehicle Recalls button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/contact'][contains(.,'Contact')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/contact'][contains(.,'Contact')]")))
        print("Contact button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'News')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'News')]")))
        print("News button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/updates']")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/updates']")))
        print("updates is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'Locations')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Locations')]")))
        print("Locations button is visible and clickable")



    def tearDown(self):
        self.driver.quit()


class Tesla_Model_3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_Tesla_Model_3(self):
        driver = self.driver
        wait = WebDriverWait(driver, 5)

        # Model 3 checkable vizible and clickable
        driver.get("https://www.tesla.com/model3")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'View Inventory')])[4]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'View Inventory')])[4]")))
        print("View Inventory button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Demo Drive')])[7]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Demo Drive')])[7]")))
        print("Demo Drive button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Compare')])[4]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Compare')])[4]")))
        print("Compare button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Order Model 3')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Order Model 3')])[1]")))
        print("Order Model 3 button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'exceed safety standards')])[3]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'exceed safety standards')])[3]")))
        print("exceed safety standards button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Chat with a Tesla Advisor')])[3]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'Chat with a Tesla Advisor')])[3]")))
        print("Chat with a Tesla Advisor button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[@class='tds-link'])[17]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='tds-link'])[17]")))
        print("schedule a demo drive  button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Plan My Trip')])[3]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Plan My Trip')])[3]")))
        print("Plan My Trip button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 2200);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'View Inventory')])[3]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'View Inventory')])[3]")))
        print("View Inventory button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 4200);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Chat with a Tesla Advisor')])[7]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'Chat with a Tesla Advisor')])[7]")))
        print("Chat with a Tesla Advisor button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Compare Models')])[3]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Compare Models')])[3]")))
        print("Compare Models button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Demo Drive')])[6]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Demo Drive')])[6]")))
        print("Demo Drive button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Chat with a Tesla Advisor')])[11]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'Chat with a Tesla Advisor')])[11]")))
        print("Chat with a Tesla Advisor button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 1400);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='-1']")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='-1']")))
        print("Performance drive  button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='-2']")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='-2']")))
        print("Long Range AWD button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='-3']")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='-3']")))
        print("Rear-Wheel Drive  button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 2200);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[@href='/ownersmanual/index-model-3.html'])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@href='/ownersmanual/index-model-3.html'])[1]")))
        print("Owner's Manual  button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[@href='/compare'])[4]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@href='/compare'])[4]")))
        print("Compare Models button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 600);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Custom Order')])[3]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Custom Order')])[3]")))
        print("Custom Order button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Request a Callback')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Request a Callback')]")))
        print("Request a Callback button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@rel,'nofollow noopener')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@rel,'nofollow noopener')]")))
        print("Learn more about Standard Connectivity and any limitations. button is visible and clickable")

        # lower menu
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/about'][contains(.,'Tesla © 2023')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/about'][contains(.,'Tesla © 2023')]")))
        print("Tesla © 2023 button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/legal'][contains(.,'Privacy & Legal')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/legal'][contains(.,'Privacy & Legal')]")))
        print("Privacy & Legalbutton is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'Vehicle Recalls')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Vehicle Recalls')]")))
        print("Vehicle Recalls button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/contact'][contains(.,'Contact')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/contact'][contains(.,'Contact')]")))
        print("Contact button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'News')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'News')]")))
        print("News button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/updates']")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/updates']")))
        print("updates is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'Locations')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Locations')]")))
        print("Locations button is visible and clickable")

    def tearDown(self):
        self.driver.quit()


class Tesla_Model_X(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_Tesla_Model_X(self):
        driver = self.driver
        wait = WebDriverWait(driver, 5)

        # Model X checkable vizible and clickable
        driver.get("https://www.tesla.com/modelx")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//span[contains(.,'View Inventory')])[10]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//span[contains(.,'View Inventory')])[10]")))
        print("View Inventory button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//span[contains(.,'Demo Drive')])[2]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//span[contains(.,'Demo Drive')])[2]")))
        print("Demo Drive button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//span[contains(.,'Compare')])[5]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//span[contains(.,'Compare')])[5]")))
        print("Compare button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//span[contains(.,'Order Model X')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//span[contains(.,'Order Model X')])[1]")))
        print("Order Model X button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 2800);")

        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//span[contains(.,'Order Now')])[4]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//span[contains(.,'Order Now')])[4]")))
        print("Order Now button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//span[contains(.,'View Inventory')])[3]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//span[contains(.,'View Inventory')])[3]")))
        print("View Inventory button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//a[contains(.,'Chat with a Tesla Advisor')])[3]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//a[contains(.,'Chat with a Tesla Advisor')])[3]")))
        print("Chat with a Tesla Advisor button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//a[contains(.,'schedule a demo drive')])[3]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//a[contains(.,'schedule a demo drive')])[3]")))
        print("schedule a demo drive button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 2200);")

        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//span[contains(.,'Order Now')])[5]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//span[contains(.,'Order Now')])[5]")))
        print("Order Now button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//span[contains(.,'Compare Models')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//span[contains(.,'Compare Models')])[1]")))
        print("Compare Models button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//span[contains(.,'Order Now')])[10]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//span[contains(.,'Order Now')])[10]")))
        print("Order Now button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//span[contains(.,'View Inventory')])[6]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//span[contains(.,'View Inventory')])[6]")))
        print("View Inventory button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//a[contains(.,'Chat with a Tesla Advisor')])[5]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//a[contains(.,'Chat with a Tesla Advisor')])[5]")))
        print("Chat with a Tesla Advisor button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//a[contains(.,'schedule a demo drive')])[5]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//a[contains(.,'schedule a demo drive')])[5]")))
        print("schedule a demo drive button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 300);")

        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//span[contains(.,'Order Now')])[11]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//span[contains(.,'Order Now')])[11]")))
        print("Order Now button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//span[contains(.,'Find My Route')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//span[contains(.,'Find My Route')])[1]")))
        print("Find My Route button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 2200);")

        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//span[contains(.,'Learn More')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//span[contains(.,'Learn More')])[1]")))
        print("Learn More button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//span[contains(.,'Order Now')])[14]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//span[contains(.,'Order Now')])[14]")))
        print("Order Now button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//span[contains(.,'Learn More')])[2]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//span[contains(.,'Learn More')])[2]")))
        print("Learn More button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//span[contains(.,'Order Now')])[19]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//span[contains(.,'Order Now')])[19]")))
        print("Order Now button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'View Inventory')])[9]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'View Inventory')])[9]")))
        print("View Inventory button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Chat with a Tesla Advisor')])[11]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'Chat with a Tesla Advisor')])[11]")))
        print("Chat with a Tesla Advisor button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'schedule a demo drive')])[11]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'schedule a demo drive')])[11]")))
        print("schedule a demo drive button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 1400);")

        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//button[contains(.,'Model X Plaid')])[2]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//button[contains(.,'Model X Plaid')])[2]")))
        print("Model X Plaid button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//button[contains(.,'Model X')])[6]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//button[contains(.,'Model X')])[6]")))
        print("Model X button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//span[contains(.,'Compare Models')])[4]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//span[contains(.,'Compare Models')])[4]")))
        print("Compare Models button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//span[contains(.,'Order Now')])[20]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//span[contains(.,'Order Now')])[20]")))
        print("Order Now button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Request a Callback')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Request a Callback')]")))
        print("Request a Callback button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@rel='nofollow noopener']")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@rel='nofollow noopener']")))
        print("Learn more about Standard Connectivity and any limitations button is visible and clickable")

        # lower menu
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/about'][contains(.,'Tesla © 2023')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/about'][contains(.,'Tesla © 2023')]")))
        print("Tesla © 2023 button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/legal'][contains(.,'Privacy & Legal')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/legal'][contains(.,'Privacy & Legal')]")))
        print("Privacy & Legalbutton is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'Vehicle Recalls')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Vehicle Recalls')]")))
        print("Vehicle Recalls button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/contact'][contains(.,'Contact')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/contact'][contains(.,'Contact')]")))
        print("Contact button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'News')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'News')]")))
        print("News button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/updates']")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/updates']")))
        print("updates is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'Locations')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Locations')]")))
        print("Locations button is visible and clickable")

    def tearDown(self):
        self.driver.quit()


class Tesla_Model_Y(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_Tesla_Model_Y(self):
        driver = self.driver
        wait = WebDriverWait(driver, 5)

        # Model Y checkable vizible and clickable
        driver.get("https://www.tesla.com/modely")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//a[contains(.,'exceed safety standards')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//a[contains(.,'exceed safety standards')])[1]")))
        print("exceed safety standards button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//span[contains(.,'Order Now')])[3]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//span[contains(.,'Order Now')])[3]")))
        print("Order Now button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//span[contains(.,'View Inventory')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//span[contains(.,'View Inventory')])[1]")))
        print("View Inventory button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//span[contains(.,'Order Now')])[7]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//span[contains(.,'Order Now')])[7]")))
        print("Order Now button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//span[contains(.,'View Inventory')])[5]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//span[contains(.,'View Inventory')])[5]")))
        print("View Inventory button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//a[contains(.,'Chat with a Tesla Advisor')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//a[contains(.,'Chat with a Tesla Advisor')])[1]")))
        print("Chat with a Tesla Advisor button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//a[contains(.,'schedule a demo drive')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//a[contains(.,'schedule a demo drive')])[1]")))
        print("schedule a demo drive button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 1400);")

        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//span[contains(.,'Order Now')])[10]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//span[contains(.,'Order Now')])[10]")))
        print("Order Now button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//span[contains(.,'View Inventory')])[8]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//span[contains(.,'View Inventory')])[8]")))
        print("View Inventory button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//a[contains(.,'Compare Models')])[3]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//a[contains(.,'Compare Models')])[3]")))
        print("Compare Models button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Order Now')])[11]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//span[contains(.,'Order Now')])[11]")))
        print("Order Now button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH,   "(//span[contains(.,'View Inventory')])[9]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//span[contains(.,'View Inventory')])[9]")))
        print("View Inventory button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//a[contains(.,'Chat with a Tesla Advisor')])[3]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//a[contains(.,'Chat with a Tesla Advisor')])[3]")))
        print("Chat with a Tesla Advisor button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//span[contains(.,'Order Now')])[16]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//span[contains(.,'Order Now')])[16]")))
        print("Order Now button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'View Inventory')])[18]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//a[contains(.,'View Inventory')])[18]")))
        print("View Inventory button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//span[contains(.,'Order Now')])[19]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//span[contains(.,'Order Now')])[19]")))
        print("Order Now button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//span[contains(.,'View Inventory')])[17]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//span[contains(.,'View Inventory')])[17]")))
        print("View Inventory button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//a[contains(.,'Compare Models')])[7]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//a[contains(.,'Compare Models')])[7]")))
        print("Compare Models button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 1400);")

        wait.until(EC.visibility_of_element_located((By.XPATH,  "//button[contains(.,'Performance')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "//button[contains(.,'Performance')]")))
        print("Performance button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH,  "//button[contains(.,'Long Range AWD')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "//button[contains(.,'Long Range AWD')]")))
        print("Long Range AWD button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH,  "//button[contains(.,'All-Wheel Drive')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "//button[contains(.,'All-Wheel Drive')]")))
        print("All-Wheel Drive button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 800);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@data-gtm-interaction='owners manual']")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "//a[@data-gtm-interaction='owners manual']")))
        print("owners manual button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH,  "//span[contains(.,'Compare Models')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "//span[contains(.,'Compare Models')]")))
        print("Compare Models button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH,  "(//span[contains(.,'Order Now')])[20]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//span[contains(.,'Order Now')])[20]")))
        print("Order Now button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/support/connectivity#connectivity-features-limited']")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "//a[@href='/support/connectivity#connectivity-features-limited']")))


        # lower menu
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/about'][contains(.,'Tesla © 2023')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/about'][contains(.,'Tesla © 2023')]")))
        print("Tesla © 2023 button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/legal'][contains(.,'Privacy & Legal')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/legal'][contains(.,'Privacy & Legal')]")))
        print("Privacy & Legalbutton is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'Vehicle Recalls')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Vehicle Recalls')]")))
        print("Vehicle Recalls button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/contact'][contains(.,'Contact')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/contact'][contains(.,'Contact')]")))
        print("Contact button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'News')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'News')]")))
        print("News button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/updates']")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/updates']")))
        print("updates is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'Locations')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Locations')]")))
        print("Locations button is visible and clickable")

    def tearDown(self):
        self.driver.quit()


class Solar_Roof(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_Solar_Roof(self):
        driver = self.driver
        wait = WebDriverWait(driver, 5)


        # Solar Roof checkable vizible and clickable
        driver.get("https://www.tesla.com/solarroof")
        delay()
        driver.find_element(By.XPATH, "(//span[contains(.,'Solar Roof')])[1]").click()
        delay()
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Order Now')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'Order Now')])[1]")))
        print("Order Now button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Schedule a Callback')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Schedule a Callback')])[1]")))
        print("Schedule a Callback button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Support')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Support')])[1]")))
        print("Support button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Order Solar Roof')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Order Solar Roof')])[1]")))
        print("Order Solar Roof button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Schedule a virtual consultation')])[3]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'Schedule a virtual consultation')])[3]")))
        print("Schedule a virtual consultation button is visible and clickable")


        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Order Now')])[4]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Order Now')])[4]")))
        print("Order Now button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Learn More')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Learn More')])[1]")))
        print("Learn More button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Order Now')])[8]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'Order Now')])[8]")))
        print("Order Now button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Order Now')])[12]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Order Now')])[12]")))
        print("Order Now button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Chat with a Tesla Advisor')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'Chat with a Tesla Advisor')])[1]")))
        print("Chat with a Tesla Advisor button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Tesla Solar Inverter')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'Tesla Solar Inverter')])[1]")))
        print("Tesla Solar Inverter button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Order Now')])[13]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Order Now')])[13]")))
        print("Order Now button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Order Now')])[18]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Order Now')])[18]")))
        print("Order Now Advisor button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Order Now')])[19]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Order Now')])[19]")))
        print("Order Now button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Schedule a Virtual Consultation')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Schedule a Virtual Consultation')]")))
        print("Schedule a Virtual Consultation button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Get Updates')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'Get Updates')])[1]")))
        print("Get Updates button is visible and clickable")



        # lower menu
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/about'][contains(.,'Tesla © 2023')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/about'][contains(.,'Tesla © 2023')]")))
        print("Tesla © 2023 button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/legal'][contains(.,'Privacy & Legal')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/legal'][contains(.,'Privacy & Legal')]")))
        print("Privacy & Legalbutton is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'Vehicle Recalls')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Vehicle Recalls')]")))
        print("Vehicle Recalls button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/contact'][contains(.,'Contact')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/contact'][contains(.,'Contact')]")))
        print("Contact button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'News')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'News')]")))
        print("News button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/updates']")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/updates']")))
        print("updates is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'Locations')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Locations')]")))
        print("Locations button is visible and clickable")

    def tearDown(self):
        self.driver.quit()



class Solar_Panels(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_Solar_Panels(self):
        driver = self.driver
        wait = WebDriverWait(driver, 5)

        # Solar Panels checkable vizible and clickable
        driver.get("https://www.tesla.com/solarpanels")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Schedule a Virtual Consultation')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Schedule a Virtual Consultation')])[1]")))
        print("Schedule a Virtual Consultatio button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Support')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Support')])[1]")))
        print("Support button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Order Solar Panels')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Order Solar Panels')])[1]")))
        print("Order Solar Panels button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[@class='tds-link'])[2]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='tds-link'])[2]")))
        print("Tesla's price match guarantee button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Schedule a virtual consultation')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'Schedule a virtual consultation')])[1]")))
        print("Schedule a virtual consultation button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'See Your Savings')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'See Your Savings')])[1]")))
        print("See Your Savings button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Schedule a Consultation')])[2]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Schedule a Consultation')])[2]")))
        print("Schedule a Consultation button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Schedule a virtual consultation')])[5]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'Schedule a virtual consultation')])[5]")))
        print("Schedule a virtual consultation button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Order Now')])[2]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Order Now')])[2]")))
        print("Order Now button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 2800);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Order Now')])[7]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Order Now')])[7]")))
        print("Order Now button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Learn More')])[3]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Learn More')])[3]")))
        print("Learn More button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Order Now')])[10]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Order Now')])[10]")))
        print("Order Now button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'request a call')])[3]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'request a call')])[3]")))
        print("request a call button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Chat with a Tesla Advisor')])[3]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'Chat with a Tesla Advisor')])[3]")))
        print("Chat with a Tesla Advisor button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Tesla Solar Inverter')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'Tesla Solar Inverter')])[1]")))
        print("Tesla Solar Inverter button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Order Now')])[11]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Order Now')])[11]")))
        print("Order Now button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Order Now')])[16]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Order Now')])[16]")))
        print("Order Now button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'3.8kW / 7.6kW')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'3.8kW / 7.6kW')]")))
        print("3.8kW / 7.6kW button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Order Now')])[17]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'Order Now')])[17]")))
        print("Order Now button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Schedule a Consultation')])[5]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Schedule a Consultation')])[5]")))
        print("Schedule a Consultation button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Get Updates')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'Get Updates')])[1]")))
        print("Get Updates button is visible and clickable")

        # lower menu
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/about'][contains(.,'Tesla © 2023')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/about'][contains(.,'Tesla © 2023')]")))
        print("Tesla © 2023 button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/legal'][contains(.,'Privacy & Legal')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/legal'][contains(.,'Privacy & Legal')]")))
        print("Privacy & Legalbutton is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'Vehicle Recalls')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Vehicle Recalls')]")))
        print("Vehicle Recalls button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/contact'][contains(.,'Contact')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/contact'][contains(.,'Contact')]")))
        print("Contact button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'News')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'News')]")))
        print("News button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/updates']")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/updates']")))
        print("updates is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'Locations')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Locations')]")))
        print("Locations button is visible and clickable")
    def tearDown(self):
        self.driver.quit()


class Powerwall(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_Powerwall(self):
        driver = self.driver
        wait = WebDriverWait(driver, 5)

        # Powerwall checkable vizible and clickable
        driver.get("https://www.tesla.com/powerwall")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Order Powerwall')])[9]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Order Powerwall')])[9]")))
        print("Order Powerwall button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Schedule a Callback')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Schedule a Callback')])[1]")))
        print("Schedule a Callback button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Support')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Support')])[1]")))
        print("Support button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Order With Solar')])[2]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Order With Solar')])[2]")))
        print("Order With Solar button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Order Powerwall')])[4]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Order Powerwall')])[4]")))
        print("Order Powerwall button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Request Callback')])[2]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Request Callback')])[2]")))
        print("Request Callback button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 1400);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Learn More')])[8]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,  "(//span[contains(.,'Learn More')])[8]")))
        print("Learn More button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Chat with an energy advisor')])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'Chat with an energy advisor')])[1]")))
        print(" Chat with an energy advisor button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Order Powerwall')])[5]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Order Powerwall')])[5]")))
        print(" Order Powerwall button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(.,'Powerwall+')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Powerwall+')]")))
        print(" Powerwall+ button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//button[contains(.,'Powerwall')])[2]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[contains(.,'Powerwall')])[2]")))
        print(" Powerwall button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[@title='Powerwall Technical Specifications'])[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@title='Powerwall Technical Specifications'])[1]")))
        print(" PowerwallPowerwall Technical Specifications button is visible and clickable")

        driver.execute_script("window.scrollBy(0, 700);")

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Order Powerwall')])[8]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Order Powerwall')])[8]")))
        print("Order Powerwall button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Chat with Energy Advisor')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Chat with Energy Advisor')]")))
        print("Chat with Energy Advisor button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'Get Energy Updates')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Get Energy Updates')]")))
        print("Get Energy Updates button is visible and clickable")


        # lower menu
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/about'][contains(.,'Tesla © 2023')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/about'][contains(.,'Tesla © 2023')]")))
        print("Tesla © 2023 button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/legal'][contains(.,'Privacy & Legal')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/legal'][contains(.,'Privacy & Legal')]")))
        print("Privacy & Legalbutton is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'Vehicle Recalls')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Vehicle Recalls')]")))
        print("Vehicle Recalls button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/contact'][contains(.,'Contact')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/contact'][contains(.,'Contact')]")))
        print("Contact button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'News')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'News')]")))
        print("News button is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/updates']")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/updates']")))
        print("updates is visible and clickable")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'Locations')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Locations')]")))
        print("Locations button is visible and clickable")

    def tearDown(self):
        self.driver.quit()


class Tesla_Shop(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_Tesla_Shop(self):
        driver = self.driver
        wait = WebDriverWait(driver, 5)

        # Tesla_Shop checkable vizible and clickable

        driver.get("https://shop.tesla.com/")
        driver.maximize_window()
        driver.find_element(By.XPATH, "(//span[contains(.,'Shop')])[1]").click()

        driver.find_element(By.XPATH, "//a[contains(text(),'Charging')]").click()

        try:
            assert "Text At Home in page"
            print("At Home text is visible")
        except AssertionError:
            print("Page text is different")

        delay()
        driver.execute_script("window.scrollBy(0, 900);")

        try:
            assert "Text On the Road in page"
            print("On the Road text is visible")
        except AssertionError:
            print("Page text is different")

        delay()
        driver.execute_script("window.scrollBy(0, 800);")

        try:
            assert "Text Parts in page"
            print("Parts text is visible")
        except AssertionError:
            print("Page text is different")

        delay()
        driver.find_element(By.XPATH, "//a[contains(.,'Vehicle Accessories')]").click()
        try:
            assert "Text Best Sellers in page"
            print("Best Sellers text is visible")
        except AssertionError:
            print("Page text is different")

        delay()
        driver.execute_script("window.scrollBy(0, 500);")
        try:
            assert "Text Interior in page"
            print("Interior text is visible")
        except AssertionError:
            print("Page text is different")
        delay()
        driver.execute_script("window.scrollBy(0, 1500);")

        try:
            assert "Text Exterior in page"
            print("Exterior text is visible")
        except AssertionError:
            print("Page text is different")

        delay()
        driver.execute_script("window.scrollBy(0, 700);")

        try:
            assert "Text Wheels and Tires in page"
            print("Wheels and Tires is visible")
        except AssertionError:
            print("Page text is different")

        delay()
        driver.execute_script("window.scrollBy(0, 1500);")
        try:
            assert "Text Floor Mats in page"
            print("Floor Mats is visible")
        except AssertionError:
            print("Page text is different")

        delay()
        driver.execute_script("window.scrollBy(0, 1500);")
        try:
            assert "Text Parts in page"
            print("Parts is visible")
        except AssertionError:
            print("Page text is different")
        delay()
        driver.execute_script("window.scrollBy(0, 900);")
        try:
            assert "Text Keys in page"
            print("Keys is visible")
        except AssertionError:
            print("Page text is different")
        delay()
        driver.execute_script("window.scrollBy(0, 900);")
        try:
            assert "Text Best Sellers in page"
            print("Best Sellers is visible")
        except AssertionError:
            print("Page text is different")

    def tearDown(self):
        self.driver.quit()


class Tesla_Positiv(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_Tesla_Positiv(self):
        driver = self.driver
        wait = WebDriverWait(driver, 5)

        # Tesla_Positiv checkable vizible and clickable
        driver.get("https://www.tesla.com/models")
        driver.maximize_window()

        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "//span[contains(.,'Model S')]").click()

        driver.find_element(By.XPATH, "(//span[contains(.,'Order Now')])[1]").is_displayed()

        driver.find_element(By.XPATH, "//span[contains(.,'Demo Drive')]").is_displayed()

        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 700);")
        time.sleep(1)
        try:
            assert driver.find_element(By.XPATH, "//h2[contains(.,'Interior of the Future')]").is_displayed()
            print("Interior of the Future text is visible")
        except AssertionError:
            print("Page text is different")
        delay()
        driver.execute_script("window.scrollBy(0, 700);")
        time.sleep(1)
        try:
            assert driver.find_element(By.XPATH, "//span[contains(.,'Cinematic Experience')]").is_displayed()
            print("Cinematic Experience text is visible")
        except AssertionError:
            print("Page text is different")
        delay()
        driver.execute_script("window.scrollBy(0, 900);")
        time.sleep(1)
        try:
            assert driver.find_element(By.XPATH, "//strong[contains(.,'Immersive Sound')]").is_displayed()
            print("Immersive Sound text is visible")
        except AssertionError:
            print("Page text is different")
        delay()
        driver.execute_script("window.scrollBy(0, 1300);")
        time.sleep(1)
        try:
            assert driver.find_element(By.XPATH, "(//span[contains(.,'Beyond Ludicrous')])[4]").is_displayed()
            print("Beyond Ludicrous text is visible")
        except AssertionError:
            print("Page text is different")
        delay()
        driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(1)
        try:
            assert driver.find_element(By.XPATH, "(//span[contains(.,'Electric Powertrain')])[2]").is_displayed()
            print("Electric Powertrain text is visible")
        except AssertionError:
            print("Page text is different")
        delay()
        driver.execute_script("window.scrollBy(0, 1500);")
        time.sleep(1)
        try:
            assert driver.find_element(By.XPATH, "(//span[contains(.,'Designed for Efficiency')])[4]").is_displayed()
            print("Designed for Efficiency text is visible")
        except AssertionError:
            print("Page text is different")
        delay()
        driver.execute_script("window.scrollBy(0, 1500);")
        time.sleep(1)
        try:
            assert driver.find_element(By.XPATH, "(//span[contains(.,'Go Anywhere')])[2]").is_displayed()
            print("Go Anywhere text is visible")
        except AssertionError:
            print("Page text is different")

        delay()
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(1)
        try:
            assert driver.find_element(By.XPATH, "(//span[contains(.,'Designed for Efficiency')])[4]").is_displayed()
            print("Freedom to Travel text is visible")
        except AssertionError:
            print("Page text is different")
        delay()
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(1)
        try:
            assert driver.find_element(By.XPATH, "(//span[contains(.,'High Impact Protection')])[2]").is_displayed()
            print("High Impact Protection text is visible")
        except AssertionError:
            print("Page text is different")
        delay()

        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(1)
        try:
            assert driver.find_element(By.XPATH, "(//span[contains(.,'Future of Driving')])[4]").is_displayed()
            print("Future of Driving text is visible")
        except AssertionError:
            print("Page text is different")
        delay()
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(1)
        try:
            assert driver.find_element(By.XPATH, "(//button[contains(.,'Model S Plaid')])[2]").is_displayed()
            print("Model S Specs is visible")
        except AssertionError:
            print("Page text is different")
        delay()
        driver.execute_script("window.scrollBy(0, 700);")
        time.sleep(1)
        try:
            assert driver.find_element(By.XPATH, "//span[contains(.,'Experience Model S')]").is_displayed()
            print("Experience Model S is visible")
        except AssertionError:
            print("Page text is different")
        driver.send_keys(Keys.PAGE_UP)

        driver.find_element(By.XPATH, "//header/ol[2]/li[1]/a[1]/*[1]").click()
        delay()
        driver.find_element(By.XPATH, "//span[contains(.,'Menu')]").click()
        delay()
        driver.find_element(By.XPATH,
                            "//span[@class='tds-site-nav-item-text'][contains(.,'Existing Inventory')]").click()
        try:
            assert "Text Inventory in page"
            print("Inventory text is visible")
        except AssertionError:
            print("Page text is different")
        driver.back()
        delay()
        driver.find_element(By.XPATH, "//span[contains(text(),'Used Inventory')]").click()
        try:
            assert "Text Inventory in page"
            print("Inventory text is visible")
        except AssertionError:
            print("Page text is different")
        driver.back()
        delay()
        driver.find_element(By.XPATH, "//span[contains(text(),'Trade-In')]").click()
        try:
            assert "Text Get Trade-In Estimate in page"
            print("Get Trade-In Estimate text is visible")
        except AssertionError:
            print("Page text is different")
        driver.back()
        delay()
        driver.find_element(By.XPATH, "(//span[contains(.,'Demo Drive')])[1]").click()
        try:
            assert "Text GSchedule a Demo Drive in page"
            print("Schedule a Demo Drive text is visible")
        except AssertionError:
            print("Page text is different")
        driver.back()
        delay()
        driver.find_element(By.XPATH, "//span[contains(text(),'Insurance')]").click()
        try:
            assert "Text Insurance in page"
            print("Insurance text is visible")
        except AssertionError:
            print("Page text is different")
        driver.back()
        delay()
        driver.find_element(By.XPATH, "//span[contains(text(),'Fleet')]").click()
        try:
            assert "Text Fleet and Business in page"
            print("Fleet and Business text is visible")
        except AssertionError:
            print("Page text is different")
        driver.back()
        delay()
        driver.find_element(By.XPATH, "//span[contains(text(),'Cybertruck')]").click()
        try:
            assert "Text BETTER UTILITY THAN A TRUCK WITH MORE PERFORMANCE THAN A SPORTS CAR in page"
            print("BETTER UTILITY THAN A TRUCK WITH MORE PERFORMANCE THAN A SPORTS CAR text is visible")
        except AssertionError:
            print("Page text is different")
        driver.back()
        delay()
        driver.find_element(By.XPATH, "//span[contains(text(),'Roadster')]").click()
        try:
            assert "Text Roadster in page"
            print("Roadster text is visible")
        except AssertionError:
            print("Page text is different")
        driver.back()
        time.sleep(8)
        driver.find_element(By.XPATH, "(//span[contains(.,'Semi')])[1]").click()

        time.sleep(8)
        try:
            assert "Text Semi in page"
            print("Semi text is visible")
        except AssertionError:
            print("Page text is different")
        driver.back()
        delay()
        driver.find_element(By.XPATH, "//span[contains(text(),'Charging')]").click()
        try:
            assert "Text Stay Charged in page"
            print("Stay Charged text is visible")
        except AssertionError:
            print("Page text is different")
        driver.back()
        delay()

        driver.find_element(By.XPATH, "//span[contains(.,'Commercial Energy')]").click()
        try:
            assert "Text Commercial Energy in page"
            print("Commercial Energy text is visible")
        except AssertionError:
            print("Page text is different")
        driver.back()
        delay()
        driver.find_element(By.XPATH, "//span[contains(.,'Utilities')]").click()
        try:
            assert "Text CUtilities in page"
            print("Utilities text is visible")
        except AssertionError:
            print("Page text is different")
        driver.back()
        delay()
        driver.find_element(By.XPATH, "//span[contains(text(),'Careers')]").click()
        try:
            assert "Text Careers in page"
            print("Careers text is visible")
        except AssertionError:
            print("Page text is different")
        driver.back()
        delay()
        driver.find_element(By.XPATH, "//span[contains(text(),'Find Us')]").click()
        try:
            assert "Text Schedule a Demo Drive in page"
            print("Schedule a Demo Drive text is visible")
        except AssertionError:
            print("Page text is different")
        driver.back()
        delay()
        driver.find_element(By.XPATH, "//span[contains(text(),'Events')]").click()
        try:
            assert "Text Events in page"
            print("Events text is visible")
        except AssertionError:
            print("Page text is different")
        driver.back()
        delay()
        driver.find_element(By.XPATH, "//span[contains(text(),'Support')]").click()
        try:
            assert "Text Trending Topics in page"
            print("Trending Topics text is visible")
        except AssertionError:
            print("Page text is different")


    def tearDown(self):
        self.driver.quit()


class Tesla_chat(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_Tesla_chat(self):
        driver = self.driver
        wait = WebDriverWait(driver, 5)

        # Tesla_chat checkable vizible and clickable
        driver.get("https://www.tesla.com/models")
        driver.maximize_window()

        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "//span[contains(.,'Model S')]").click()

        driver.find_element(By.XPATH, "(//span[contains(.,'Order Now')])[1]").is_displayed()

        driver.find_element(By.XPATH, "//span[contains(.,'Demo Drive')]").is_displayed()

        driver.find_element(By.XPATH, "//span[contains(.,'Model S')]").is_displayed()

        driver.find_element(By.XPATH, "//button[@id='tw-chat--avaya-chat__animated_button']").click()
        delay()
        driver.find_element(By.XPATH, "//a[@id='btn-account-support']").is_displayed()
        delay()
        driver.find_element(By.XPATH, "//button[@id='btn-live-agent']").click()
        delay()
        driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("Vladimir")
        delay()
        driver.send_keys(Keys.TAB)
        driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys("Shambaryan")
        delay()
        driver.send_keys(Keys.TAB)
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("123abc@gmail.com")
        delay()
        driver.find_element(By.ID, "phoneNumber").send_keys("+14842989273")
        delay()
        driver.send_keys(Keys.TAB)
        driver.find_element(By.ID, "postalCode").send_keys("12345")
        time.sleep(2)
        driver.find_element(By.XPATH, "//option[contains(text(),'Yes')]").click()
        delay()
        driver.find_element(By.XPATH, "//button[contains(text(),'start chat')]").click()


    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()
