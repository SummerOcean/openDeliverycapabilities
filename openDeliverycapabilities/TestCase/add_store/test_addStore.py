import time

import pytest
from jsonpath import jsonpath
from API.createStore import cerate_deliveryStore


@pytest.mark.parametrize("storeName",["开放配送创建自动化测试门店"])
def test_addStore(storeName):
    '''创建门店成功'''
    c_as=cerate_deliveryStore(storeName)
    print("创建门店成功"+c_as.text)
    assert c_as.json()['status'] == 1
    assert jsonpath(c_as.json(),'$.msg')[0]=="操作成功"
    "取出门店id"
    print("创建门店成功:"+c_as.text)










