import numpy as np
import pandas as pd
from os.path import join
from util import create_file_list

IN_PATH = '../input/016_corr_in'
OUT_PATH = '../output/016_corr_out'


def limit_angle_zomf_corr(input_name, output_name, save_header):
    df = pd.read_csv(input_name, sep=r'\t+', engine='python', skiprows=1, usecols=np.arange(7), dtype=np.float64, names=save_header.split())

    def update_angle(time):
        if time < 0.8:
            return np.deg2rad(15)
        if time < 0.9:
            return np.deg2rad(750 * time - 585)
        return np.deg2rad(90)

    df.iloc[:, 6] = df.iloc[:, 4].apply(update_angle)

    # index_drop = df[(df.iloc[:, 4] > 0.6) & ((df.iloc[:, 4] * 10) % 10) & (df.iloc[:, 4] != 3.9)].index
    # df.drop(index_drop, inplace=True)
    df.to_csv(output_name, sep='\t', index=False)


def run():
    save_header = 'XCoord	YCoord	V	A	T	DeltaV	DeltaA'
    for name in create_file_list(IN_PATH):
        limit_angle_zomf_corr(join(IN_PATH, name), join(OUT_PATH, name), save_header)


if __name__ == '__main__':
    run()
