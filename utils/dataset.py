import pandas as pd
import numpy as np
import os
import glob

ragaId2Raga = {'22': 'Kharaharpriya', '22_a': 'Aabhogi',
               '29': 'Shankarabharanam', '29_h': 'Hamsadhwani',
               '15': 'Mayamalavagowla', '15_m': 'Malahari',
               '8': 'Hanumatodi', '8_d': 'Dhanyaasi',
               '20': 'Natabhairavi', '20_s': 'Saramathi',
               '28': 'Harikambodhi', '28_k': 'Kambodhi',
               '65': 'Kalyani'}

def findFiles(path): return glob.glob(path)

BASE_PATH = "/home/efm-workstation/notations"

def _getSongName(path, ragaId='22'):
    path_eles = os.path.basename(path)
    path_eles = path_eles.replace('-parsed.txt', '')
    if str(ragaId) in ragaId2Raga.keys():
        return path_eles + '({})'.format(ragaId2Raga[ragaId])
    else:
        raise ValueError("raga Id {} is not known".format(ragaId))

def GetRagaSongCoords(ragaId, basePath=BASE_PATH):
    raga_path = os.path.join(basePath, str(ragaId))
    coord_lists = {}
    for filename in findFiles('{}/*-parsed.txt'.format(raga_path)):
        name = _getSongName(filename, ragaId)
        df = pd.read_csv(filename)
        df_filtered = df[df[" Note"] < 99999]
        song_coords = []
        for i in range(len(df_filtered)):
            song_coords.append((df_filtered.iloc[i, 0], df_filtered.iloc[i, 1], df_filtered.iloc[i, 2]))

        coord_lists[name] = song_coords

    return coord_lists

if __name__ == '__main__':
    lists1 = GetRagaSongCoords('22_a')
    lists2 = GetRagaSongCoords('22')
    lists3 = dict(lists1, **lists2)
    print(lists3.keys())