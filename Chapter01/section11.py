# Section11
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv

# 예제1
import csv
from gettext import install
from tkinter import INSIDE

with open("./Chapter01/resource/sample1.csv", "r") as f:
    reader = csv.reader(f)
    # next(reader)    # Header 스킵

    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))

    for c in reader:
        print(c)

# 예제2
with open("./Chapter01/resource/sample2.csv", "r") as f:
    reader = csv.reader(f, delimiter="|")
    # next(reader)    # Header 스킵

    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))

    for c in reader:
        print(c)

# 예제3 (Dict 변환)
with open("./Chapter01/resource/sample1.csv", "r") as f:
    reader = csv.DictReader(f)

    for c in reader:
        for k, v in c.items():
            print(k, v)
        print("--------------")

# 예제4
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]

with open("./Chapter01/resource/sample3.csv", "w", newline="") as f:
    wt = csv.writer(f)

    for v in w:
        wt.writerow(v)

# 예제5
with open("./Chapter01/resource/sample4.csv", "w", newline="") as f:
    wt = csv.writer(f)
    wt.writerows(w)

# XSL, XLSX
# openpyxl, xlsxsriter, xlrd, xlwt, xlutils
# panas 를 주로 사용(posenpyxl, xlrd)
# pip install xlrd
# pip install openpyxl
# pip install pandas
import pandas as pd

# sheetname='시트명' 또는 숫자, header=3, skiprow=숫자
xlsx = pd.read_excel("./Chapter01/resource/sample.xlsx")

# 상위 데이터 확인
print(xlsx.head())
print()

print(xlsx.tail())

# 데이터 확인
print(xlsx.shape)  # 행, 열

# 엑셀 or CSV 다시 쓰기
xlsx.to_excel("./Chapter01/resource/result.xlsx", index=False)
xlsx.to_csv("./Chapter01/resource/result.csv", index=False)
