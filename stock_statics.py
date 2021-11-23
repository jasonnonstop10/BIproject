
import pandas as pd
import json


def get_statics():
    df = pd.read_excel('SianStockDCF.xlsx', sheet_name='E(R)')
    df = df[0:6]
    df1 = df[['Ticker', 'Fair Value', "Market Price"]]
    result = df1.to_json(orient="split")
    parsed = json.loads(result)
    return parsed.get('data')


def get_staticsfindone(name):
    df = pd.read_excel('SianStockDCF.xlsx', sheet_name='E(R)')
    df = df[0:6]
    df1 = df[['Ticker', 'Fair Value', "Market Price"]]
    result = df1.to_json(orient="split")
    parsed = json.loads(result)
    for i in parsed.get('data'):
        if i[0] == name:
            return i
    return None
