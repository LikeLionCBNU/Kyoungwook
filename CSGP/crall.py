import requests
import json
import os
from bs4 import BeautifulSoup
import pandas as pd
import xmltodict
import urllib.request
from tqdm import tqdm
import csv

code_list = []

def stock(stock_code):
    krx_api_requests = requests.get('http://asp1.krx.co.kr/servlet/krx.asp.XMLSise?code={}'.format(stock_code)).content.strip()
    print("진행중")
    try :
        krx_api_to_str =  json.dumps(xmltodict.parse(krx_api_requests))
        krx_api_to_str = krx_api_to_str.replace('@','')
        krx_api = json.loads(krx_api_to_str)
        perfect = krx_api['stockprice']['TBL_StockInfo']
        print(perfect)

        if perfect['JongName'] != '':
            if not os.path.exists('stock.csv'):
                with open('stock.csv','w') as f:
                    w = csv.writer(f)
                    w.writerow(perfect.keys())
                    w.writerow(perfect.values())
            else:
                with open('stock.csv','a') as f:
                    w = csv.writer(f)
                    w.writerow(perfect.values())
        ##db = pd.DataFrame(krx_api, index=['stockprice']['TBL_StockInfo'])
        

        ##if not os.path.exists('excel_test.csv'):
        ##    writer = csv.DictWriter('excel_test.csv')
        ##    writer.writeheader()
        ##    for data in perfect:
        ##        writer.writerow(data)
        ##    db.to_csv('excel_test.csv', mode = 'w', encoding = 'utf-8-sig')
        ##else:
        ##    writer = csv.DictWriter('excel_test.csv')
        ##    writer.writeheader()
        ##    for data in perfect:
        ##        writer.writerow(data)
        ##    db.to_csv('excel_test.csv', mode = 'a', index=False, encoding = 'utf-8-sig')
        print("성공")
        
    except Exception as e:
        api = "error"

code_data = pd.read_excel('stock_data.xls', dtype={'종목코드': str})
code_data = code_data[['종목코드']]
code_data = code_data.values.tolist()

code_list = sum(code_data, [])

stock_code = ['066570', '208350']

for code in code_list:
    stock(code)