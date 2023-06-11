import numpy as np
import pandas as pd
from os.path import join
from util import create_file_list
import matplotlib as mpl
import matplotlib.pyplot as plt


IN_PATH = '../input/001_cmp_picking'
OUT_PATH = '../output/001_zomf_corr'


def set_fig_ax(fig, ax):
    ax.invert_zaxis()
    ax.set_title(f'Velocity picking')
    ax.set_xlabel('Count')
    ax.set_ylabel('Velocity')
    ax.set_zlabel('Time')
    fig.set_figwidth(10)
    fig.set_figheight(8)


def plot_corridor_3d(input_name):
    df = pd.read_csv(input_name, sep='\t', skiprows=13, usecols=np.arange(4),
                     dtype=np.float64, header=0, names=['x', 'y', 'v', 't'])

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    count = 0
    set_fig_ax(fig, ax)

    for group in df.groupby(by=['x', 'y']):
        x = group[1][['v']].to_numpy()
        x.fill(count)
        ax.plot(x, group[1][['v']], group[1][['t']], marker='o')
        count += 1

    plt.show()


def run():
    for name in create_file_list(IN_PATH):
        plot_corridor_3d(join(IN_PATH, name))


if __name__ == '__main__':
    run()
