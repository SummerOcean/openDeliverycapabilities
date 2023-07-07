import requests, json, time, random


def postDeliveryInfo(businessId,previewFeeOrderNo,**kwargs):
    url = "http://fds-gateway.fds-qc.can-dao.com/fds-web/fds/dispatch"
    json = {
        "accessKey": "aed579eaa90710f7",
        "actionName": "candao.rider.postDeliveryInfo",
        "timestamp": 1667890039537,
        "ticket": "d201521e-fbc2-4365-9d5f-9474-beac8b5e",
        "sign": "1d3990f2487fa7f6733e78498cc5c1eb",
        "serviceType": "pos",
        "vendor": "",
        "storeId": "342737",
        "previewFeeOrderNo":previewFeeOrderNo,
        "data": {
            "storeName": "开放配送建店测试1更新信息",
            "sn": "1",
            "businessId": businessId,
            "sender": {
                "name": "（百果园）中山古镇镇富兴路店",
                "phone": "13203559287",
                "address": "海淀区清河龙岗路51号清润家园小区 永辉",
                "longitude": "116.35",
                "latitude": "40.03"
            },
            "receiver": {
                "name": "顺丰同城",
                "phone": "18665612534",
                "address": "奥园体育俱乐部",
                "longitude": "116.37",
                "latitude": "40.03"
            },
            "counts": 1,
            "orderType": 1,
            "orderTime": "2023-3-20 16:00:00",
            "sendTime": "2023-3-20 17:00:10",
            "payType": 2,
            "isInvoice": False,
            "invoiceType": 0,
            "productPrice": 56.0,
            "deliveryFee": 0.0,
            "mealFee": 0.0,
            "currencyType": 0,
            "price": 56.0,
            "tablewareRecycling": False,
            "merchantPrice": 56.0,
            "discountPrice": 0.0,
            "weight": 6000,
            "distance": 4000,
            "products": [
                {
                    "name": "张亮麻辣烫",
                    "price": 56.0,
                    "num": 1
                }
            ],
            "deliverySysType": "fds",
            "extOrderId": "fntest_202303070401",
            "fromType": "ele",
            "storeId": "342737",
            "mappingCode": "177747",
            "subStoreId": "177747"
        }
    }
    res=requests.post(url=url,json=json,verify=False)
    print(res.text)
    return res
