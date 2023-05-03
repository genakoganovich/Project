import numpy as np
import pandas as pd
from os.path import join
from util import create_file_list

IN_PATH = '../input/007_hor_in'
OUT_PATH = '../output/007_hor_out'


def remove_column(input_name, output_name):
    df = pd.read_csv(input_name, sep=',', usecols=np.arange(2, 5), dtype=np.float64)
    df.to_csv(output_name, sep='\t', index=False)


def run():
    for name in create_file_list(IN_PATH):
        remove_column(join(IN_PATH, name), join(OUT_PATH, name))


if __name__ == '__main__':
    run()
