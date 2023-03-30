import tabula
import pandas as pd
from typing import TextIO
file="roller-chain-sprockets.pdf"
tables=tabula.read_pdf(file,pages="67",multiple_tables=True)
u=1
for df in tables:
 print(df)


#tabula.convert_into(file,"lga.csv",pages="13")