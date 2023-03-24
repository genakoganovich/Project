import numpy as np
import pandas as pd
from os.path import join
from util import create_file_list

IN_PATH = '../input/002_zomf_corr'
OUT_PATH = '../output/002_zomf_corr_edit'


def edit_zomf_corridor(input_name, output_name, time, delta_velocity):
    def add_velocity(x):
        return round(x + delta_velocity, 2)

    df = pd.read_csv(input_name, sep='\t', header=0)
    df.loc[df['T'] > time, ['V']] = df.loc[df['T'] > time, ['V']].apply(add_velocity)
    df.to_csv(output_name, sep='\t', index=False)


def run():
    time = 1
    delta_velocity = 1000

    for name in create_file_list(IN_PATH):
        edit_zomf_corridor(join(IN_PATH, name), join(OUT_PATH, name), time, delta_velocity)


if __name__ == '__main__':
    run()
