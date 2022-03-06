"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from app_po1.base.wework_app import WeWorkApp


class AddMemberPage(WeWorkApp):

    def click_addbymenual(self):
        # click 手动输入添加
        self.find_click(MobileBy.XPATH,
                        "//*[@text='手动输入添加']")
        from app_po1.page.editmember_page import EditMemberPage
        return EditMemberPage(self.driver)

    def get_result(self):
        # get toast text
        element_toast = self.find(MobileBy.XPATH,
                                  "//*[@class='android.widget.Toast']")
        result = element_toast.get_attribute("text")
        return result
