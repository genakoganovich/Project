import numpy as np
import pandas as pd
import util
from os.path import join
from util import create_file_list

IN_PATH = '../input/001_cmp_picking'
OUT_PATH = '../output/001_zomf_corr'


def to_zomf_corridor(input_name, output_name, save_header, max_angle, corr_w, min_w, max_w, min_vel):
    skip_rows_value = util.find_end_header_line(input_name) + 1
    df = pd.read_csv(input_name, sep='\t', skiprows=skip_rows_value, usecols=np.arange(7), dtype=np.float64,
                     names=save_header.split())
    max_t = df.iloc[:, 3].max()

    df.iloc[:, 6] = max_angle
    df.iloc[:, 5] = df.iloc[:, 3].astype(object).apply(lambda t: round(min_w + (t / max_t) * (max_w - min_w), 1))
    df.iloc[:, 4] = df.iloc[:, 3]
    df.iloc[:, 2] = df.apply(lambda row: round(row.iloc[2] + row.iloc[5] / 2, 2), axis=1)
    df.iloc[:, 2] = df.iloc[:, 2].apply(lambda vel: min_vel + corr_w if vel < min_vel + corr_w else vel)
    df.iloc[:, 3] = 0
    df.to_csv(output_name, sep='\t', index=False)


def run():
    save_header = 'XCoord	YCoord	V	A	T	DeltaV	DeltaA'
    max_angle = 1.55334
    corr_w, min_w, max_w = 500, 400, 1500
    min_vel = 1500
    for name in create_file_list(IN_PATH):
        to_zomf_corridor(join(IN_PATH, name), join(OUT_PATH, name), save_header, max_angle,
                         corr_w, min_w, max_w, min_vel)


if __name__ == '__main__':
    run()