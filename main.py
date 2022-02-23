from selenium.webdriver.common.by import By
from abc import ABC
import time

class PageElement(ABC):
    def __init__(self, webdriver, url=''):
        self.webdriver = webdriver
        self.url = url

    def open(self):
        self.webdriver.get(self.url)

class Login(PageElement):
    usrName = (By.ID, "txtUsername")
    pw = (By.ID, "txtPassword")
    joinLogin = (By.ID, "btnLogin")

    def login(self, usrName, pw):
        self.webdriver.find_element(*self.usrName).send_keys(usrName)
        self.webdriver.find_element(*self.pw).send_keys(pw)
        self.webdriver.find_element(*self.joinLogin).click()
        time.sleep(20)
        self.webdriver.close()

from selenium import webdriver
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
webdriver = webdriver.Chrome()

url = "https://opensource-demo.orangehrmlive.com/"

login_page = Login(webdriver, url)
login_page.open()

login_page.login(usrName="Admin", pw="admin123")