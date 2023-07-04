import time
from API.createStore import cerate_deliveryStore

def test_addStore():
    '''创建门店成功'''
    c_as=cerate_deliveryStore("开放配送创建测试门店")
    print("创建门店成功"+c_as.text)
    assert c_as.json()['status'] == 1
    "取出门店id"
    print("创建门店成功:"+c_as.text)










