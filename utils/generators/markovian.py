from utils import dataStructures, dataset, parallelizer
import numpy as np
from tqdm import tqdm

def weighted_sampling(weights):
    """
    Weighted sampling based on a given set of weights, which are passed as the argument.
    Weights are expected to be integers. Visit https://peteroupc.github.io/randomfunc.html#General_Non_Uniform_Distributions for details
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
    r = np.random.normal(0, 1)
    while r < 0:
        r = np.random.normal(0, 1)

    return 2 ** (-np.floor(r))

def GenerateForRaga(ragaId='22', num_comps=10, comp_length=1000, serial=False):
    """
    Function for generating surrogate data for a given raga. This function primarily represents the raga as a Markov Chain,
    computes the transitions matrices and other relevant stuff, and calls the extension function @Generate for final
    generation.
    :param ragaId: ID of the raga whose surrogates need to be generated
    :param num_comps: Number of surrogate compositions to be generated
    :param comp_length: Number of note-events in each composition
    :param serial: Whether to run on single core or multiple cores.
    :return: returns a Dictionary with strings of the patter "Surrogate{1....num_comps}" as keys and a bunch of 3-Tuples
            as values
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

    unigram_notes = dataStructures.NGramHolder(finalEvList.classes[1], 1)
    unigram_notes.CalculateFreq(list(finalEvList.mainArray[1]))
    if serial:
        for i in tqdm(range(num_comps)):
            n_beats = np.random.choice([6, 7, 8, 10, 12, 14, 16])
            n_meas = comp_length // n_beats
            retVal["surrogate{}({})".format(i, dataset.GetRagaFromRagaId(ragaId))] = Generate(unigram_notes, finalEvList, n_meas=n_meas, talam=n_beats)
    else:
        parallelizer.UniformConcurrentExecutor(_generationAtom, [0, unigram_notes, finalEvList, ragaId, retVal], comp_length)

    return retVal

def _generationAtom(thread_idx, unigram_notes, final_ev_list, ragaId, ret_dict, comp_length=1000):

    n_beats = np.random.choice([6, 7, 8, 10, 12, 14, 16])
    n_meas = comp_length // n_beats
    # print("Generating on thread: ", thread_idx)
    ret_dict["surrogate{}({})".format(thread_idx, dataset.GetRagaFromRagaId(ragaId))] = Generate(unigram_notes, final_ev_list, n_meas=n_meas, talam=n_beats)


