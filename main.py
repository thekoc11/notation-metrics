import os
import time

import numpy as np
from utils import dataStructures, dataset, plotter, parallelizer
from utils.gpu import matmul
import matplotlib.pyplot as plt
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

if __name__ == '__main__':
    # dat = dataset.GetRagaSongCoordsConcat('15')
    # iters = 0
    # final_list = None
    # for k, v in dat.items():
    #     l = dataStructures.EventList(v)
    #     uni = dataStructures.NGramHolder(l.classes[1], 1)
    #     iters += 1
    #     # print(np.array(uni.keys).astype('int64'))
    #     if final_list is None:
    #         final_list = l
    #     else:
    #         final_list = final_list.Add(l)
    #
    # uni = dataStructures.NGramHolder(final_list.classes[1], 1)
    # # print(np.array(uni.keys).astype('int64'))
    # uni.CalculateFreq(final_list.mainArray[1])
    # print(uni.GetProbMatrix())
    # print(dat)
    dat1 = dataset.GetRagaSongCoords('28_k')
    # prob = []

    # t1 = time.perf_counter()
    d_surr1 = markovian.GenerateForRaga('28', 100, serial=True)
    # t2 = time.perf_counter()
    # t3 = time.perf_counter()
    # d_surr2 = markovian.GenerateForRaga('28', 100)
    # t4 = time.perf_counter()

    # print("Serial took {} seconds".format(t2 - t1))
    # print("Parallel took {} seconds".format(t4 - t3))
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
    # fig = plt.figure(figsize=(10, 10))
    # ax = fig.add_subplot(1, 1, 1)
    # v_new = plotter._handleRests(v[1])
    # Normal = np.ceil(np.random.normal(10, 4, 10000))
    # l_norm = dataStructures.EventList(Normal)

    # ax.plot(l.classFreq[1])
    # ax.plot(l_norm.classFreq)
    # print(l.classes[1])
    # print(l.classFreq[1])
    # # print(np.array(v_new).mean())
    # plt.show()
    # print(prob)
    # uni_fil = dataStructures.NGramHolder(np.arange(7), 1)
    # arr = np.vectorize(OneOctave)(final_list.mainArray[1], 7)
    # arr = arr[~(np.isnan(arr))]
    # uni_fil.CalculateFreq(arr)
    # print(uni.table)
    # print(uni.table.sum(), uni.totalPossibleTransitions)
    # prob = np.array([e / e.sum() for e in uni.table])
    # nIters = 30
    # # print(prob)
    # new_prob = prob
    # new_prob_last = prob
    # for i in range(nIters):
    #     new_prob = np.matmul(prob, new_prob)
    #     if i == nIters - 2:
    #         new_prob_last = new_prob
    #     # print(new_prob)
    # # print(new_prob - new_prob_last)
    # # print("New Probability")
    # # print(new_prob)
    # pi = new_prob[-1]
    # # print(np.matmul(pi, prob))
    # print(pi)
    # print(final_list.classFreq[1] / final_list.classFreqSum[1])
