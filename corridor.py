import numpy as np
import pandas as pd
from os import listdir
from os.path import isfile, join

IN_PATH = '../input/001_cmp_picking'
OUT_PATH = '../output/001_zomf_corr'


def create_file_list(path):
    return [f for f in listdir(path) if isfile(join(path, f))]


def to_zomf_corridor(input_name, output_name, save_header, max_angle, corridor_width, min_velocity):
    df = pd.read_csv(input_name, sep='\t', skiprows=13, usecols=np.arange(7), dtype=np.float64, names=save_header.split())
    df.iloc[:, 6] = max_angle
    df.iloc[:, 5] = corridor_width
    df.iloc[:, 4] = df.iloc[:, 3]
    df.iloc[:, 2] = df.iloc[:, 2]\
        .apply(lambda x: min_velocity + corridor_width / 2 if x < min_velocity + corridor_width / 2 else x)
    df.iloc[:, 3] = 0
    df.to_csv(output_name, sep='\t', index=False)


def run():
    save_header = 'XCoord	YCoord	V	A	T	DeltaV	DeltaA'
    max_angle = 1.55334
    corridor_width = 500
    min_velocity = 1500
    for name in create_file_list(IN_PATH):
        to_zomf_corridor(join(IN_PATH, name), join(OUT_PATH, name), save_header, max_angle, corridor_width, min_velocity)


if __name__ == '__main__':
    run()
