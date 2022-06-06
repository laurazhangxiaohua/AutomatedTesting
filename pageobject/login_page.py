from selenium.webdriver.common.by import By

from base.base_page import BasePage



class LoginPage(BasePage):

    #页面元素
    username_loc = (By.ID,"txtusername")
    password_loc = (By.ID,"txtpwd")
    submit_loc =  (By.ID,"btnsubmit")
    #页面操作
    def login_pc(self,username,password,button):
        self.set_keys()
        self.set_keys()
        self.set_keys()