def Generate(NGram, eventlist, n_meas=200, start=None, talam=6):
    """
    Returns the final generated surrogates, one by one.
    :param NGram: The transition matrix of the raga. For more details, visit
                Chapter 3 of "Jurafsky, D., 2000. Speech & language processing. Pearson Education India."
    :param eventlist: Conglomerated EventList of all the compositions in a given raga
    :param n_meas: Number of measures to be generated
    :param start: If it is preferable to start a surrogate composition with a specified pitch, it should be specified
            here
    :param talam: The total number of counts in every avartanam of the talam is specified here
    :return: A list of 3-Tuples (measure index, pitch index, event duration) of length (n_meas * talam)
    """
    assert isinstance(NGram, dataStructures.NGramHolder)
    assert isinstance(eventlist, dataStructures.NoteEventList) or isinstance(eventlist, dataStructures.EventList)

    prob = np.array([e / e.sum() for e in NGram.table])
    stati_prob_dist = prob

    for _ in range(40):
        stati_prob_dist = np.matmul(stati_prob_dist, prob)

    d_1 = 0
    for i in range(1, len(NGram.currents)):
        if NGram.currents[i] - NGram.currents[i-1] == 1:
           d_1 += 1

    stat_int_dist = stati_prob_dist * 1000
    stat_int_dist = stat_int_dist.astype('int64')

    # print("1semitone differences: {}, total alphabet: {}".format(d_1, len(NGram.currents)))
    seven = not((len(NGram.currents) - d_1) > 2)
    # print("seven-tonal: ", seven)

    retVal = []
    if start is None:
        ind = weighted_sampling(stat_int_dist[-1])
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

    rest = 1 - min(0.2, stati_prob_dist[-1][-1])
    # pbar = tqdm(total=n_meas * talam + 1)

    while len(retVal) < n_meas * talam:
        unif_no = np.random.uniform(0, 1)

        i = list(NGram.keys).index(start) if NGram.N > 1 else list(NGram.keys).index(*start)
        # new_probs = NGram.table[i] weighted_sampling(stati_prob_dist[-2])
        candidate_ind = weighted_sampling(NGram.table[i]) #if unif_no <= rest else len(NGram.currents) - 1 # int(np.random.normal(i, 1))
        # if unif_no < rest and (candidate_ind < 0 or candidate_ind > len(NGram.currents) - 2):
        #     continue
        iters += 1
        rf = stati_prob_dist[-1][candidate_ind] / stati_prob_dist[-1][i] if unif_no < rest else 1

        rg =  normal(i, candidate_ind, 1) / normal(candidate_ind, i, 1) #if unif_no < rest else 1
        accept_ratio = min(rf * rg, 1)

        if conts > 300:
            """
            In case the loop gets stuck due to the `if` statement immediately after this one (line 167), 
            this condition chooses a previous candidate index in order to break the loop. 
            Hack, but works 
            """
            ele = start.pop(-1)
            if seven and ele > 7: start.append(ele - 7)
            elif seven and ele < 0: start.append(ele + 7)
            elif not seven and ele > 12: start.append(ele - 12)
            elif not seven and ele < 0 : start.append(ele + 12)
            else: start.append(ele)
            conts = 0

        diff_cond = np.abs(NGram.currents[candidate_ind] - start[-1]) > 6 if seven else np.abs(NGram.currents[candidate_ind] - start[-1]) > 10
        if diff_cond and NGram.currents[candidate_ind] != 99999 and start[-1] != 99999:
            conts += 1
            continue

        start.append(NGram.currents[candidate_ind])
        bl = randomInversePowerOf2()
        currBeatLength += bl

        if np.ceil(currBeatLength) < nbeats or (nbeats - currBeatLength) > eps:
            retVal.append((curr_meas, NGram.currents[candidate_ind], bl))
            accepted += 1

        elif np.abs(nbeats - currBeatLength) <= eps:
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


    # Diagnostic Code
    # print(retVal[500:520])
    # seven_tonal = ['s', 'r', 'g', 'm', 'p', 'd', 'n', ';']
    # l = []
    # ev_list = retVal[700:720]
    # pbar.close()
    # for i in range(20):
    #     if int(ev_list[i][1]) > 9999:
    #         l.append(seven_tonal[7])
    #     elif int(ev_list[i][1]) >= 0 and int(ev_list[i][1]) < 9999:
    #         l.append(seven_tonal[int(ev_list[i][1]) % 7] + '*' * (int(ev_list[i][1])//7) )
    #     elif int(ev_list[i][1]) + 7 >= 0:
    #         l.append(seven_tonal[int(ev_list[i][1]) + 7] + '_')
    #     else:
    #         l.append(seven_tonal[int(ev_list[i][1]) + 14] + '__')
    #
    # print(l)
    # print("Acceptance rate: {}".format(accepted / iters * 100))
    # print("Number of beats: ", nbeats)
    return retVal


#
# if __name__ == '__main__':
#     P = np.zeros((3, 3), dtype='float64')
#     P[0, 0] = .6
#     P[0, 1]  = .1
#     P[0, 2] = .3
#     P[1, 0] = .1
#     P[1, 1] = .7
#     P[1, 2] = .2
#     P[2, 0] = .2
#     P[2, 1] = .2
#     P[2, 2] = .6
#
#     P_tmp = P
#     for _ in range(25):
#         P_tmp = np.matmul(P_tmp, P)
#         print(P_tmp)
#
#
#



