
import os
import pytest


if __name__ == '__main__':
    pytest.main(['-s', '-q','./test_story.py','--clean-alluredir','--alluredir=allure-results'])
    os.system(r"allure generate -c -o allure-report")
