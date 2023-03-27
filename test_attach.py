# -*- coding: utf-8 -*-
# auth=chenyubo

import allure
import pytest
@pytest.fixture
def attach_for_text():
    '''allure.attach.不会在报告中展示附件内容'''
    allure.attach(body="这是一段文本,setUp", name="test文本01", attachment_type=allure.attachment_type.TEXT)
    yield
    allure.attach(body="这是一段文本,teardown", name="test文本02", attachment_type=allure.attachment_type.TEXT)

@pytest.fixture
def attach_for_file():
    '''allure.attach.file可以在报告中展示附件内容'''
    allure.attach.file(source='./files/images01.jpg',name="美景",attachment_type=allure.attachment_type.JPG)
    yield
    allure.attach.file(source='./files/video01.mp4',name="文件",attachment_type=allure.attachment_type.MP4)

@pytest.fixture
def get_sum():
    return 1+1
@allure.description("写个测试用例，直接调用pytest.feature函数")
def test_attachment_text(attach_for_text):
    pass

@allure.description_html("""
<h1>这是一段html描述</h1>
<img src="files/a.jpg">
""")
def test_attach_for_file(attach_for_file):
    pass

def test_get_sum(get_sum):
    """计算1+1=2"""
    pass