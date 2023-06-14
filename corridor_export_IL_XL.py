import numpy as np
import pandas as pd
from os.path import join
from util import create_file_list

IN_PATH = '../input/010_export_IL_XL_in'
OUT_PATH = '../output/010_export_IL_XL_out'


def export_il_xl(input_name, output_name):
    df = pd.read_csv(input_name, sep='\t', skiprows=13, usecols=np.arange(6, 8), dtype=np.int32, header=0,
                     names=['IL', 'XL'])
    df.drop_duplicates(subset=['IL', 'XL'], inplace=True)
    df.to_csv(output_name, sep='\t', index=False)


def run():
    for name in create_file_list(IN_PATH):
        export_il_xl(join(IN_PATH, name), join(OUT_PATH, name))


if __name__ == '__main__':
    run()
