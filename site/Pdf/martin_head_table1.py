import tabula
import pandas as pd
from typing import TextIO
from tabula.io import read_pdf
file="roller-chain-sprockets.pdf"
tables=tabula.read_pdf(file,pages="12",multiple_tables=True) # PageNumber
for df in tables:
    df = df.columns.to_frame().T.append(df, ignore_index=True)
    df.columns = range(len(df.columns))
    df = df.iloc[2:]
    headers = df.iloc[0]
    df = pd.DataFrame(df.values[1:], columns=headers)
    df=df.Catalog
    df['Page'] = 12  # PageNumber
    # print(df)
    df1 = df.copy()
    df1.columns = [df1.columns, df1.columns.to_series().groupby(level=0).cumcount()]
    df1=df1.stack().reset_index(drop=True)
    with open(r'martin-head-table1.txt', 'a') as f: # f:\data\pandas.txt
        dfAsString = df1.to_string(header=False, index=False)
        f.write(dfAsString)



#tabula.convert_into(file,"lga.csv",pages="13")