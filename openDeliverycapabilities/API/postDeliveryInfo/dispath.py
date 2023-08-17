import requests,json,time,random

def deliveryStatusChange(driverStatus,updateTime,reson,delivery_infoRecord_Id,**kwargs):
    url="http://fds-gateway.fds-qc.can-dao.com/fds-web/delivery/call_back"
    json={
            "accessKey": "3ddeb3649a32b24d",
            "actionName": "candao.rider.pushDeliveryStatus",
            "timestamp": 1628667007975,
            "ticket": "ce1e3033-74a5-99b6-9b38-b4fe-b5a545ab",
            "sign": "955af304ba8648dbb170c84123f973c8",
            "serviceType": "delivery",
            "vendor": "",
            "data": {
                "deliveryOrderNo": "1392823576855328548",
                "driverStatus": driverStatus,
                "reason": reson,
                "realPrice":"2",
                "totalPrice": "2",
                "fee": "1.8",
                "distance": "7000",
                "riderId": "64564",
                "riderName": "吴彦祖",
                "riderPhone": "18888888888",
                "longitude":"116.289654",
                "latitude":"40.055338",
                "updateTime": updateTime,
                "deliverySysType": "fds",
                "extOrderId": "",
                "orderId": delivery_infoRecord_Id,
                "deliveryOrderId": "481862286536433386",
                "isSupplement": False,
                "accessKey": "fe13c70dec77af3b",
                "storeId": "147534",
                "shopId": 13886
            }
        }
    json.update(kwargs)
    res = requests.post(url=url, json=json, verify=False)
    return res
