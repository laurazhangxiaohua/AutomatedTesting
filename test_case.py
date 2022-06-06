import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCase(unittest.TestCase):

    def test_01_login(self):
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://tuoguan.sftest1234.com:92/UserNameLogin.aspx")
        time.sleep(2)

        driver.find_element(By.ID,"txtusername").send_keys("betacs1jl")
        driver.find_element(By.ID,"txtpwd").send_keys("111111aA")
        driver.find_element(By.ID,"btnsubmit").click()

    def test_02_review_account(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("http://tuoguan.sftest1234.com:92/UserNameLogin.aspx")
        time.sleep(2)
        driver.find_element(By.ID,"txtusername").send_keys("betacs1jl")
        driver.find_element(By.ID,"txtpwd").send_keys("111111aA")
        driver.find_element(By.ID,"btnsubmit").click()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT,"职工通福利管理").click()
        time.sleep(2)
        card_list = driver.find_elements(By.NAME,"chkElectronicCardNo")
        card_list[0].click()
        release_card_list = driver.find_elements(By.LINK_TEXT,"发放")
        release_card_list[0].click()
        time.sleep(4)
        driver.find_element(By.ID,"userNameInput").send_keys("测试张小花")
        driver.find_element(By.XPATH,"//input[@value='查询']").click()
        driver.find_element(By.ID,"grantELectronic").click()
        driver.find_element(By.ID,"btnYes").click()
        time.sleep(4)
        driver.find_element(By.ID,"closeMaxBoxBtn").click()