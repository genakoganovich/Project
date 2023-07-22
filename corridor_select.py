import numpy as np
import pandas as pd
from os.path import join
from util import create_file_list

IN_PATH = '../input/012_select_in'
OUT_PATH = '../output/012_select_out'


def select_by_y_coord(input_name, output_name, save_header):
    df = pd.read_csv(input_name, sep='\t', skiprows=1, usecols=np.arange(7), dtype=np.float64,
                     names=save_header.split())

    def update_angle(angle):
        return np.deg2rad(20) if angle > np.deg2rad(20) else angle

    df.iloc[:, 6] = df.iloc[:, 6].apply(update_angle)
    df[df['YCoord'] > 6727700].to_csv(output_name, sep='\t', index=False)


def run():
    save_header = 'XCoord	YCoord	V	A	T	DeltaV	DeltaA'
    for name in create_file_list(IN_PATH):
        select_by_y_coord(join(IN_PATH, name), join(OUT_PATH, name), save_header)


if __name__ == '__main__':
    run()
