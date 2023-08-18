import os as os
import pandas as pd

# reader excel file from os directory
path = os.getcwd()

# search file with extension .xlsx or .csv
files_founded = [f for f in os.listdir(path) if f.endswith('.xlsx')
                 or f.endswith('.xls') or f.endswith('.csv')
                 or (f.endswith('.gsheet'))]

if files_founded:
    for file in files_founded:
        # read excel file, remove NaN columns
        excel_data = pd.read_excel(
            file, sheet_name='Sheet1').dropna(axis=1, how='all').dropna(axis=0, how='all').dropna(
            axis=0, subset=['Item', 'Valor']).reset_index(drop=True).sort_values(
            by=['Valor'], ascending=False).reset_index(drop=True)
else:
    print('File not found')
