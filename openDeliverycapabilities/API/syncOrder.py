import requests,json,time,random

def syncDeliveryStatus(deliveryOrderId,**kwargs):
    url= url="http://fds-gateway.fds-qc.can-dao.com/fds-web/fds/dispatch"
    json={
        "accessKey": "a1986c922435ec9d",
        "actionName": "candao.rider.syncDeliveryStatus",
        "timestamp": 1667874667421,
        "ticket": "6457d677-e610-9801-6c94-3b58-41620410",
        "sign": "47e9f3f47ede1d226dfd74ce32af7354",
        "serviceType": "pos",
        "vendor": "",
        "storeId": "342737",
        "data": {
            "driverStatus": 15,
            "code": "1",
            "extOrderId": "",
            "deliveryOrderId": deliveryOrderId,
            "orderId": ""
        }
    }
    res=requests.post(url=url,json=json,verify=False)
    print(res.text)
    return res