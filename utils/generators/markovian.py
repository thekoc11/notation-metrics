from utils import dataStructures, dataset, parallelizer
import numpy as np
from utils.gpu import matmul

def weighted_sampling(weights):
    """
    Weights are expected to be integers
    """


    cum_W = []
    indices = []

    for i in range(len(weights)):
        if weights[i] != 0:
            indices.append(i)
            if len(cum_W) > 0:
                it = weights[i] + cum_W[-1]
                cum_W.append(it)
            else:
                cum_W.append(weights[i])

    num = np.ceil(np.random.uniform(0, 1) * cum_W[-1])
    iter = 0
    while cum_W[iter] < num:
        iter += 1

    return indices[iter]


def randomInversePowerOf2():

    r = np.random.normal(2, 1)
    while r < 0:
        r = np.random.normal(2, 1)

    return 2 ** (-np.floor(r))

def GenerateForRaga(ragaId='22', num_comps=10, serial=False):
    """

    """

    data = dataset.GetRagaSongCoords(ragaId)
    finalList = None
    finalEvList = None
    retVal = {}

    for k, v in data.items():
        l = dataStructures.PackTuples(v[1], v[2])
        l = dataStructures.NoteEventList(l)
        l1 = dataStructures.EventList(v)
        if finalList is None:
            finalList = l
        else:
            finalList = finalList.Add(l)
        if finalEvList is None:
            finalEvList = l1
        else:
            finalEvList = finalEvList.Add(l1)

    # print(finalList.classFreqs)
    # print(finalList.classes)
    # print(len(finalList), len(finalList.classes), len(finalList.classFreqs))

    # unigram = dataStructures.NGramHolder(finalList.classes, 2)
    # unigram.CalculateFreq(finalList.List)
    # Generate(unigram, finalList)
    unigram_notes = dataStructures.NGramHolder(finalEvList.classes[1], 1)
    unigram_notes.CalculateFreq(list(finalEvList.mainArray[1]))
    if serial:
        for i in range(num_comps):
            n_beats = np.random.choice([6, 7, 8, 10, 12, 14, 16])
            n_meas = 1000 // n_beats
            retVal["surrogate{}({})".format(i, dataset.GetRagaFromRagaId(ragaId))] = Generate(unigram_notes, finalEvList, n_meas=n_meas, talam=n_beats)
    else:
        parallelizer.UniformConcurrentExecutor(_generationAtom, [0, unigram_notes, finalEvList, ragaId, retVal], num_comps)

    return retVal
    # Generate(unigram_dur, finalList)

def _generationAtom(thread_idx, unigram_notes, final_ev_list, ragaId, ret_dict):

    n_beats = np.random.choice([6, 7, 8, 10, 12, 14, 16])
    n_meas = 1000 // n_beats
    # print("Generating on thread: ", thread_idx)
    ret_dict["surrogate{}({})".format(thread_idx, dataset.GetRagaFromRagaId(ragaId))] = Generate(unigram_notes, final_ev_list, n_meas=n_meas, talam=n_beats)


def Generate(NGram, eventlist, n_meas=200, start=None, talam=6):
    """
    :param:
    """
    assert isinstance(NGram, dataStructures.NGramHolder)
    assert isinstance(eventlist, dataStructures.NoteEventList) or isinstance(eventlist, dataStructures.EventList)

    stati_prob_dist = []
    if isinstance(eventlist, dataStructures.EventList):
        stati_prob_dist = eventlist.classFreq[1]

    retVal = []
    if start is None:
        ind = np.random.choice(np.arange(len(NGram.keys)))
        start = NGram.keys[ind]
    if NGram.N != 1:
        # retVal = [*start]
        pass
    else:
        # retVal = [start]
        start = [start]
    accepted = 0
    iters = 0
    normal = lambda x, mu, sigma: (1 / sigma * np.sqrt(2 * np.pi)) * np.exp((-1 / 2) * ((x - mu) / sigma) ** 2)
    eps = 0.0078125
    nbeats = talam
    currBeatLength = 0
    curr_meas = 0
    conts = 0
    while len(retVal) < n_meas * talam:

        i = list(NGram.keys).index(start) if NGram.N > 1 else list(NGram.keys).index(*start)
        # new_probs = NGram.table[i]
        candidate_ind = weighted_sampling(stati_prob_dist)
        iters += 1
        accept_ratio = min(stati_prob_dist[candidate_ind] / stati_prob_dist[i], 1)
        if conts > 3 and len(retVal) > 2:
            retVal.pop(len(retVal) - 1)
            start.pop(-1)
            start.append(retVal[-1][1])
            accepted -= 1
            conts = 0
            continue

        if np.abs(NGram.currents[candidate_ind] - start[-1]) > 10 and NGram.currents[candidate_ind] != 99999 and start[-1] != 99999:
            conts += 1
            continue

        start.append(NGram.currents[candidate_ind])
        bl = randomInversePowerOf2()
        currBeatLength += bl

        if np.ceil(currBeatLength) < nbeats or (nbeats - currBeatLength) > eps:
            if accept_ratio == 1:
                retVal.append((curr_meas, NGram.currents[candidate_ind], bl))
                accepted += 1
            elif accept_ratio > np.random.uniform(0, 1):
                retVal.append((curr_meas, NGram.currents[candidate_ind], bl))
                accepted += 1
        elif np.abs(nbeats - currBeatLength) <= eps:
            if accept_ratio == 1:
                retVal.append((curr_meas, NGram.currents[candidate_ind], bl))
                accepted += 1
            elif accept_ratio > np.random.uniform(0, 1):
                retVal.append((curr_meas, NGram.currents[candidate_ind], bl))
                accepted += 1
            currBeatLength = 0
            curr_meas += 1
        else:
            currBeatLength -= bl
            start.pop(-1)
            continue
        start.pop(0)

        # print("Current Measure: {}, Note: {},  current beat: {}, iters: {}".format(curr_meas, NGram.currents[candidate_ind], currBeatLength, iters))



    # print(retVal[500:520])
    # print("Acceptance rate: {}".format(accepted / iters * 100))
    # print("Number of beats: ", nbeats)
    return retVal



if __name__ == '__main__':
    P = np.zeros((3, 3), dtype='float64')
    P[0, 0] = .6
    P[0, 1]  = .1
    P[0, 2] = .3
    P[1, 0] = .1
    P[1, 1] = .7
    P[1, 2] = .2
    P[2, 0] = .2
    P[2, 1] = .2
    P[2, 2] = .6

    P_tmp = P
    for _ in range(25):
        P_tmp = np.matmul(P_tmp, P)
        print(P_tmp)






