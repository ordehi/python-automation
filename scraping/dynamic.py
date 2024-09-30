from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

url = "https://automated.pythonanywhere.com/"


def get_driver(url):
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--log-level=3")
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    service = Service(
        "C:\\Users\\ordeh\\dev\\learn\\python\\autos\\browsers\\chromedriver-win64\\chromedriver.exe")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    return driver


def clean_text(text):
    """Extract the temperature from text"""
    output = float(text.split(": ")[1])
    return output


def main():
    driver = get_driver(url)
    time.sleep(2)
    # element = driver.find_element(by="xpath",
    #                               value='/html/body/div[1]/div/h1[2]')
    element = driver.find_element(By.CSS_SELECTOR,
                                  value='#displaytimer')
    return clean_text(element.text)


print(main())
