from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from types import SimpleNamespace as Namespace
from time import sleep
import json

class Account():
    def __init__(self, home_url, login_url, username, password):
        self.home_url = home_url
        self.login_url = login_url
        self.username = username
        self.password = password

    def getHomeUrl(self):
        if self.home_url: return self.home_url

    def getLoginUrl(self):
        if self.login_url: return self.login_url

    def getUsername(self):
        if self.username: return self.username

    def getPassword(self):
        if self.password: return self.password  


def read_json():
    account_file = 'json/account.json'
    with open(account_file, 'r') as f:
        config = json.load(f, object_hook=lambda d: Namespace(**d))

    global home_url, login_url, username, password
    home_url = config.url.home
    login_url = config.url.login
    username = config.account.username
    password = config.account.password

    account = Account(home_url, login_url, username, password)

    return account

def findClassElement(driver, class_name):
    return driver.find_element(By.CLASS_NAME, class_name)

def findClassElements(driver, class_name):
    return driver.find_elements(By.CLASS_NAME, class_name)

def findXpathElements(driver, xpath_name):
    return driver.find_elements(By.XPATH ,xpath_name)

def findXpathElement(driver, xpath_name):
    return driver.find_element(By.XPATH ,xpath_name)

def scroll(driver):
    # driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    driver.execute_script("window.scrollBy(0, 6000);")
    sleep(5)

def potatomediaLogin(driver): #登入
    #get account

    input = findClassElement(driver, 'forms-form__FormInputInput--4ZfCG')
    input.send_keys(username)
    input = findClassElement(driver, 'elements-text-button__TextButton--Ba1mj.elements-text-button__TextButton--theme-filled--kI1ER') 
    input.send_keys(Keys.ENTER)
    sleep(2)
    pwd = findClassElement(driver, 'forms-form__FormInputInput--4ZfCG')
    pwd.send_keys(password)
    pwd = findClassElement(driver, 'elements-text-button__TextButton--Ba1mj.elements-text-button__TextButton--theme-filled--kI1ER') 
    pwd.send_keys(Keys.ENTER)
    sleep(2)
