import requests, json, time, random
from COMMON.connectMysql import ConnectDb,db_info
from CONFIG.configPath import ROOT_PATH


def postDeliveryFdsInfo(businessId,**kwargs):
    url = "http://fds-gateway.fds-qc.can-dao.com/fds-web/fds/dispatch"
    json={
        "accessKey": "aed579eaa90710f7",
        "actionName": "candao.rider.postDeliveryInfo",
        "timestamp": 1667890039537,
        "ticket": "d201521e-fbc2-4365-9d5f-9474-beac8b5e",
        "sign": "1d3990f2487fa7f6733e78498cc5c1eb",
        "serviceType": "pos",
        "vendor": "",
        "storeId": "342737",
        "data": {
            "storeName": "开放配送建店测试1更新信息",
            "sn": "1",
            "businessId": businessId,
            "sender": {
                "name": "（百果园）鹭洲里店-测试",
                "phone": "13203559287",
                "address": "成都市武侯区鹭洲里",
                "longitude": "104.040821",
                "latitude": "30.550782"
            },
            "receiver": {
                "name": "哈利波特",
                "phone": "18665612534",
                "address": "四川省成都市武侯区富华南路",
                "longitude": "104.039379",
                "latitude": "30.549796"
            },
            "counts": 1,
            "orderType": 1,
            "orderTime": "2023-07-18 16:00:00",
            "sendTime": "2023-07-18 17:00:10",
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
            "deliverySysType": "dd",
            "extOrderId": "fntest_20230388",
            "fromType": "ele",
            "storeId": "342737",
            "mappingCode": "177747",
            "subStoreId": "177747"
        }
    }
    res=requests.post(url=url,json=json,verify=False)
    print(res.text)
    return res


def select_deliveryId(deliveryOrderId):
    db=ConnectDb(db_info)  #实例化
    # 呼叫生成的运单order_id查询出delivery_id并赋值到sql语句中
    # delivery_order的id关联delivery_info_record的delivery_id
    select_id = 'SELECT id from delivery_info_record where delivery_id = {}'.format(deliveryOrderId);
    res1 = db.select_sql(select_id)
    #print(res1)
    if res1:
        delivery_inforecord_Id = res1[0].get('id')
        print("呼叫记录id："+str(delivery_inforecord_Id))
        return delivery_inforecord_Id


#通过获取的ID，传入回调接口，骑手接单
def deliveryStatusChange(driverStatus,reson,delivery_inforecord_Id,**kwargs):
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
                "updateTime": time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),
                "deliverySysType": "fds",
                "extOrderId": "",
                "orderId": delivery_inforecord_Id,
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


