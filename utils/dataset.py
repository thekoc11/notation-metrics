import pandas as pd
import numpy as np
import os
import glob
import data
from io import open
from utils import dataStructures
ragaId2Raga = {'22': 'Kharaharpriya', '22_a': 'Abhogi',
               '29': 'Shankarabharanam', '29_h': 'Hamsadhwani',
               '15': 'Mayamalavagowla', '15_m': 'Malahari',
               '8': 'Hanumatodi', '8_d': 'Dhanyaasi',
               '20': 'Natabhairavi', '20_s': 'Saramathi',
               '28': 'Harikambodhi', '28_k': 'Kambodhi',
               '65': 'Kalyani'}

def findFiles(path): return glob.glob(path)

BASE_PATH = "/home/efm-workstation/notations"


class Dictionary(object):
    def __init__(self):
        self.word2idx = {}
        self.idx2word = []

    def add_word(self, word):
        if word not in self.word2idx:
            self.idx2word.append(word)
            self.word2idx[word] = len(self.idx2word) - 1
        return self.word2idx[word]

    def __len__(self):
        return len(self.idx2word)


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
        df_filtered = df
        song_coords = []
        song_meas = []
        song_dur = []
        song_note = []
        for i in range(len(df_filtered)):
            song_meas.append(df_filtered.iloc[i, 0])
            song_dur.append(df_filtered.iloc[i, 2])
            song_note.append(df_filtered.iloc[i, 1])
        song_coords = [song_meas, song_note, song_dur]
        coord_lists[name] = song_coords

    return coord_lists
def GetRagaSongCoordsDict(ragaId, basePath=BASE_PATH):
    """

    :param ragaId: The ID of the raga is the katapayadi sankhya of the melakarta or
                   <katapayadi sankhya of the parent melakarta>_<initial alphabet of the janya>
    :param basePath (optional): path where the compositions are stored. Leave default for now.
    :return: The 3d data of every song
    """
    raga_path = os.path.join(basePath, str(ragaId))
    coord_lists = []
    for filename in findFiles('{}/*-parsed.txt'.format(raga_path)):
        name = _getSongName(filename, ragaId)
        df = pd.read_csv(filename)
        df_filtered = df
        song_coords = []
        song_meas = []
        song_dur = []
        song_note = []
        for i in range(len(df_filtered)):
            song_meas.append(df_filtered.iloc[i, 0])
            song_dur.append(df_filtered.iloc[i, 2])
            song_note.append(df_filtered.iloc[i, 1])
        song_coords = {"Measure": song_meas, " Note": song_note, " Duration": song_dur}
        coord_lists.append(song_coords)

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
        df_filtered = df
        song_time = []
        song_notes = []
        song_coords = []
        cum_dur = 0
        for i in range(len(df_filtered)):
            if i > 0 and df_filtered.iloc[i, 0] != df_filtered.iloc[i-1, 0]:
                cum_dur = 0
            elif i == 0:
                cum_dur = df_filtered.iloc[i, 2]
            else:
                cum_dur += df_filtered.iloc[i, 2]

            song_time.append(df_filtered.iloc[i, 0] + cum_dur)
            song_notes.append(df_filtered.iloc[i, 1])

        song_coords = [song_time, song_notes]
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
        return retDict

def GetAdjustedMelodies(d, normalise_length=True, pre_min_len=None):
    """

    :param d: Expected to be a dictionary, the output of @GetRagaSongCoords or @GetRagaSongCoordsConcat
    :return: dictionary, whose keys are the same as the input (:param d), and values are the calculated
             adjusted melodies respectively
    """
    ret_dict = {}
    for key, val in d.items():
        adj_mel = data.GetAdjustedMelody(val)
        # print("{}: {}".format(key, len(adj_mel)))
        ret_dict[key] = adj_mel
    #
    # for key in ret_dict.keys():
    #     print("{}:  length: {}".format(key, len(ret_dict[key])))

    if normalise_length:
        list_lens = [len(i) for i in list(ret_dict.values())]
        min_len = np.min(list_lens) if pre_min_len is None else pre_min_len
        indices = [np.random.randint(0, i - min_len + 1, 1)[0] for i in list_lens]
        for i, (key, val) in enumerate(ret_dict.items()):
            ret_dict[key] = ret_dict[key][indices[i]:indices[i] + min_len]
            # print("{}: Start: {}, end: {}, length: {}".format(key, indices[i], indices[i] + min_len, len(ret_dict[key])))

    # for key in ret_dict.keys():
    #     print("{}:  length: {}".format(key, len(ret_dict[key])))
    return ret_dict

def GetRagaSongCoordsConcat(*args):
    """

    :param args: String arguments, which are expected to be valid ragaIds
    :return: a contiguous dictionary containing the euclidean data of all the compositions in the ragas specified in
             :param args. The keys are the names of the compositions, while the values are the 3d data-lists.
    """
    dict_list = []
    num_comps = 9999999
    for ragaId in args:
        dict_r = GetRagaSongCoords(ragaId)
        n_c = len(list(dict_r.keys()))
        if n_c < num_comps:
            num_comps = n_c
        dict_list.append(dict_r)
    # final_list = []
    # for dict_r in dict_list:
    #     # dict_r = GetRagaSongCoords(ragaId)
    #     n_c = len(list(dict_r.keys()))
    #     new_dict = {}
    #     selected_inds = np.random.choice(n_c, size=num_comps, replace=False)
    #     for ind in selected_inds:
    #         key = list(dict_r.keys())[ind]
    #         new_dict[key] = dict_r[key]
    #     final_list.append(new_dict)
    final_dict = ConcatenateDicts(*dict_list)
    return final_dict

