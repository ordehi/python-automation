from selenium import webdriver
from selenium.webdriver.chrome.service import Service

url = "https://blog.ordehi.dev/"


def get_driver(url):
    options = webdriver.ChromeOptions()
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


def main():
    driver = get_driver(url)
    element = driver.find_element(by="xpath",
                                  value='//*[@id="__next"]/div/main/section[1]/small')
    return element.text


print(main())
