import time
from API.postDeliveryInfo.getPreview import previewDeliveryFe

def test_gePreFee():
    '''获取预览配送费'''
    businessId="fdstest" + str(int(time.time()))
    '''打印出订单号'''
    print("订单号:"+businessId)

    g_d=previewDeliveryFe(businessId)
    print("获取预览费用成功:"+g_d.text)

    '''断言'''
    assert  g_d.json()['status']==1

    "获取出预览费用的编号"
    previewFeeOrderNo=g_d.json()['data']['previewFeeOrderNo']
    print('预览费用编号：'+previewFeeOrderNo)



