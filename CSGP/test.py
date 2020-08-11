import requests
import json
import os
from bs4 import BeautifulSoup
import pandas as pd
import xmltodict
import urllib.request
from tqdm import tqdm
import csv

f = open('stock.csv', 'r', encoding='utf-8-sig')
rdf = csv.reader(f)
print("불러오기")
for line in rdf:
    print(type(line[3]))
    print(line)
f.close()