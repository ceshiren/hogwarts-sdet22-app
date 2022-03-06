"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class TestContact:

    def setup(self):
        # 打开应用
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "hogwarts"
        # mac/linux:  adb logcat ActivityManager:I | grep "cmp"
        # windows:   adb logcat ActivityManager:I | findstr "cmp"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = True

        # desired_caps = {}
        # desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '6.0'
        # desired_caps['deviceName'] = 'emulator-5554'
        # desired_caps['appPackage'] = 'com.tencent.wework'
        # desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
        # desired_caps['noReset'] = 'true'
        # 最重要的一句，与远程服务建立连接，返回一个 session 对象
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 在调用find_element() 的时候,会每隔0.5秒查找一次元素，
        self.driver.implicitly_wait(5)

    def teardown(self):
        # 关闭应用
        self.driver.quit()

    def swipe_find(self, text, num=3):
        # 滑动查找元素
        self.driver.implicitly_wait(1)
        for i in range(num):
            try:
                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                return element
            except:
                print("未找到")
                size = self.driver.get_window_size()
                # 'width', 'height'
                width = size.get("width")
                height = size.get("height")
                start_x = width / 2
                start_y = height * 0.8
                end_x = start_x
                end_y = height * 0.3
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=2000)

            if i == num - 1:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"找了{num}次，未找到")

    def test_add_contact(self):
        """
        前提条件：
            1、提前注册企业微信管理员帐号
            2、手机端安装企业微信
            3、企业微信 app 处于登录状态
        通讯录添加成员用例步骤
            打开【企业微信】应用
            进入【通讯录】页面
            点击【添加成员】
            点击【手动输入添加】
            输入【姓名】【手机号】并点击【保存】
        :return:
        """
        name = "lili1"
        phonenum = "13712345679"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # find_element 是第一次找到的元素，找到就返回
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='必填']").send_keys(name)
        # self.driver.find_elements(MobileBy.XPATH, "//*[@text='必填']")[0].send_keys(name)
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[contains(@text, "姓名")]/../*[@text="必填"]'). \
            send_keys(name)

        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text, '手机')]/..//*[@text='必填']"). \
            send_keys(phonenum)

        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        element_toast = self.driver.find_element(MobileBy.XPATH,
                                                 "//*[@class='android.widget.Toast']")
        result = element_toast.get_attribute("text")
        # 断言
        assert "添加成功" == result
        # 辅助查看页面布局的方法
        # while True:
        #     current_xml = self.driver.page_source
        #     if "添加成功" in current_xml:
        #         print(current_xml)
        #         break

    def wait_for_text(self, text):
        try:
            WebDriverWait(self.driver, 5). \
                until(lambda x: x.find_element(MobileBy.XPATH, f"//*[@text='{text}']"))
            return True
        except:
            return False

    def test_del_contact(self):
        """
        通讯录添加成员用例步骤
        打开【企业微信】应用
        进入【通讯录】页面
        点击右上角搜索图标，进入搜索页面
        输入搜索内容（已添加的联系人姓名）
        点击展示的第一个联系人（有可能多个），进入联系人详情页面
        点击右上角三个点，进入个人信息页面
        点击【编辑成员】进入编辑成员页面
        点击【删除成员】并确定
        验证点：搜索结果页面联系人个数少一个
        :return:
        """
        searchkey = "aaa"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # following-sibling 就是找到当前结点 后面的所有结点,如果找到多个元素，下标从1开始，比如 1,2,3...
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@text='测试公司']/../../../following-sibling::*/*[1]").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='搜索']").send_keys(searchkey)
        # sleep(2)
        # # 搜索结果分两种情况
        # # 第一种情况 ： 无结点
        # if "无搜索结果" in self.driver.page_source:
        #     pytest.xfail(reason=f"无搜索结果：{searchkey}")
        # print("有搜索结果")

        # 显式等待 是否找到联系人
        exists = self.wait_for_text("联系人")
        if not exists:
            pytest.xfail(reason=f"无搜索结果：{searchkey}")

        # 第二种情况： 有结果，删除操作
        # 判断搜索结果中的【联系人个数】 beforenum
        # find_elements  返回一个元素列表 [ele1,ele2,....]
        beforenum = len(self.driver.find_elements(MobileBy.XPATH,
                                                  "//*[@text='联系人']/../following-sibling::*"))
        # 点击第一个联系人
        self.driver.find_elements(MobileBy.XPATH,
                                  "//*[@text='联系人']/../following-sibling::*")[0].click()

        # 点击 个人信息页 的右上角的 三个点
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@text='个人信息']/../../../../following-sibling::*[1]").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        self.swipe_find("删除成员").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
        sleep(2)
        # 删除之后，再一次的拿【联系人个数】 afternum
        afternum = len(self.driver.find_elements(MobileBy.XPATH,
                                                 "//*[@text='联系人']/../following-sibling::*"))

        # 断言assert beforenum - afternum == 1
        assert beforenum - afternum == 1
