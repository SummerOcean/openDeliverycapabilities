import requests,json,time,random

def openDeliveryAuth(**kwargs):
        url="http://fds-gateway.fds-qc.can-dao.com/fds-web/fds/dispatch"
        json={
            "accessKey": "aed579eaa90710f7",
            "actionName": "candao.rider.getAuthUrl",
            "timestamp": 1644562168813,
            "ticket": "3d7209ac-47d0-ac03-e9a7-5f56-8635bd66",
            "sign": "870b279affdf1dcff33ceb5dc0e044e9",
            "serviceType": "pos",
            "vendor": "",
            "data": {
                "type": "0",
                "storeId": "342737",
                "deliverySysType": "sf",
                "redirectUrl": "https://www.baidu.com"
        }

    }
        res=requests.post(url=url,json=json,verify=False)
        print(res.text)
        return res


