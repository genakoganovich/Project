import numpy as np
import pandas as pd
from os.path import join

IN_PATH = '../input/004_storage_report'
OUT_PATH = '../output/004_storage_report_out'


def run():
    name = "StorageReport_2023-04-05_21_38.txt"
    df = pd.read_csv(join(IN_PATH, name), sep=':', header=None, skiprows=1)
    df.iloc[:, 0] = df.iloc[:, 0].apply(lambda x: float(x[:-2]))
    df.insert(loc=1, column='Account', value=df.iloc[:, 1].apply(lambda x: x.split('/')[1]))
    df[len(df.columns)] = df.iloc[:, 2].apply(lambda x: x.count('/'))
    df.to_csv(join(OUT_PATH, name), sep='\t', index=False, header=['Size', 'Account', 'Path', 'Level'])


def view():
    name = "StorageReport_2023-04-05_21_38_account_level.txt"
    df = pd.read_csv(join(IN_PATH, name), sep='\t',
                     header=0,
                     dtype={'Size': np.float64, 'Account': str, 'Path': str, 'Level': np.int32})

    # selected_df = df.loc[df['Path'].str.startswith('/geomage_tyumen')]
    selected_df = df[(df['Account'] == 'geomage_tyumen') & (df['Size'] > 5) & (df['Level'] == 2)]
    print(selected_df.to_string())


if __name__ == '__main__':
    view()
