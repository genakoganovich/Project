import numpy as np
import pandas as pd
from os.path import join
from util import create_file_list

IN_PATH = '../input/017_scv_sec_to_ms_in'
OUT_PATH = '../output/017_scv_sec_to_ms_out'


def csv_sec_to_ms(input_name, output_name, save_header):
    df = pd.read_csv(input_name, sep=';', skiprows=1, usecols=np.arange(5), dtype=np.float64, names=save_header.split())

    def update_shift(shift):
        return shift * 1000

    df.iloc[:, 4] = df.iloc[:, 4].apply(update_shift)
    df.to_csv(output_name, sep='\t', index=False, float_format='%.0f')



def run():
    save_header = 'X	Y	Inline	Xline	Shift'
    for name in create_file_list(IN_PATH):
        csv_sec_to_ms(join(IN_PATH, name), join(OUT_PATH, name), save_header)
        update_line_terminator(join(OUT_PATH, name))



def update_line_terminator(output_file):
    # Заменяем символ конца строки
    with open(output_file, 'r') as f:
        content = f.read()

    # Перезаписываем файл с новыми концами строк
    with open(output_file, 'w', newline='') as f:
        f.write(content.replace('\r\n', '\n'))

if __name__ == '__main__':
    run()
