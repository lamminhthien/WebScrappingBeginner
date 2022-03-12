import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
import requests

# Selenium Action
class Selenium():
  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def open(self,urlChapter):
    self.driver.get(urlChapter)
    self.driver.set_window_size(817, 816)


# BeautifulSoup, Request action
class CrawlerAllChaper():
    def crawler(self,urlManga):
        r = requests.get(urlManga)
        r.status_code
        soup = BeautifulSoup(r.text,'html.parser')
        list = []
        for item in soup.find_all(attrs={"data-id":True,"data-rating":False}):
            list.append(item.get('href'))
        return list


# Pyauto gui action
class AutoControl():
    def autoDownload(self):
        pyautogui.hotkey('ctrl','s')
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(7)

# All instances of classes
selenium_instance = Selenium()
crawlerChapter = CrawlerAllChaper()
autoControl = AutoControl()

# Get link chapters list from CrawlerAllChapter
urlManga = "http://www.nettruyenmoi.com/truyen-tranh/tieu-thu-bi-am-sat-16690"
chapterList = crawlerChapter.crawler(urlManga)

# for loop, open and download each chapter
for urlChapter in chapterList:
    selenium_instance.setup_method()
    selenium_instance.open(urlChapter)
    autoControl.autoDownload()
    selenium_instance.teardown_method


