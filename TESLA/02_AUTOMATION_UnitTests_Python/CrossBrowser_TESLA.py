

import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Chrome_tesla(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_tesla(self):
        driver = self.driver
        driver.get("https://www.tesla.com/models")
        wait = WebDriverWait(driver, 5)


        # Model S checkable vizible and clickable

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


class Firefox_tesla(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    # As per unittest module, individual test should start with test_
    def test_search_weather_firefox(self):
        driver = self.driver
        driver.get("https://www.tesla.com/models")
        wait = WebDriverWait(driver, 5)

        # Model S checkable vizible and clickable

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


class Edge_tesla(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()

    # As per unittest module, individual test should start with test_
    def test_tesla_edge(self):
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


if __name__ == "__main__":
    unittest.main()
