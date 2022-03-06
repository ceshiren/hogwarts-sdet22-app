"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import pytest

from app_po1.base.wework_app import WeWorkApp


class TestContact:

    def setup_class(self):
        self.app = WeWorkApp()

    def setup(self):
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.back()

    def teardown_class(self):
        self.app.stop()

    def test_addcontact(self):
        name = "lili1"
        phonenum = "13100000001"
        result = self.main.goto_addresslist(). \
            click_addmemeber().click_addbymenual().edit_member(name, phonenum).get_result()
        assert "添加成功" == result

    def test_addcontact1(self):
        name = "lili2"
        phonenum = "13100000002"
        result = self.main.goto_addresslist(). \
            click_addmemeber().click_addbymenual().edit_member(name, phonenum).get_result()
        assert "添加成功" == result
