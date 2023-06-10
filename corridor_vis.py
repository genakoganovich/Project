import numpy as np
import pandas as pd
from os.path import join
from util import create_file_list
import matplotlib as mpl
import matplotlib.pyplot as plt


IN_PATH = '../input/001_cmp_picking'
OUT_PATH = '../output/001_zomf_corr'


def set_fig_ax(picking, fig, ax):
    ax.invert_yaxis()
    ax.set_title(f'Velocity picking\n (x, y) = ({picking[0][0]}, {picking[0][1]})')
    ax.set_xlabel('Velocity')
    ax.set_ylabel('Time')
    fig.set_figwidth(5.5)
    fig.set_figheight(8)
    return fig, ax


def plot_corridor(input_name):
    df = pd.read_csv(input_name, sep='\t', skiprows=13, usecols=np.arange(4),
                     dtype=np.float64, header=0, names=['x', 'y', 'v', 't'])

    for group in df.groupby(by=['x', 'y']):
        fig, ax = set_fig_ax(group, *plt.subplots())
        ax.plot(group[1][['v']], group[1][['t']], marker='o')
        plt.show()


def run():
    for name in create_file_list(IN_PATH):
        plot_corridor(join(IN_PATH, name))


if __name__ == '__main__':
    run()
