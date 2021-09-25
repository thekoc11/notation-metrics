import os
import time
import numpy as np
from utils import dataStructures, dataset, plotter, parallelizer
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from utils.generators import markovian


def OneOctave(note, tonal):
    """
    Returns an index of a term in the middle octave, depending upon a given value in the twelve or the seven-tonal
    scales
    :param note: The given value in the twelve or the seven tonal scale.
    :param tonal: Specifies the scale of :param note. Valid values: {7, 12}
    :return: return =
    """
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

    #### TODO: need to make the following code more effecient
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
    dat = dataset.GetRagaSongCoordsConcat('29')
    iters = 0
    final_list = get_raga_event_list(dat)

    uni = dataStructures.NGramHolder(final_list.classes[1], 1)
    uni.CalculateFreq(final_list.mainArray[1])

    d_surr1 = markovian.GenerateForRaga('29', num_comps=100, comp_length=1000, serial=True)

    finl_surr = get_raga_event_list(d_surr1)
    uni_surr = dataStructures.NGramHolder(finl_surr.classes[1], 1)
    uni_surr.CalculateFreq(finl_surr.mainArray[1])

    print("original dataset classes: ")
    print(final_list.classes[1])
    print("generated dataset classes: ")
    print(finl_surr.classes[1])

    prob = np.array([e / e.sum() for e in uni.table])
    prob_surr = np.array([e / e.sum() for e in uni_surr.table])
    nIters = 40
    # # print(prob)
    new_prob = prob
    new_prob_surr = prob_surr
    for i in range(nIters):
        new_prob = np.matmul(prob, new_prob)
        new_prob_surr = np.matmul(prob_surr, new_prob_surr)
        if i == nIters - 2:
            new_prob_last = new_prob
    pi =   new_prob[-1] # final_list.classFreq[2] / final_list.classFreqSum[2] #
    pi_surr = new_prob_surr[-1] # finl_surr.classFreq[2] / finl_surr.classFreqSum[2] #
    print(pi)
    print(pi_surr)
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(1, 1, 1)

    ax.plot( pi, '-o', label='raga')
    pi_surr_plot = []
    for i in range(len(final_list.classes[2])):
        if final_list.classes[2][i] not in finl_surr.classes[2]:
            pi_surr_plot.append(np.nan)
        else:
            pi_surr_plot.append(pi_surr[list(finl_surr.classes[2]).index(final_list.classes[2][i])])
    ax.plot( pi_surr, '-o', label='surrogate')

    # ax.plot(final_list.classes[2], pi_surr_plot, '-o', label="raga")
    # ax.plot(final_list.classes[2], pi, '-o', label="surrogate")
    # ax.legend()
    ax.yaxis.set_major_locator(MaxNLocator(3))
    ax.xaxis.set_major_locator(MaxNLocator(3))
    plt.xticks(fontsize=38)
    plt.yticks(fontsize=38)
    plt.show()
