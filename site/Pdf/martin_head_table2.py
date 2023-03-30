import tabula
import pandas as pd
from typing import TextIO
from tabula.io import read_pdf
file="roller-chain-sprockets.pdf"
tables=tabula.read_pdf(file,pages="27",multiple_tables=True)
for df in tables:
    df = df.columns.to_frame().T.append(df, ignore_index=True)
    df.columns = range(len(df.columns))
    df = df.iloc[1:]
    headers = df.iloc[0]
    df = pd.DataFrame(df.values[1:], columns=headers)
    df=df.Catalog
    df['Page'] = 27
    print(df)
    df1 = df.copy()
    df1.columns = [df1.columns, df1.columns.to_series().groupby(level=0).cumcount()]
    df1=df1.stack().reset_index(drop=True)
    with open(r'martin-27.txt', 'a') as f: # f:\data\pandas.txt
        dfAsString = df1.to_string(header=False, index=False)
        f.write(dfAsString)


#tabula.convert_into(file,"lga.csv",pages="13")