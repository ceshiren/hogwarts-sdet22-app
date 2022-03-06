"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from app_po1.base.wework_app import WeWorkApp
from app_po1.page.addmember_page import AddMemberPage


class AddressListPage(WeWorkApp):

    def click_addmemeber(self):
        # click 添加成员
        self.find_click(MobileBy.XPATH,
                        "//*[@text='添加成员']")
        return AddMemberPage(self.driver)
