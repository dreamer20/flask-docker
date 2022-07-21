from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
# driver = webdriver.Remote(
#    command_executor='http://127.0.0.1:4444/wd/hub',
#    desired_capabilities=DesiredCapabilities.CHROME)

SELENIUM_GRID_HOST = os.getenv('SELENIUM_GRID_HOST')
APP_HOST = os.getenv('APP_HOST')
APP_PORT = os.getenv('APP_PORT')


def test_in_browser(host, port):
    print(host)
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor=f'http://{SELENIUM_GRID_HOST}:4444',
        options=chrome_options
    )
    driver.get(F"http://{APP_HOST}:{APP_PORT}")
    driver.quit()
