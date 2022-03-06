"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def find_click(self, by, locator):
        # 找到之后完成点击操作
        self.find(by, locator).click()

    def find_send_keys(self, by, locator, text):
        # 找到之后完成点击操作
        self.find(by, locator).send_keys(text)

    def back(self, num=3):
        # 封装返回方法
        for i in range(num):
            self.driver.back()
