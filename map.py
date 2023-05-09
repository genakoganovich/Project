import numpy as np
import pandas as pd
from os.path import join
from util import create_file_list

IN_PATH = '../input/008_map_in'
OUT_PATH = '../output/008_map_out'


def create_map(input_name, output_name):
    df = pd.read_csv(input_name, sep='\t', header=0, dtype=str)
    row, col = df.shape
    for i in range(0, row, 2):
        print('{0}_{1}{2}-{3}_step{4}'.format(df.iloc[i, 0], df.iloc[i, 1], df.iloc[i, 2], df.iloc[i, 3], df.iloc[i, 4]))
        print()
    # df.to_csv(output_name, sep='\t', index=False)


def run():
    for name in create_file_list(IN_PATH):
        create_map(join(IN_PATH, name), join(OUT_PATH, name))


if __name__ == '__main__':
    run()
