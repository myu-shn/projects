from selenium import webdriver
from bs4 import BeautifulSoup as bs
from bs4.element import Tag
import re
import random

def initiate_crawler():
    user_agents = [ 
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36', 
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36', 
        'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148', 
        'Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36' 
    ] 
    user_agent = random.choice(user_agents) 

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
    chrome_options.add_argument(f"user-agent={user_agent}")

    capabilities = chrome_options.to_capabilities()
    capabilities['acceptInsecureCerts'] = True
    capabilities['acceptSslCerts'] = True
    driver = webdriver.Chrome(chrome_options=chrome_options, desired_capabilities=capabilities)
    
    return driver

def shutdown_crawler(driver):

    driver.close()
    driver.quit()