def GetRagaSongCoords2dConcat(*args):
    dict_list = []
    num_comps = 9999999
    for ragaid in args:
        dict_r = GetRagaSongCoords2d(ragaid)
        n_c = len(list(dict_r.keys()))
        if n_c < num_comps:
            num_comps = n_c
        new_dict = {}
        selected_inds = np.random.choice(n_c, size=num_comps, replace=False)
        for ind in selected_inds:
            key = list(dict_r.keys())[ind]
            new_dict[key] = dict_r[key]
        dict_list.append(new_dict)
    return ConcatenateDicts(*dict_list)

def GetAdjMelDictsConcat(*args, **kwargs):
    """

    :param args: String arguments, which are expected to be valid ragaIds
    :return: a contiguous dictionary containing the adjusted melodies of all the compositions in the ragas specified in
             :param args. The keys are the names of the compositions, while the values are the adjusted melodies.
    """
    ragaCount = len(args)
    final_dict = GetRagaSongCoordsConcat(*args)
    for key in final_dict:
        final_dict[key] = dataStructures.PackTuples(*final_dict[key])
    unif = True
    if 'unif' in kwargs.keys():
        unif = kwargs['unif']
    min_len = None
    if 'min_len' in kwargs.keys():
        min_len = kwargs['min_len']

    dictAdjMel = GetAdjustedMelodies(final_dict, normalise_length=unif, pre_min_len=min_len)

    if unif:
        list_lens = [len(i) for i in list(dictAdjMel.values())]
        min_len = np.min(list_lens)
        indices = [np.random.randint(0, i - min_len + 1, 1)[0] for i in list_lens]
        for i, (key, val) in enumerate(dictAdjMel.items()):
            dictAdjMel[key] = dictAdjMel[key][indices[i]:indices[i]+min_len]
            # print("{}: Start: {}, end: {}, length: {}".format(key, indices[i], indices[i] + min_len, len(dictAdjMel[key])))
    print(f"Final Value Chosen: {len(list(dictAdjMel.values())[0])}")
    return dictAdjMel

def StandardisingRepeater(song_coords, stan_size=1500):
    curr_size = len(song_coords)
    if stan_size < curr_size:
        return song_coords[0:stan_size]
    elif curr_size < stan_size:
        rep_coords = song_coords[curr_size-stan_size : curr_size]
        return song_coords + rep_coords
    else:
        return song_coords



# def CreateSurrogateDataset(ragaId='22', basePath=BASE_PATH):
#     raga_path = os.path.join(basePath, str(ragaId))
#     orig_files = [ i for i in findFiles('{}/*'.format(raga_path)) if i not in findFiles('{}/*-parsed.txt'.format(raga_path))]
#     vowels = ['A', 'a', 'e', 'E', 'I', 'i', 'O', 'o', 'U', 'u', '(', ')']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#     start_reading = False
#     all_words = Dictionary()
#     for filename in orig_files:
#         with open(filename, 'r', encoding='utf8') as f:
#             print('File {} opened:'.format(filename))
#             for line in f:
#                 if  '<END>' in line.split():
#                     start_reading = False
#                     pass
#                 elif '<BEGIN>' in line.split():
#                     start_reading = True
#
#                 if start_reading and '<BEGIN>' not in line.split():
#                     words = line.split()
#                     for word in words:
#                         add_words = False
#                         for letter in word:
#                             if letter in vowels or letter in nums:
#                                 add_words = False
#                                 break
#                             else: add_words = True
#                         if add_words:
#                             all_words.add_word(word)
#
#     return all_words


if __name__ == '__main__':
    from models import simpleVAE as sv
    #
    # dicts3d = GetRagaSongCoordsConcat('15', '15_m')
    # for key in dicts3d:
    #     print(key)
    # for key in dicts3d:
    #     dicts3d[key] = dataStructures.PackTuples(*dicts3d[key])
    coords = GetAdjMelDictsConcat('15', '15_m')
    # d = GetAdjustedMelodies(dicts3d)

    # print(adjMelDicts.keys())
    # coords = GetRagaSongCoords('22')
    # print(coords[np.random.choice(list(coords.keys()))])
    # print(coords)
    # dataset = []
    # for keys, values in coords.items():
    #     print(keys, len(values))
    #     notes = []
    #     for e in values:
    #         notes.append(e[1])
    #     notes = np.array(notes)
    #     notes = np.unique(notes)
    #     print(notes)
    #     dataset.append(values)
    # new = sv.UseVAE(dataset, 63830)
    # print(len(new))
    # vocab_22 = CreateSurrogateDataset('8_d')
    # print(vocab_22.idx2word)
    # print(len(vocab_22))