import time
from API.openDelivery import openDeliveryAuth

def test_getAuth():
    '''获取授权链接'''
    c_as=openDeliveryAuth()
    print("获取授权链接成功"+c_as.text)
    assert c_as.json()['status'] == 1

