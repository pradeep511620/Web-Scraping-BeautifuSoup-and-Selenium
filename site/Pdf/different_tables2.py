import tabula
import pandas as pd
from typing import TextIO
from tabula.io import read_pdf
file="roller-chain-sprockets.pdf"
tables=tabula.read_pdf(file,pages="67",multiple_tables=True)
loc = 0
for df in tables:
    loc +=1
    if loc == 6:  # Table1 = 6, 11  Index([nan, nan, nan, nan, 'Stock', 'Rec.\rMax.', 'Dia.', 'Length\rThru', nan], dtype='object', name=1)
        df = df.columns.to_frame().T.append(df, ignore_index=True)
        df.columns = range(len(df.columns))
        df = df.iloc[0:]
        headers = df.iloc[0]
        df = pd.DataFrame(df.values[1:], columns=headers)
        # print(df)
        print(df.columns)
        df=df['Catalog\rNumber'] #CatalogNumber     Catalog         Number
        df['Page'] = 67
        # print(df)


        with open(r'martin67-12.txt', 'a') as f: # f:\data\pandas.txt
            dfAsString = df.to_string(header=False, index=False)
            f.write(dfAsString)


#tabula.convert_into(file,"lga.csv",pages="13")