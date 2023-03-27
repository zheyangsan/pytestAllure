# -*- coding: utf-8 -*-
# auth=chenyubo
import allure

def test_no_level():
    pass
@allure.severity(allure.severity_level.TRIVIAL)
def test_trivial_case():
    pass
@allure.severity(allure.severity_level.NORMAL)
def test_normal_case():
    pass
@allure.severity(allure.severity_level.MINOR)
def test_minor_case():
    pass

@allure.severity(allure.severity_level.NORMAL)
class TestDemo(object):
    def test_class_no_level(self):
        pass
    @allure.severity(allure.severity_level.MINOR)
    def test_class_normal_case(self):
        pass