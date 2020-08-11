import requests as rq
import csv
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CSGP.settings")
import django
django.setup()
from stock.models import *

CSV_PATH = '/Users/hamdongho/WebProject/CSG/CSGP/stock.csv'
with open(CSV_PATH, newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        Category.objects.create(
            Name = row['JongName'],
            Current_Price = row['CurJuka'],
            Debi = row['Debi'],
            DungRak = row['DungRak'],
            Prev_Price = row['PrevJuka'],
            Trade_Volume = row['Volume'],
            Trade_Money = row['Money'],
            Start_Price = row['StartJuka'],
            High_Price = row['HighJuka'],
            Low_Price = row['LowJuka'],
            Week_52_High = row['High52'],
            Week_52_Low = row['Low52'],
            UP_Price = row['UpJuka'],
            Down_Price = row['DownJuka'],
            Per = row['Per'],
            Amount = row['Amount'],
            Face_Price = row['FaceJuka'],
            )