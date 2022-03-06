"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from app_po1.base.wework_app import WeWorkApp
from app_po1.page.addresslist_page import AddressListPage


class MainPage(WeWorkApp):
    _addresslist_element = (MobileBy.XPATH,
                            "//*[@text='通讯录']")

    def goto_addresslist(self):
        # click 通讯录
        self.find_click(*self._addresslist_element)
        return AddressListPage(self.driver)
