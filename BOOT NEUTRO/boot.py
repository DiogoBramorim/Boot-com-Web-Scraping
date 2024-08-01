import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')

import time
from bs4 import BeautifulSoup
from selenium import webdriver
import chromedriver_autoinstaller
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("URL DO SITE")

username = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, 'LINK DO TIPO XPATH DO CAMPO'))
)
username.send_keys('login')

password = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, 'LINK DO TIPO XPATH DO CAMPO'))
)
password.send_keys('senha')

login = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH,'LINK DO TIPO XPATH DO CAMPO'))
)
login.click()
acesso = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH,'LINK DO TIPO XPATH DO CAMPO'))
)
acesso.click()

solicitar = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH,'LINK DO TIPO XPATH DO CAMPO'))
)
solicitar.click()
time.sleep(5)
sair = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH,'LINK DO TIPO XPATH DO CAMPO'))
)
sair.click()
time.sleep(5)
