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
driver.get("http://www.floriano.ifpi.edu.br:8080/CortexMobileIFPI/login.jsf;jsessionid=e35791f25571204316c0d9990506")

username = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="j_username"]'))
)
username.send_keys('09245915360')

password = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="j_password"]'))
)
password.send_keys('09260@sari')

login = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH,'//*[@id="j_idt6"]/div[2]/center/form/div[3]/div/input'))
)
login.click()
acesso = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH,'//*[@id="j_idt7:btnGerenciaMinhaConta"]'))
)
acesso.click()

solicitar = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH,'//*[@id="j_idt7:btnCompraTicketUsuario"]'))
)
solicitar.click()
time.sleep(5)
sair = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH,'//*[@id="j_idt7:menuPrin"]/li[4]/a'))
)
sair.click()

time.sleep(5)

driver.get("https://www.google.com/intl/pt-BR/gmail/about/")
entrar = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH,'/html/body/header/div/div/div/a[2]'))
)
entrar.click()

contaN = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH,'//*[@id="identifierId"]'))
)
contaN.send_keys('diogobamorim20@gmail.com')

ir = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH,'//*[@id="identifierNext"]/div/button/span'))
)
ir.click()

senha = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input'))
)
senha.click()
senha.send_keys('Dio@2006')

entrarG = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH,'//*[@id="passwordNext"]/div/button/span'))
)
entrarG.click()

time.sleep(5)