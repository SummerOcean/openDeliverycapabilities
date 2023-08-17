import time
from API.postDeliveryInfo.postDeliveryFds import postDeliveryFdsInfo
from API.syncOrder import syncDeliveryStatus

def test_syncDeliveryStatus():

    '''2、下单呼叫'''
    #businessId=str(int(time.time()))
    p_d_i=postDeliveryFdsInfo(str(int(time.time())))
    '''断言'''
    assert p_d_i.json()['status'] == 1
    d_o=p_d_i.json()['data']['deliveryOrderId']
    print('配送单号：%d' %d_o)





    '''3.取消待接单状态的订单'''
    s_d=syncDeliveryStatus(d_o)
    assert p_d_i.json()['status'] == 1











