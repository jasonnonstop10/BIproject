import json


def get_detail(stock):
    with open('stockdetail.json', 'r', encoding="utf-8") as f:
        detail = json.load(f)
        data = detail['data']
        for i in data:
            if i["symbol"] == stock:
                return i
    return None


def get_detailALL():
    with open('stockdetail.json', 'r', encoding="utf-8") as f:
        detail = json.load(f)
        return detail
