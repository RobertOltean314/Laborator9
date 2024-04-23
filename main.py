import pandas as pd
import openpyxl

fisier = 'CititDinFisier.xlsx'


def read_context(file):
    data = pd.read_excel(file, header=None)

    df = pd.DataFrame(data)

    for i, row in df.iterrows():
        print(f" {row.iloc[0]} {row.iloc[1]}")


read_context(fisier)
