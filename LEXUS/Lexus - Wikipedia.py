import requests
import self
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def delay():
    time.sleep(random.randint(1, 2))

def assertIn(param, title):
    return None


driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org/")
driver.maximize_window()


wait = WebDriverWait(driver, 2)


driver.find_element(By.XPATH, "//input[@id='searchInput']").send_keys("Lexus")
delay()

driver.find_element(By.XPATH, "//i[contains(.,'Search')]").click()


try:
    assert driver.title == "Lexus"
    print("Title is Correct. Current Title is:", driver.title)
except AssertionError:
    print("Title is different. Current Title is:", driver.title)

driver.find_element(By.XPATH, "(//div[contains(.,'(Top)')])[5]").click()
delay()
driver.find_element(By.XPATH, "//body/div[2]/div[1]/nav[1]/div[1]/div[1]/ul[1]/li[2]/button[1]/span[1]").click()
delay()
driver.find_element(By.XPATH, "//div[@class='vector-toc-text'][contains(.,'1.11980s: The F1 project')]").click()

try:
    assert driver.title == "1980s: The F1 project"
    print("Title is Correct. Current Title is:", driver.title)
except AssertionError:
    print("Title is different. Current Title is:", driver.title)


driver.find_element(By.XPATH, "//div[@class='vector-toc-text'][contains(.,'1.1.1Brand development')]").click()

try:
    assert driver.title == "Brand development"
    print("Title is Correct. Current Title is:", driver.title)
except AssertionError:
    print("Title is different. Current Title is:", driver.title)


driver.find_element(By.XPATH, "//div[@class='vector-toc-text'][contains(.,'1.1.2Launch')]").click()
delay()
# API response Status code check
codeWiki = requests.get("https://www.wikipedia.org").status_code
if codeWiki == 200:
    print("Wikipedia Url has correct", requests.get("https://www.wikipedia.org").status_code, " as status Code")
else:
    print("Wikipedia Url has incorrect", requests.get("https://www.wikipedia.org").status_code,"as status Code")


driver.find_element(By.XPATH, "//div[@class='vector-toc-text'][contains(.,'1.32000s: Global reorganization')]").click()
delay()



driver.find_element(By.XPATH, "//div[@class='vector-toc-text'][contains(.,'1.3.1Hybrids and F models')]").click()
delay()

# API тест для srlenium
print("Google Url has", requests.get("https://www.google.com").status_code, "as status Code")
code = requests.get("https://www.google.com").status_code
if code == 200:
    print("API response code is OK")
else:
    print("API response code is not 200", "Current code is:", code)


driver.find_element(By.XPATH, "//div[@class='vector-toc-text'][contains(.,'1.42010s–2020s: Recent developments')]").click()
delay()

# перфоманс тест ждем проявления элемента и проверка кликабельности в течении 2 сек
try:
    wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="wob_wc"]')))
    driver.find_element(By.ID, "wob_rain").click()
    delay()
    driver.find_element(By.ID, "wob_wind").click()
    delay()
    driver.find_element(By.ID, "wob_temp").click()
except TimeoutException:
    print("Weather widget loading took more than 5 sec")
driver.find_element(By.XPATH, "//div[@class='vector-toc-text'][contains(.,'2Corporate affairs')]").click()
delay()

#перфоманс тест
try:
    wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="wob_wc"]')))
    print("Lexus widget is visible")
except TimeoutException:
    print("Lexus widget loading took more than 2 sec")


driver.find_element(By.XPATH, "//div[@class='vector-toc-text'][contains(.,'2.1Operations')]").click()
delay()


driver.find_element(By.XPATH, "//div[@class='vector-toc-text'][contains(.,'2.2Sales')]").click()
delay()

driver.find_element(By.XPATH, "//div[@class='vector-toc-text'][contains(.,'2.3Financial performance')]").click()
delay()

driver.find_element(By.XPATH, "//div[@class='vector-toc-text'][contains(.,'3Automobiles')]").click()
delay()

driver.find_element(By.XPATH, "//div[@class='vector-toc-text'][contains(.,'3.1Vehicle lineup')]").click()
delay()

driver.find_element(By.XPATH, "//div[@class='vector-toc-text'][contains(.,'3.2F marque')]").click()
delay()

driver.find_element(By.XPATH, "//div[@class='vector-toc-text'][contains(.,'3.3Model nomenclature')]").click()
delay()

driver.find_element(By.XPATH, "//div[@class='vector-toc-text'][contains(.,'4Design and technology')]").click()
delay()

driver.find_element(By.XPATH, "//div[@class='vector-toc-text'][contains(.,'4.1L-finesse')]").click()
delay()

driver.find_element(By.XPATH, "//div[@class='vector-toc-text'][contains(.,'5Production')]").click()
delay()

driver.find_element(By.XPATH, "//div[@class='vector-toc-text'][contains(.,'5.1Assembly plants')]").click()
delay()

driver.find_element(By.XPATH, "//div[@class='vector-toc-text'][contains(.,'5.2Quality rankings')]").click()
delay()

driver.find_element(By.XPATH, "//div[@class='vector-toc-text'][contains(.,'6Service')]").click()
delay()

driver.find_element(By.XPATH, "//div[@class='vector-toc-text'][contains(.,'7Motorsport')]").click()
delay()

driver.find_element(By.XPATH, "//div[@class='vector-toc-text'][contains(.,'8Marketing')]").click()
delay()

driver.find_element(By.XPATH, "//div[@class='vector-toc-text'][contains(.,'8.1Lexus slogans')]").click()
delay()

driver.find_element(By.XPATH, "//div[@class='vector-toc-text'][contains(.,'9See also')]").click()

driver.quit()