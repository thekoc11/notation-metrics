import pandas as pd
import numpy as np
import os
import glob
import data

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
    """

    :param ragaId: The ID of the raga is the katapayadi sankhya of the melakarta or
                   <katapayadi sankhya of the parent melakarta>_<initial alphabet of the janya>
    :param basePath (optional): path where the compositions are stored. Leave default for now.
    :return: The 3d data of every song
    """
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



def GetRagaSongCoords2d(ragaId, basePath=BASE_PATH):
    """

    :param ragaId: The ID of the raga is the katapayadi sankhya of the melakarta or
                   <katapayadi sankhya of the parent melakarta>_<initial alphabet of the janya>
    :param basePath (optional): path where the compositions are stored. Leave default for now.
    :return: The 2d data of every song
    """
    raga_path = os.path.join(basePath, str(ragaId))
    coord_lists = {}
    for filename in findFiles('{}/*-parsed.txt'.format(raga_path)):
        name = _getSongName(filename, ragaId)
        df = pd.read_csv(filename)
        df_filtered = df[df[" Note"] < 99999]
        song_coords = []
        cum_dur = 0
        for i in range(len(df_filtered)):
            if i > 0 and df_filtered.iloc[i, 0] != df_filtered.iloc[i-1, 0]:
                cum_dur = 0
            elif i == 0:
                cum_dur = df_filtered.iloc[i, 2]
            else:
                cum_dur += df_filtered.iloc[i, 2]

            song_coords.append((df_filtered.iloc[i, 0] + cum_dur, df_filtered.iloc[i, 1]))

        coord_lists[name] = song_coords

    return coord_lists

def GetRagaFromRagaId(ragaid='22'):
    if str(ragaid) in ragaId2Raga.keys():
        return ragaId2Raga[ragaid]
    else: return None

def ConcatenateDicts(*args):
    if len(args) < 2:
        if len(args) == 1:
            return args[0]
        else: raise ValueError("Please input at least one argument!")

    elif len(args) == 2:
        return dict(args[0], **args[1])
    elif len(args) > 2:
        retDict = dict(args[0], **args[1])
        for i in range(2, len(args)):
            retDict.update(args[i])

def GetAdjustedMelodies(d):
    """

    :param d: Expected to be a dictionary, the output of @GetRagaSongCoords or @GetRagaSongCoordsConcat
    :return: dictionary, whose keys are the same as the input (:param d), and values are the calculated
             adjusted melodies respectively
    """
    ret_dict = {}
    for key, val in d.items():
        adj_mel = data.GetAdjustedMelody(val)
        print("{}: {}".format(key, len(adj_mel)))
        ret_dict[key] = adj_mel
    return ret_dict

def GetRagaSongCoordsConcat(*args):
    """

    :param args: String arguments, which are expected to be valid ragaIds
    :return: a contiguous dictionary containing the euclidean data of all the compositions in the ragas specified in
             :param args. The keys are the names of the compositions, while the values are the 3d data-lists.
    """
    dict_list = []
    for ragaId in args:
        dict_list.append(GetRagaSongCoords(ragaId))
    final_dict = ConcatenateDicts(*dict_list)
    return final_dict

def GetAdjMelDictsConcat(*args):
    """

    :param args: String arguments, which are expected to be valid ragaIds
    :return: a contiguous dictionary containing the adjusted melodies of all the compositions in the ragas specified in
             :param args. The keys are the names of the compositions, while the values are the adjusted melodies.
    """
    ragaCount = len(args)
    final_dict = GetRagaSongCoordsConcat(*args)
    dictAdjMel = GetAdjustedMelodies(final_dict)
    list_lens = [len(i) for i in list(dictAdjMel.values())]
    min_len = np.min(list_lens)
    indices = [np.random.randint(0, i - min_len + 1, 1)[0] for i in list_lens]
    for i, (key, val) in enumerate(dictAdjMel.items()):
        dictAdjMel[key] = dictAdjMel[key][indices[i]:indices[i]+min_len]
        print("{}: Start: {}, end: {}, length: {}".format(key, indices[i], indices[i] + min_len, len(dictAdjMel[key])))
    return dictAdjMel




if __name__ == '__main__':
    # dicts3d = GetRagaSongCoordsConcat('22', '22_a')
    # adjMelDicts = GetAdjMelDictsConcat('22', '22_a')
    # print(adjMelDicts.keys())
    coords = GetRagaSongCoords2d('22')
    print(coords[np.random.choice(list(coords.keys()))])
