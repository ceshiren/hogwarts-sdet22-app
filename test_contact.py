"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


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
        caps["noReset"] = "True"
        # 最重要的一句，与远程服务建立连接，返回一个 session 对象
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 在调用find_element() 的时候,会每隔0.5秒查找一次元素，
        self.driver.implicitly_wait(5)

    def teardown(self):
        # 关闭应用
        self.driver.quit()

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
