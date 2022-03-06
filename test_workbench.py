"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import datetime
import time
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException


class TestWorkbench:

    def setup(self):
        # 打开应用
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "hogwarts"
        # mac/linux:  adb logcat ActivityManager:I | grep "cmp"
        # windows:   adb logcat ActivityManager:I | findstr "cmp"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps['skipServerInstallation'] = 'true'  # 跳过 uiautomator2 server的安装
        caps['skipDeviceInitialization'] = 'true'  # 跳过设备初始化
        # caps['settings[waitForIdleTimeout]']= 0  # 等待页面完全加载完成的时间
        caps["noReset"] = "True"
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

    def get_time(self):
        t = time.localtime()
        cur_time = time.strftime("%Y-%m-%d_%H:%M:%S", t)
        print(f"当前时间为：{cur_time}")

    def test_daka(self):
        """
        前提条件：
            1、提前注册企业微信管理员帐号
            2、手机端安装企业微信
            3、企业微信 app 处于登录状态
        实现打卡功能
            打开【企业微信】应用
            进入【工作台】页面
            点击【打卡】
            选择【外出打卡】tab
            点击【第 N 次打卡】
            验证点：提示【外出打卡成功】
        """
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        # 滑动查找
        self.swipe_find("打卡").click()
        # self.driver.update_settings({"waitForIdleTimeout": 0})
        # print(time.time())
        self.get_time()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        # print(time.time())
        self.get_time()
        # 验证
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']")
