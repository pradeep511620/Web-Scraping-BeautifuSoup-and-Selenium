import tabula
import pandas as pd
from typing import TextIO
from tabula.io import read_pdf

file = "roller-chain-sprockets.pdf"
tables = tabula.read_pdf(file, pages="100", multiple_tables=True)
var=1
for df in tables:
    if var==1:
        var=var+1
        continue
    df = df.columns.to_frame().T.append(df, ignore_index=True)
    df.columns = range(len(df.columns))

    headers = df.iloc[0]
    df = pd.DataFrame(df.values[2:], columns=headers)
    print(df)
    df=df.Number
    df['Page'] = 98
    print(df)

    with open(r'martin100.txt', 'a') as f:  # f:\data\pandas.txt
        dfAsString = df.to_string(header=False, index=False)
        f.write(dfAsString)

# tabula.convert_into(file,"lga.csv",pages="13")