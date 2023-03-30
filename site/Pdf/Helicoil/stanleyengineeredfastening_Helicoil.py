import tabula
import pandas as pd
from typing import TextIO
from tabula.io import read_pdf
file="HC 2000_rev11_web.pdf"
tables=tabula.read_pdf(file,pages="25",multiple_tables=True)
loc = 0
for df in tables:
    # df = df.replace(['-'], '_')
    if loc==0:
        df = df.astype(str)
        print(df)
        df.to_csv("heading25.csv")
        loc=loc+1
        continue
    elif loc == 1:
        loc=loc+1
        df = df.astype(str)
        print(df)
        df.to_csv("1table25.csv")
    elif loc == 2:
        df = df.astype(str)
        print(df)
        df.to_csv("2table25.csv")
    else:
        print("No tables found")





#tabula.convert_into(file,"lga.csv",pages="13")