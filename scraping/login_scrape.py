from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

url = "https://automated.pythonanywhere.com/login"
username = 'automated'
password = 'automatedautomated'
username_selector = 'id_username'
password_selector = 'id_password'
home_xpath = '/html/body/nav/div/a'
timer_selector = 'displaytimer'


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


def enter_text(input, text):
    input.send_keys(text)


def find_element_by_id(driver, id):
    element = driver.find_element(By.ID, id)
    return element


def find_and_input(driver, selector, text):
    input = find_element_by_id(driver, selector)
    enter_text(input, text)
    return input


def find_element_by_xpath(driver, xpath):
    return driver.find_element(By.XPATH, xpath)


def find_and_click(driver, xpath):
    element = find_element_by_xpath(driver, xpath)
    element.click()


def clean_text(text):
    """Extract the temperature from text"""
    output = float(text.split(": ")[1])
    return output


def main():
    driver = get_driver(url)

    find_and_input(driver, username_selector, username)
    password_input = find_and_input(driver, password_selector, password)
    password_input.submit()
    print(driver.current_url)

    find_and_click(driver, home_xpath)
    time.sleep(2)
    to_scrape = find_element_by_id(driver, timer_selector)

    return clean_text(to_scrape.text)


print(main())
