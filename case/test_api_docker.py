import allure
import pytest


@allure.feature("WESAPI测试")
class TestReceiveWMSData(object):
    @allure.title("测试WMS下发PLU主数据接口")
    @allure.story("WMS下发PLU主数据")
    @allure.link("",name="receiveWmsData")
    def test_reveive_wms_data(self):
        with allure.step("调用接口下发主数据"):
            pass
        with allure.step("查询数据库"):
            pass

    @allure.title("测试WCS修改PLU主数据接口")
    @allure.story("Wcs修改PLU主数据")
    @allure.link("", name="updateData")
    def test_update_data(self):
        with allure.step("调用接口修改主数据"):
            pass
        with allure.step("查询数据库"):
            pass