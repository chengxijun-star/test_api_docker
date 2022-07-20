import pytest

import os

if __name__ == '__main__':
    pytest.main(['-s','-v','./case','--alluredir=./allure'])
    os.system("allure generate ./allure -o ./report --clean")