import pandas as pd
import matplotlib
import os
from tqdm import tqdm
import time

print('Loading coconut...')

col = [
    "UserID",
    "Date",
    "Ban Time",
    "Reason"
]

file = "coconut.txt"

try:
    df = pd.read_csv(file)
    df["Date"] = pd.to_datetime(df["Date"])
    print("Successed!")
except:
    print("Try fail!")
    import pandas as pd
    df = pd.read_excel(file)
    df.columns = col
    df["Date"] = pd.to_datetime(df["Date"])
    print("Excepted!")

print('Finding id...')

with open('find_id(s).txt', 'r') as r:
    line = r.readlines()
    r.close()

find_id = [i.replace('\n', '') for i in line]

cond = df["UserID"].isin(find_id)
a = df[cond]
a.to_csv('result.txt', encoding='utf-8-sig', index=False)
print(a)
# baned_id = a["UserID"].unique()
# df[df["UserID"].isin(baned_id)].to_csv('result.txt', encoding='utf-8-sig', index=False)
# df[df["UserID"].isin(baned_id)].groupby("UserID").count()
print('\nResult in \"result.txt\"')
input('Press enter to exit')