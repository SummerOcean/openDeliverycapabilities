import requests,json,time,random

def cerate_deliveryStore(storeName,**kwargs):
    url="http://fds-gateway.fds-qc.can-dao.com/fds-web/fds/dispatch"
    json={
        "accessKey": "aed579eaa90710f7",
        "actionName": "candao.rider.deliveryStoreInfo",
        "timestamp": 1644562168813,
        "ticket": "3d7209ac-47d0-ac03-e9a7-5f56-8635bd66",
        "sign": "870b279affdf1dcff33ceb5dc0e044e9",
        "serviceType": "pos",
        "vendor": "",
        "data": {
            "operationType": "add",
            "brandId": "4683",
            "subStoreId": "int(time.time())",
            "phone": "18584853382",
            "name": "eden1",
            "storeName": storeName,
            "address": "青羊区墨香雅轩文化艺术服务中",
            "longitude": "104.065453",
            "latitude": "30.673095",
            "storeCategory": "",
            "storeSecCategory": "",
            "idNumber": "",
            "idNumberUrl": "123url",
            "suCode": "suCode",
            "legalPerson": "legalPerson",
            "legalPersonContactPhone": "1310001111",
            "legalPersonIdCardNo": "legalPersonIdCardNo",
            "idNumberFanUrl": "idNumberFanUrl",
            "businessLicenceUrl": "businessLicenceUrl",
            "foodLicensePicUrl": "foodLicensePicUrl"
                  }
        }
    res=requests.post(url=url,json=json,verify=False)
    print(res.text)
    return res

if __name__=='__main__':
    cerate_deliveryStore("开放配送测试建店")


