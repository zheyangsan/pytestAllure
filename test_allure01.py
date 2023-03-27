# -*- coding: utf-8 -*-
# auth=chenyubo
import os
import sys

import pytest
import allure

@allure.feature('test_success')
def test_success():
    """this test succeeds"""
    assert True
@allure.feature('test_failure')
def test_failure():
    """this test fails"""
    assert False

@allure.feature('test_skip')
def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')

@allure.feature('test_broken')
def test_broken():
    raise Exception('oops')

@allure.feature('test_xfail_expected_failure')
@pytest.mark.xfail(reason='该功能还未实现')
def test_xfail_expected_failure():
    print("该功能还未实现...")
    assert False

@allure.feature('test_skipif')
@pytest.mark.skipif('win' in sys.platform,reason='操作系统是windows,执行时跳过此条用例')
def test_skipif():
    print("当前操作系统是windows,此条用例跳过，不用执行")


#------------------------------------------------------------------------------


@allure.step('测试步骤一：测试可以成功出2个参数')
def first_step(step_param1,step_param2=None):
    print(step_param1,step_param2)

@pytest.mark.parametrize('param1',['这是第1个参数','这是第2个参数','这是第3个参数'],ids=['1','2','3'])
def test_first_step_with_one_parameters(param1):
    first_step(param1)

@pytest.mark.parametrize('param1',['param1_01','param1_02','param1_03'],ids=['1','2','3'])
@pytest.mark.parametrize('param2',['param2_01','param2_02','param2_03'],ids=['a','b','c'])
def test_first_step_with_two_parameters(param1,param2):
    '''会将param1和param2的参数组合后，执行用例'''
    first_step(param1,param2)



@allure.step('测试步骤二')
def second_step():
    third_step()

@allure.step('测试步骤三')
def third_step():
    pass
@allure.step("初始测试步骤")
def test_with_steps():
    first_step(200)
    second_step()

#--------------------------------------------------------------------------------------

