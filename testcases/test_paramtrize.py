# -*- coding: utf-8 -*-
# auth=chenyubo
import pytest
import yaml
class TestDemo:
    @pytest.mark.parametrize('env',yaml.safe_load(open('./config.yml')))
    def test_demo(self,env):
        if 'sit' in env:
            print(f'这是测试环境{env}')
        elif 'dev' in env:
            print(f'这是开发环境{env}')
        else:
            print(f'这是uat环境{env}')