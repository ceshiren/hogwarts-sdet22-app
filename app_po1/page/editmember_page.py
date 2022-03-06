"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from app_po1.base.wework_app import WeWorkApp


class EditMemberPage(WeWorkApp):
    def edit_member(self, name, phonenum):
        # input name
        # input phonenum
        # click 保存
        from app_po1.page.addmember_page import AddMemberPage
        # self.driver.find_element(MobileBy.XPATH,
        #                          '//*[contains(@text, "姓名")]/../*[@text="必填"]'). \
        #     send_keys(name)
        self.find_send_keys(MobileBy.XPATH,
                            '//*[contains(@text, "姓名")]/../*[@text="必填"]',
                            name)

        # self.driver.find_element(MobileBy.XPATH,
        #                          "//*[contains(@text, '手机')]/..//*[@text='必填']"). \
        #     send_keys(phonenum)
        self.find_send_keys(MobileBy.XPATH,
                            "//*[contains(@text, '手机')]/..//*[@text='必填']",
                            phonenum)

        self.find_click(MobileBy.XPATH, "//*[@text='保存']")

        return AddMemberPage(self.driver)
