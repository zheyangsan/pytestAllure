# -*- coding: utf-8 -*-
# auth=chenyubo
import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
class TestDemo():
    @allure.feature("百度搜索")
    @allure.testcase("https://www.baidu.com")
    @allure.title('测试搜索正向功能')
    @pytest.mark.parametrize('keywords',('chatgpt','allure','python'))
    def test_search(self,keywords):

        with allure.step("打开百度网页"):
            driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
            driver.get("https://www.baidu.com")
            driver.maximize_window()

        with allure.step(f"搜索框关键字-{keywords},点击搜索"):
            driver.find_element(By.ID,'kw').send_keys(keywords)
            time.sleep(2)
            driver.find_element(By.ID,'su').submit()
            time.sleep(2)
        with allure.step("截图"):
            driver.save_screenshot(filename=f"../files/screenshots/{keywords}.jpg")
            allure.attach.file(source=f"../files/screenshots/{keywords}.jpg", name=f"{keywords}.jpg", attachment_type=allure.attachment_type.JPG)
        with allure.step("关闭浏览器"):
            driver.quit()