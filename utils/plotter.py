import re, seaborn as sns
import numpy as np

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import ListedColormap
import data

# # generate data
# n = 200
# x = np.random.uniform(1, 20, size=n)
# y = np.random.uniform(1, 100, size=n)
# z = np.random.uniform(1, 100, size=n)
#
# # axes instance
# fig = plt.figure(figsize=(6,6))
# ax = fig.gca(projection='3d')
#
# # get colormap from seaborn
# cmap = ListedColormap(sns.color_palette("husl", 256).as_hex())
#
# # plot
# sc = ax.plot(x, y, z)
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')
#
# # legend
# # plt.legend(*sc.legend_elements(), bbox_to_anchor=(1.05, 1), loc=2)
#
# # save
# plt.savefig("scatter_hue", bbox_inches='tight')

def plot3d(x, y, z, xlabel, ylabel, zlabel, filename='song_3d'):
    # axes instance
    fig = plt.figure(figsize=(6, 6))
    ax = fig.gca(projection='3d')

    # get colormap from seaborn
    cmap = ListedColormap(sns.color_palette("husl", 256).as_hex())

    # plot
    sc = ax.plot(x, y, z)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)

    # legend
    # plt.legend(*sc.legend_elements(), bbox_to_anchor=(1.05, 1), loc=2)

    # save
    plt.savefig(filename, bbox_inches='tight')

def _handleRests(axis_data, default=np.nan):
    for i in range(len(axis_data)):
        if axis_data[i] > 9999:
            axis_data[i] = default
    return axis_data

if __name__ == '__main__':
    dat = data.xtractAxes(data.GetSongCoords2d(data.PAHI_RAMACHANDRA))
    dat1 = data.xtractAxes(data.GetSongCoords2d(data.SYAMALE_MEENAKSHI))
    dat2 = data.xtractAxes(data.GetSongCoords2d(data.MOZART_THEME))
    dat3 = data.xtractAxes(data.GetSongCoords2d(data.AH_VOUS_ORIGINAL))
    dat[1] = _handleRests(dat[1])
    dat1[1] = _handleRests(dat1[1])
    dat2[1] = _handleRests(dat2[1])
    dat3[1] = _handleRests(dat3[1])
    plt.plot(dat[0], dat[1], '-o')
    plt.plot(dat1[0], dat1[1], '-o')
    plt.plot(dat2[0], dat2[1], '-o')
    plt.plot(dat3[0], dat3[1], '-o')
    plt.show()