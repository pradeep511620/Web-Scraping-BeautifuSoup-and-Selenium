import tabula
import pandas as pd
from typing import TextIO
from tabula.io import read_pdf
file="roller-chain-sprockets.pdf"
tables=tabula.read_pdf(file,pages="98",multiple_tables=True)
for df in tables:
    df = df.columns.to_frame().T.append(df, ignore_index=True)
    df.columns = range(len(df.columns))
    df = df.iloc[1:]
    headers = df.iloc[0]
    df = pd.DataFrame(df.values[1:], columns=headers)
    print(df)
    df=df.Catalog
    df['Page'] = 98
    print(df)
    print(df.columns)

    with open(r'martin98a.txt', 'a') as f: # f:\data\pandas.txt
        dfAsString = df.to_string(header=False, index=False)
        f.write(dfAsString)


#tabula.convert_into(file,"lga.csv",pages="13")