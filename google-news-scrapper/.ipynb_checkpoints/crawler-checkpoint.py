from selenium import webdriver
from bs4 import BeautifulSoup as bs
from bs4.element import Tag
import re

def initiate_crawler():
    
    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--allow-insecure-localhost')
    chrome_options.add_argument('--allow-running-insecure-content')
    chrome_options.add_argument("--disable-quic")  # not "--disable-quic"

    capabilities = chrome_options.to_capabilities()
    capabilities['acceptInsecureCerts'] = True
    capabilities['acceptSslCerts'] = True
    driver = webdriver.Chrome(chrome_options=chrome_options, desired_capabilities=capabilities)

    return driver

def shutdown_crawler(driver):

    driver.close()
    driver.quit()