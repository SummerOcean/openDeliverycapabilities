import random,requests,json,time

#1800  edenstore1
#1801  edenstore2


def zt_order():
    url = "http://gateway.dms-qc.can-dao.com/receive-service/orderProcess/v2/addOrder"
    json={
        'token': '6a13073d0ed87ac6',
        'timestamp': 1686300076810,
        'originId': '1543303241126810',
        'originNo': 'eden-1543303241126810',
        'payForSupplierFee': '200',
        'deliverFee': '6.6',
        'createTime': '1687855620446',
        'info': '{"note":"送一点冰块 谢谢【如遇缺货】：缺货时电话与我沟通 收餐人隐私号 17806513350_3334，手机号 19136080630,备份隐私号:17806513350_3334","discount":12.78,"product":[{"name":"丽芝士 印度尼西亚进口 纳宝帝奶酪味威化饼干 56g","price":"4.55","count":1,"product":[]},{"name":"统一 老坛酸菜牛肉面 120g（面饼85g+配料35g）","price":"5.2","count":1,"product":[]},{"name":"👓👯🐽🐧👓👯🐰🐽👓👯🐯🐻👓👯🐰🐸范佳乐 小麦啤酒 ≥5度 450ml","price":"9.75","count":1,"product":[]},{"name":"水水水水👓👯🐽🐧👓👯🐰🐽👓👯🐯🐻👓👯🐰🐸","price":"9.75","count":1,"product":[{"name":"海带结","price":"0.0","count":2,"product":[]},{"name":"胡萝卜","price":"0.0","count":2,"product":[]}]}],"total":"29.25","extra":7.0}',
        'cargoWeight': '0.1',
        'cargoPrice': '5',
        'totalAmout': '8',
        'fetchFromReceiverFee': '10',
        'cargoNum': 2,
        'payType': 0,
        'isPrepay': '1',
        'fetchTime': 0,
        'finishTime': '1687859220000',
        'supplierId': '1800',
        'supplierName': '海格的店',
        'supplierBrandName': '大红花',
        'supplierBrandId': 4234345,
        'supplierAddress': '吉泰六路205号',
        'supplierPhone': '15680665321',
        'supplierLat': '30.650755',
        'supplierLng': '104.077682',
        'receiverName': '哈哈👓👯🐽🐧👓👯🐰🐽👓👯🐯🐻👓👯🐰🐸',
        'receiverAddress': '成都高新招商花园城',
        'receiverPhone': '19136080630',
        'receiverLat': '30.635516',
        'receiverLng': '104.068194',
        'callbackType': 1,
        'callback': 'http://qc.can-dao.com:4002/WMCallback',
        'serialNumber': '547',
        'isInvoiceTitle': 1,
        'sendType': 1,
        'channel': 22,
        'vipOrder': 0,
        'supplementFlag': 0,
        'isInvoice': True,
        'invoiceType': 0,
        'invoiceTitle': '发票抬头哈哈哈哈',
        'taxNo': '税号37854058349085'
    }
    res = requests.post(url=url, json=json)
    return res
if __name__ == "__main__":
    res_zt_order = zt_order()
    print(res_zt_order.text)



