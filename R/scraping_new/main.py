import csv
import pandas as pd
from typing import TextIO

with open('norton2.csv', newline='',encoding='UTF-8') as f:
    reader = csv.reader(f)
    your_list = list(reader)

print(your_list)
df = pd.DataFrame(your_list)
print(df)
print(len(df.columns))
print(len(df))
for x in range(1, len(df)):
         for y in range(1, len(df.columns)):
             save_details: TextIO = open("norton3.txt", "a+", encoding="utf-8")
             save_details.write("\n" + df[0][x] + "\t" + df[y][0] + "\t" + df[y][x])
             save_details.close()
             print("\n**Record stored into txt file.**")