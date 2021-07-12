import os
import time

import numpy as np
from utils import dataStructures, dataset, plotter, parallelizer
from utils.gpu import matmul
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import ETC
from utils.generators import markovian


def OneOctave(note, tonal):
    if note < 0:
        return note + tonal
    elif note > (tonal - 1) and note < 9999:
        return note - tonal
    elif note > 9999:
        return np.nan
    else:
        return note

def get_raga_event_list(dat):
    iters = 0
    final_list = None
    for k, v in dat.items():
        if isinstance(v[0], tuple):
            v = dataStructures.UnpackTuples(v)
        l = dataStructures.EventList(v)
        iters += 1
        if final_list is None:
            final_list = l
        else:
            final_list = final_list.Add(l)
    return final_list


if __name__ == '__main__':
    dat = dataset.GetRagaSongCoordsConcat('8_d')
    iters = 0
    final_list = get_raga_event_list(dat)

    uni = dataStructures.NGramHolder(final_list.classes[1], 1)
    uni.CalculateFreq(final_list.mainArray[1])
    # dat1 = dataset.GetRagaSongCoords('28_k')

    d_surr1 = markovian.GenerateForRaga('8_d', num_comps=50, comp_length=1000, serial=True)
    finl_surr = get_raga_event_list(d_surr1)
    uni_surr = dataStructures.NGramHolder(finl_surr.classes[1], 1)
    uni_surr.CalculateFreq(finl_surr.mainArray[1])

    print("original dataset classes: ")
    print(final_list.classes[1])
    print("generated dataset classes: ")
    print(finl_surr.classes[1])

    # for key in dat:
    #     dat[key] = dataStructures.PackTuples(*dat[key])

    # for key in dat1:
    #     dat1[key] = dataStructures.PackTuples(*dat1[key])
    #
    # d_fin1 = dataset.ConcatenateDicts(dat, d_surr1)#, dat1, d_surr2)
    # adj = dataset.GetAdjustedMelodies(d_fin1)
    # i1 = np.random.choice(list(adj.keys()))
    # i2 = np.random.choice(list(adj.keys()))
    #
    # print(i1, i2)
    # print(ETC.CCM_causality(adj[i1], adj[i2]))
    # parallelizer.TrueLZPCausality_listParallel(list(adj.values()), list(adj.keys()), mela=dataset.GetRagaFromRagaId('28'))
    # print(prob)
    # uni_fil = dataStructures.NGramHolder(np.arange(7), 1)
    # arr = np.vectorize(OneOctave)(final_list.mainArray[1], 7)
    # arr = arr[~(np.isnan(arr))]
    # uni_fil.CalculateFreq(arr)
    # print(uni.table)
    # print(uni.table.sum(), uni.totalPossibleTransitions)
    prob = np.array([e / e.sum() for e in uni.table])
    prob_surr = np.array([e / e.sum() for e in uni_surr.table])
    nIters = 100
    # # print(prob)
    new_prob = prob
    new_prob_surr = prob_surr
    for i in range(nIters):
        new_prob = np.matmul(prob, new_prob)
        new_prob_surr = np.matmul(prob_surr, new_prob_surr)
        if i == nIters - 2:
            new_prob_last = new_prob
    pi = new_prob[-1] # final_list.classFreq[1] / final_list.classFreqSum[2]
    pi_surr = new_prob_surr[-1] #finl_surr.classFreq[2] / finl_surr.classFreqSum[2]
    print(pi)
    print(pi_surr)
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(1, 1, 1)

    # Y = np.zeros(10000)
    # Y[0] = np.random.randint(20)
    # for i in range(10000):
    #     Y[i] = int(np.random.normal(Y[i - 1], 5))
    # print(np.unique(Y, return_counts=True))
    # ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # ax.hist(Y, bins=20)
    ax.plot(pi, '-o')
    pi_surr_plot = []
    for i in range(len(final_list.classes[1])):
        if final_list.classes[1][i] not in finl_surr.classes[1]:
            pi_surr_plot.append(np.nan)
        else:
            pi_surr_plot.append(pi_surr[list(finl_surr.classes[1]).index(final_list.classes[1][i])])
    ax.plot(pi_surr_plot, '-o')
    # ax.plot(finl_surr.classes[2], pi_surr, '-o')
    ax.legend()
    plt.show()
