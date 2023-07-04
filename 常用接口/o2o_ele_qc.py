""" 模拟饿了么下单----qc环境"""
# -*- coding:utf-8 -*-

import random,requests,json,time


def ele_order(false=None, true=None, **kwargs):
    """订单来源：饿了么"""
    url="http://candao-api-gateway.v6-qc.can-dao.com/ZtApiAction"
    json={
                "accessKey": "38163d8c1ac7bb0d",
                "ticket": "6773990f-ecb1-dd9e-fd6f-676f-77f54083",
                "actionName": "candao.order.ztPushOrder",
                "content": {
                    "extOrderId": int(time.time()),
                    "extOrderNo": "1231232",
                    "thirdSn": random.randint(1,100),
                    "longitude": "104.044891",
                    "latitude": "30.550085",
                    "storeId": "334804",
                    "extStoreName": "t_9E8aG58c7k",
                    "name": "chenyu",
                    "hiddenPhone": "A31****0151",
                    "backupPhone": [
                        "131****0154"
                    ],
                    "phone": "15017555695",
                    "address": "天府二街151号领地环球金融中心b座四川发展大厦",
                    "userNote": "顾客需要两份餐两份餐具顾客需要两份餐具顾客需要两份餐具顾客需要两份餐具顾客需要两份餐具顾客需要两份餐具顾客需要两",
                    "orderType": 1,
                    "book": 1,
                    "orderTime": "2022-2-24 15:41:43",
                    "payType": 2,
                    "orderStatus": 7,
                    "isPayed": true,
                    "thirdUserId": "11237483639",
                    "paymentDetails": [{
                        "type": 2,
                        "money": 0.23,
                        "typeName": "在线支付",
                        "num": 0
                    }],
                    "isInvoice": false,
                    "peopleNum": 0,
                    "isThirdDistribute": false,
                    "distributeTypeCode": "0000",
                    "price": 10,
                    "deliveryFee": 0.01,
                    "mealFee": 0,
                    "discountPrice": 0,
                    "merchantBearPrice": 0,
                    "thirdPlatformBearPrice": 0,
                    "merchantPrice": 35.6,
                    "commission": 0.01,
                    "cpcAmount": 0,
                    "reconciliationExtras": {
                        "chargeMode": 1,
                        "performanceServiceFee": 0,
                        "technicalServiceFee": 0,
                        "distanceFee": 0,
                        "priceFee": 0,
                        "slaFee": 0,
                        "baseShippingAmount": 0,
                        "categoryChargeFee": 0,
                        "weightChargeFee": 0,
                        "holidayChargeFee": 0
                    },
                    "ftType": {
                        "emptyProductId": true,
                        "productAberrant": true,
                        "storeAberrant": true
                    },
                    "products": [{
                            "pid": "603733",
                            "isDiscount": false,
                            "name": "豆乳米麻薯",
                            "price": 3.3,
                            "totalPrice": 1,
                            "realTimeTotalPrice": 0,
                            "addPrice": 0,
                            "num": 2,
                            "boxNum": 2,
                            "boxPrice": 0,
                            "productTagUid": 0,
                            "bagNo": "1",
                            "skus": [{
                                "skuId": "2178771",
                                "price": 18,
                                "name": "中北",
                                "isOption": false
                            }],
                            "isMatchDisProduct": false,
                            "realTimePrice": 0
                        },
                        {
                            "pid": "603733",
                            "isDiscount": false,
                            "name": "桃桃生牛乳*大瓶",
                            "price": 1,
                            "totalPrice": 1,
                            "realTimeTotalPrice": 0,
                            "addPrice": 3,
                            "num": 5,
                            "boxNum": 1,
                            "boxPrice": 2,
                            "productTagUid": 0,
                            "bagNo": "1",
                            "skus": [{
                                "skuId": "2178771",
                                "price": 0.01,
                                "name": "小杯",
                                "isOption": false
                            }],
                            "isMatchDisProduct": false,
                            "realTimePrice": 0
                        },
            
            
                        {
                            "pid": "608493",
                            "isDiscount": false,
                            "name": "珍珠奶茶7",
                            "price": 0,
                            "totalPrice": 1.5,
                            "realTimeTotalPrice": 0,
                            "addPrice": 0,
                            "num": 1,
                            "boxNum": 1,
                            "boxPrice": 0,
                            "productTagUid": 0,
                            "bagNo": "1",
                            "skus": [{
                                "skuId": "2145234",
                                "price": 0.11,
                                "name": "大杯",
                                "isOption": false
                            }],
                            "isMatchDisProduct": false,
                            "realTimePrice": 0
                        },
                        {
                            "pid": "608493",
                            "isDiscount": false,
                            "name": "奥利奥芝士欧包--奥利奥芝士欧包--奥利奥芝士欧包",
                            "price": 0,
                            "totalPrice": 1,
                            "realTimeTotalPrice": 0,
                            "addPrice": 0,
                            "num": 10,
                            "boxNum": 1,
                            "boxPrice": 0,
                            "productTagUid": 0,
                            "bagNo": "1",
                            "skus": [{
                                "skuId": "2145234",
                                "price": 23,
                                "name": "夹心口味添加芝士搭配奥利奥",
                                "isOption": false
                            }],
                            "isMatchDisProduct": false,
                            "realTimePrice": 0
                        },

                    ],
                    "weight": 0,
                    "allowanceServiceFee": 0,
                    "isFavorites": true,
                    "baseLogisticsServiceFee": 0,
                    "distanceIncreaseFee": 0,
                    "timeIntervalMarkUpFee": 0,
                    "agentBearPrice": 0,
                    "sex": 0
                },
                "fromType": 20,
                "clientType": 50,
                "platformKey": "5f6e39eead63ef15",
                "langType": 0,
                "ip": "10.216.86.1"

       }

    res=requests.post(url=url,json=json)
    return res

if __name__=="__main__":
    res_ele_order=ele_order()
    print(res_ele_order.text)

