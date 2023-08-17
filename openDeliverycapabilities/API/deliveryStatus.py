from COMMON.connectMysql import ConnectDb,db_info
from requests import post
import requests,json,time


'''手动呼叫生成配送单,call_rider生成配送单，未返回配送单号，再通过连接数据库去查询配送单号'''
def callRider(s,order_id,**kwargs):
    url="http://fds-gateway.fds-qc.can-dao.com/fds-web/delivery/call/rider"
    json={
	    "data": {
		        "deliveryCompanys":
                    [{
                        "companyId": 54,
			            "name": "闪送",
			            "beforeDeliveryFee": 21.4,
			            "deliveryFee": 21.6,
                        "juHeDelivery": False,
                        "companyType": 2,
                        "deliveryStatus": 0,
                        "gradient": 1,
                        "addDirectServiceFee": "False"
                    }],
                "orderId": order_id,
                "storeId": "167042"
                },
	    "platformKey": "1e2da0f14e0fc3e8",
        }
    json.update(kwargs)
    res1=s.post(url=url,json=json,verify=False)
    return res1


def select_deliveryId(order_id):
    db = ConnectDb(db_info)   #实例化
    # 呼叫生成的运单order_id查询出delivery_id并赋值到sql语句中
    # delivery_order的id关联delivery_info_record的delivery_id
    select_id = 'SELECT id from delivery_info_record where delivery_id = {}'.format(order_id);
    res1 = db.select_sql(select_id)
    #print(res1)
    if res1:
        deliveryId = res1[0].get('id')
        print("配送单号："+str(deliveryId))
        return deliveryId






#通过获取的ID，传入回调接口，骑手接单
def deliveryStatusChange(driverStatus,reson,delivery_info_record_id,**kwargs):
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
                "orderId": delivery_info_record_id,
                "deliveryOrderId": "481862286536433386",
                "isSupplement": False,
                "accessKey": "fe13c70dec77af3b",
                "storeId": "147534",
                "shopId": 13886
            }
        }
    json.update(kwargs)
    res = post(url=url, json=json, verify=False)
    return res


#通过获取的ID，传入回调接口，骑手接单
def deliveryStatusChange1(driverStatus,updateTime,reson,delivery_info_record_id,**kwargs):
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
                "orderId": delivery_info_record_id,
                "deliveryOrderId": "481862286536433386",
                "isSupplement": False,
                "accessKey": "fe13c70dec77af3b",
                "storeId": "147534",
                "shopId": 13886
            }
        }
    json.update(kwargs)
    res = post(url=url, json=json, verify=False)
    return res







