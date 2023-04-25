import numpy as np
import pandas as pd
from os.path import join
from util import create_file_list

IN_PATH = '../input/006_trace_headers_in'
OUT_PATH = '../output/006_trace_headers_out'


def remove_column(input_name, output_name):
    df = pd.read_csv(input_name, sep='\t', skiprows=6, usecols=np.arange(3), dtype=np.float64)
    df.iloc[:, 2] = df.iloc[:, 2].apply(lambda x: x / 1000)
    df.to_csv(output_name, sep='\t', index=False)


def run():
    for name in create_file_list(IN_PATH):
        remove_column(join(IN_PATH, name), join(OUT_PATH, name))


if __name__ == '__main__':
    run()
