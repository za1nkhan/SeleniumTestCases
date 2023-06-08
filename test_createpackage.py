# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCreatepackage():
  def setup_method(self, method):
    # self.driver = webdriver.Chrome()
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_argument("--headless")
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--headless")
    edge_options = webdriver.EdgeOptions()
    edge_options.add_argument("--headless")
    drivers = [webdriver.Chrome(options=chrome_option), webdriver.Firefox(options=firefox_options),
               webdriver.Edge(options=edge_options)]
    self.driver = drivers[0]
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_createpackage(self):
    # Test name: Create package
    # Step # | name | target | value
    # 1 | open | https://rudy.visaic.com.ua/packages | 
    self.driver.get("https://rudy.visaic.com.ua/packages")
    # 2 | setWindowSize | 1200x1120 | 
    self.driver.set_window_size(1200, 1120)
    # 3 | click | id=email | 
    self.driver.find_element(By.ID, "email").click()
    # 4 | type | id=email | usah.admin@visaic.com
    self.driver.find_element(By.ID, "email").send_keys("usah.admin@visaic.com")
    # 5 | click | id=password | 
    self.driver.find_element(By.ID, "password").click()
    # 6 | type | id=password | usah1234
    self.driver.find_element(By.ID, "password").send_keys("usah1234")
    # 7 | click | css=.btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    # 8 | click | linkText=Add new package | 
    self.driver.find_element(By.LINK_TEXT, "Add new package").click()
    # 9 | click | id=name | 
    self.driver.find_element(By.ID, "name").click()
    # 10 | type | id=name | test package
    self.driver.find_element(By.ID, "name").send_keys("test package")
    # 11 | click | css=.codex-editor__redactor | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".codex-editor__redactor")
    self.driver.execute_script("arguments[0].click();", element)
    # 14 | editContent | css=.ce-paragraph | test trial
    element2 = self.driver.find_element(By.CSS_SELECTOR, ".codex-editor__redactor")
    self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = 'test trial'}", element2)
    # 15 | click | css=.mt-2 span | 
    self.driver.find_element(By.CSS_SELECTOR, ".mt-2 span").click()
    # 16 | click | name=submit-button | 
    self.driver.find_element(By.NAME, "submit-button").click()
    # 17 | click | css=tr:nth-child(1) .btn > .fa | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .btn > .fa").click()
    # 18 | click | linkText=Delete package | 
    self.driver.find_element(By.LINK_TEXT, "Delete package").click()
    # 19 | mouseOver | linkText=Delete package | 
    element = self.driver.find_element(By.LINK_TEXT, "Delete package")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 20 | mouseOut | linkText=Delete package | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 21 | click | css=.confirm-btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".confirm-btn").click()
    # 22 | click | css=.fa-angle-down |
    self.driver.find_element(By.CSS_SELECTOR, ".fa-angle-down").click()
    # 23 | click | linkText=Logout |
    element2 = self.driver.find_element(By.CSS_SELECTOR, ".dropdown-item:nth-child(3)")
    self.driver.execute_script("arguments[0].click();", element2)
  
