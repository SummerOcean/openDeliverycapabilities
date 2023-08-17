import time
from API.postDeliveryInfo.getPreview import previewDeliveryFe
from API.postDeliveryInfo.postDeliveryInfo import postDeliveryInfo


def test_postDelivery():
    '''1、获取预览费用和编号'''
    businessId = "fdstest" + str(int(time.time()))

    '''打印出订单号'''
    print("订单号:" + businessId)

    p_d = previewDeliveryFe(businessId)
    print("获取预览费用成功:" + p_d.text)

    '''断言'''
    assert p_d.json()['status'] == 1

    "获取出预览费用的编号"
    previewFeeOrderNo = p_d.json()['data']['previewFeeOrderNo']
    print('预览费用编号：' + previewFeeOrderNo)
    '''    '''

    '''2、下单呼叫'''
    p_d_i=postDeliveryInfo(businessId,previewFeeOrderNo)
    '''断言'''
    assert p_d_i.json()['status'] == 1
    d_o=p_d_i.json()['data']['deliveryOrderId']
    print('配送单号：%d' %d_o)




