from COMMON.connectMysql import ConnectDb,db_info
from CONFIG.configPath import ROOT_PATH
from API.postDeliveryInfo.postDeliveryFds import postDeliveryFdsInfo,select_deliveryId,deliveryStatusChange
import time


def test_status_5():
    "1.下单呼叫"
    businessId = "fdstest" + str(int(time.time()))
    p_d_f=postDeliveryFdsInfo(businessId)
    '''断言'''
    assert p_d_f.json()['status'] == 1
    deliveryOrderId = p_d_f.json()['data']['deliveryOrderId']
    print('配送单号：%d' % deliveryOrderId)

    "2.链接数据库查询呼叫记录id"
    delivery_infoRecord_Id = select_deliveryId(deliveryOrderId)
    print(delivery_infoRecord_Id)


    "3.回调已分配"
    rider_status = deliveryStatusChange(5, '已分配', delivery_infoRecord_Id)
    print("已分配" + rider_status.text)


