import camelot
from typing import TextIO
import pandas as pd
for i in range(18,19):
 tables=camelot.read_pdf("Justrite (1).pdf",pages=str(i))
 for table in tables:

     df=table.df
     print(df)
     df = df.replace('\n', '', regex=True)
     df = df.replace('\t', ' ', regex=True)
     print(len(df.columns))
     print(len(df))
     for x in range(1, len(df)):
         for y in range(1, len(df.columns)):
             save_details: TextIO = open("alemite.txt", "a+", encoding="utf-8")
             save_details.write("\n" + df[0][x] + "\t" + df[y][0] + "\t" + df[y][x])
             save_details.close()
             print("\n**Record stored into txt file.**")


