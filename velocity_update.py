import numpy as np
import pandas as pd
from os.path import join
from util import create_file_list

IN_PATH = '../input/009_velup_in'
OUT_PATH = '../output/009_velup_out'


def update_velocity_picking(input_name, output_name):
    with open(input_name, 'r') as f_in, open(output_name, 'w') as f_out:
        count = 0
        for line in f_in:
            if count < 10:
                f_out.write(line)
                
            count += 1


def run():
    for name in create_file_list(IN_PATH):
        update_velocity_picking(join(IN_PATH, name), join(OUT_PATH, name))


if __name__ == '__main__':
    run()
