# -*- coding: utf-8 -*-
# auth=chenyubo
import allure
import pytest

@allure.feature("登录模块")
class TestLogin():
    TEST_CASE_FILE='https://www.baidu.com'
    @allure.story("登录成功")
    @allure.testcase(TEST_CASE_FILE,'外部测试链接')
    def test_login_success(self):
        with allure.step("步骤1：打开登录页面"):
            print("打开登录页面")
        with allure.step("步骤2：输入正确的用户名和密码"):
            print("输入正确用户名和密码")
        with allure.step("步骤3：点击登录按钮"):
            print("点击登录")

        print("测试登录成功")

    @allure.story("登录失败")
    def test_login_fail(self):
        print("测试登录失败")

    @allure.story("登录超时")
    def test_login_longtime(self):
        print("测试登录超时")

@allure.feature("支付模块")
class TestPayOrder():
    @allure.story("支付成功")
    @allure.title("测试支付成功场景")
    def test_pay_success(self):
        print("订单支付成功")

    @allure.title("测试支付失败场景")
    @allure.story("支付失败")
    def test_pay_fail(self):
        print("订单支付失败")

    @allure.title("测试超时支付场景")
    @allure.story("超时支付")
    def test_pay_cancle(self):
        print("订单超时支付")

    @allure.title("测试重复支付场景")
    @allure.story("重复支付")
    def test_pay_repeat(self):
        print("订单重复支付")