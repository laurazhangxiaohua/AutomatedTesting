from selenium import webdriver


class BasePage:

    def __init__(self):
        global driver
        #打开浏览器
        self.driver = webdriver.Chrome()
        driver = self.driver
        self.driver.maximize_window()
        #打开页面
        self.driver.get("http://tuoguan.sftest1234.com:92/UserNameLogin.aspx")
    #定位元素
    def locator_element(self,loc):
        print(loc)
        return self.driver.find_element(loc)
    #设置值的关键字
    def set_keys(self,loc,value):
        self.locator_element(loc).send_keys(value)