
AH_VOUS_ORIGINAL = {"melody": [], "durations": [], "beat_onset": [], 'rests': []}

SYAMALE_MEENAKSHI = {"melody": [], "durations": [], "beat_onset": [], 'rests': []}

AH_VOUS_ORIGINAL["melody"] = [99999, 0, 0,
                              7, 7, 9, 11, 12, 11,
                              7, 5, 5, 2,
                              4, 4, 0, 2, 2, -1,
                              0, 7, 7,
                              5, 5, 4, 4,
                              4, 2, 7, 7,
                              5, 5, 4, 4,
                              4, 2, 0, 0,
                              7, 7, 9, 11, 11, 12,
                              7, 5, 5, 2,
                              4, 4, 0, 2, 2, -1,
                              0, 99999]
AH_VOUS_ORIGINAL["durations"] = [0.5, 0.25, 0.25, # = 1
                                 0.25, 0.25, 0.125, 0.125, 0.125, 0.125, #= 1
                                 0.5, 0.25, 0.125, 0.125, # = 1
                                 0.25, 0.125, 0.125, 0.25, 0.125, 0.125, # = 1
                                 0.5, 0.25, 0.25, # = 1
                                 0.25, 0.25, 0.25, 0.25, # = 1
                                 0.25, 0.25, 0.25, 0.25, # = 1
                                 0.25, 0.25, 0.25, 0.25, # = 1
                                 0.25, 0.25, 0.25, 0.25, # = 1
                                 0.25, 0.25, 0.125, 0.125, 0.125, 0.125, # = 1
                                 0.5, 0.25, 0.125, 0.125, # = 1
                                 0.25, 0.125, 0.125, 0.25, 0.125, 0.125, # = 1
                                 0.5, 0.5] # = 1
AH_VOUS_ORIGINAL["beat_onset"] = [1, 0, 0,
                                  1, 0, 0, 0, 0, 0,
                                  1, 0, 0, 0,
                                  1, 0, 0, 0, 0, 0,
                                  1, 0, 0,
                                  1, 0, 0, 0,
                                  1, 0, 0, 0,
                                  1, 0, 0, 0,
                                  1, 0, 0, 0,
                                  1, 0, 0, 0, 0, 0,
                                  1, 0, 0, 0,
                                  1, 0, 0, 0, 0, 0,
                                  1, 0]
AH_VOUS_ORIGINAL["rests"] = [0 for i in range(len(AH_VOUS_ORIGINAL["durations"]))]
AH_VOUS_ORIGINAL["rests"][0] = 1
AH_VOUS_ORIGINAL["rests"][-1] = 1

SYAMALE_MEENAKSHI["melody"] = [0, 2, 4, 5,
                               7, 7,
                               9, 11, 12, 11, 9,
                               7, 4,
                               5, 9, 5, 2,
                               4, 7, 4, 0,
                               2, 5, 2, -1,
                               0, 0,
                               7, 7, 7,
                               5, 5, 5,
                               4, 4, 4,
                               2, 2, 2,
                               7, 7, 9, 7,
                               5, 5, 7, 5,
                               4, 4, 5, 4,
                               2, 2, 4, 2]

SYAMALE_MEENAKSHI["beat_onset"] = [1, 0, 0, 0,
                                   1, 0,
                                   1, 0, 0, 0, 0,
                                   1, 0,
                                   1, 0, 0, 0,
                                   1, 0, 0, 0,
                                   1, 0, 0, 0,
                                   1, 0,
                                   1, 0, 0,
                                   1, 0, 0,
                                   1, 0, 0,
                                   1, 0, 0,
                                   1, 0, 0, 0,
                                   1, 0, 0, 0,
                                   1, 0, 0, 0,
                                   1, 0, 0, 0]
SYAMALE_MEENAKSHI["durations"] = [0.375, 0.125, 0.25, 0.25,
                                  0.5, 0.5,
                                  0.25, 0.25, 0.2, 0.1, 0.2,
                                  0.5, 0.5,
                                  0.25, 0.25, 0.25, 0.25,
                                  0.25, 0.25, 0.25, 0.25,
                                  0.375, 0.125, 0.25, 0.25,
                                  0.5, 0.5,
                                  0.5, 0.25, 0.25,
                                  0.5, 0.25, 0.25,
                                  0.5, 0.25, 0.25,
                                  0.5, 0.25, 0.25,
                                  0.5, 0.25, 0.125, 0.125,
                                  0.5, 0.25, 0.125, 0.125,
                                  0.5, 0.25, 0.125, 0.125,
                                  0.5, 0.25, 0.125, 0.125]

PAHI_RAMACHANDRA = {"melody": [], "durations": [], "beat_onset": [], 'rests': []}
PAHI_RAMACHANDRA["melody"] = [0, 2, 4, 5,
                              7, 7,
                              9, 11, 12, 9,
                              7, 4,
                              5, 9, 5, 2,
                              4, 7, 4, 0,
                              2, 5, 2, -1,
                              0, 0,
                              7, 7, 7,
                              5, 5, 5,
                              4, 4, 4,
                              2, 2,
                              7, 7, 11, 9, 7,
                              5, 5, 9, 7, 5,
                              4, 4, 7, 5, 4,
                              2, 2, 4, 2]

PAHI_RAMACHANDRA["durations"] = [0.375, 0.125, 0.25, 0.25,
                                 0.5, 0.5,
                                 0.375, 0.125, 0.25, 0.25,
                                 0.5, 0.5,
                                 0.25, 0.25, 0.25, 0.25,
                                 0.25, 0.25, 0.25, 0.25,
                                 0.25, 0.25, 0.25, 0.25,
                                 0.5, 0.5,
                                 0.5, 0.25, 0.25,
                                 0.5, 0.25, 0.25,
                                 0.5, 0.25, 0.25,
                                 0.75, 0.25,
                                 0.5, 0.125, 0.125, 0.125, 0.125,
                                 0.5, 0.25, 0.08333333, 0.08333333, 0.08333333,
                                 0.5, 0.25, 0.08333333, 0.08333333, 0.08333333,
                                 0.5, 0.25, 0.125, 0.125]
PAHI_RAMACHANDRA["beat_onset"] = [1, 0, 0, 0,
                                  1, 0,
                                  1, 0, 0, 0,
                                  1, 0,
                                  1, 0, 0, 0,
                                  1, 0, 0, 0,
                                  1, 0, 0, 0,
                                  1, 0,
                                  1, 0, 0,
                                  1, 0, 0,
                                  1, 0, 0,
                                  1, 0,
                                  1, 0, 0, 0, 0,
                                  1, 0, 0, 0, 0,
                                  1, 0, 0, 0, 0,
                                  1, 0, 0, 0]

MOZART_THEME = {"melody": [], "durations": [], "beat_onset": [], 'rests': []}

MOZART_THEME["melody"] = [0, 0,
                          7, 7,
                          9, 9,
                          7, 7,
                          5, 5,
                          4, 4,
                          2, 2, 4,
                          0,
                          7, 7,
                          5, 5,
                          4, 4,
                          2, 2,
                          7, 7,
                          5, 5,
                          4, 5, 4, 2, 4, 5,
                          4, 2,
                          0, 0,
                          7, 7,
                          9, 9,
                          7, 7,
                          5, 5,
                          4, 4,
                          2, 4, 2, 0, 2, 4,
                          0]
MOZART_THEME["durations"] = [0.25, 0.25,
                             0.25, 0.25,
                             0.25, 0.25,
                             0.25, 0.25,
                             0.25, 0.25,
                             0.25, 0.25,
                             0.25, 0.1875, 0.0625,
                             0.5,
                             0.25, 0.25,
                             0.25, 0.25,
                             0.25, 0.25,
                             0.25, 0.25,
                             0.25, 0.25,
                             0.25, 0.25,
                             0.25, 0.03125, 0.03125, 0.03125, 0.09375, 0.0625,
                             0.25, 0.25,
                             0.25, 0.25,
                             0.25, 0.25,
                             0.25, 0.25,
                             0.25, 0.25,
                             0.25, 0.25,
                             0.25, 0.25,
                             0.25, 0.03125, 0.03125, 0.03125, 0.09375, 0.0625,
                             0.5]

MOZART_THEME["beat_onset"] = [1, 0,
                              1, 0,
                              1, 0,
                              1, 0,
                              1, 0,
                              1, 0,
                              1, 0, 0,
                              1,
                              1, 0,
                              1, 0,
                              1, 0,
                              1, 0,
                              1, 0,
                              1, 0,
                              1, 0, 0, 0, 0, 0,
                              1, 0,
                              1, 0,
                              1, 0,
                              1, 0,
                              1, 0,
                              1, 0,
                              1, 0,
                              1, 0, 0, 0, 0, 0,
                              1]

TWINKLE_TWINKLE = {"melody": [], "durations": [], "beat_onset": [], 'rests': []}

TWINKLE_TWINKLE["melody"] = [0, 0, 7, 7,
                             9, 9, 7,
                             5, 5, 0, 0,
                             2, 2, 0,
                             7, 7, 5, 5,
                             4, 4, 2,
                             7, 7, 5, 5,
                             4, 4, 2,
                             0, 0, 7, 7,
                             9, 9, 7,
                             5, 5, 4, 4,
                             2, 2, 0]

TWINKLE_TWINKLE["durations"] = [0.25, 0.25, 0.25, 0.25,
                                0.25, 0.25, 0.5,
                                0.25, 0.25, 0.25, 0.25,
                                0.25, 0.25, 0.5,
                                0.25, 0.25, 0.25, 0.25,
                                0.25, 0.25, 0.5,
                                0.25, 0.25, 0.25, 0.25,
                                0.25, 0.25, 0.5,
                                0.25, 0.25, 0.25, 0.25,
                                0.25, 0.25, 0.5,
                                0.25, 0.25, 0.25, 0.25,
                                0.25, 0.25, 0.5]

GOOSEY_GOOSEY_GANDER = {"melody": [], "durations": [], "beat_onset": [], 'rests': []}

GOOSEY_GOOSEY_GANDER["melody"] = [0, 2, 0, 4, 7, 7,
                                  9, 7, 9, 12, 7, 7,
                                  5, 5, 5, 4, 4, 4,
                                  2, 5, 2, -1, 0, 0,
                                  0, 2, 0, 4, 7, 7, 7,
                                  9, 7, 9, 12, 7, 7, 7,
                                  9, 12, 7, 4, 9, 5, 5,
                                  4, 4, 2, 2, 0]

GOOSEY_GOOSEY_GANDER["durations"] = [0.125, 0.125, 0.125, 0.125, 0.25, 0.25,
                                     0.125, 0.125, 0.125, 0.125, 0.25, 0.25,
                                     0.25, 0.125, 0.125, 0.25, 0.125, 0.125,
                                     0.125, 0.125, 0.125, 0.125, 0.25, 0.25,
                                     0.125, 0.125, 0.125, 0.125, 0.25, 0.125, 0.125,
                                     0.125, 0.125, 0.125, 0.125, 0.25, 0.125, 0.125,
                                     0.125, 0.125, 0.125, 0.125, 0.25, 0.125, 0.125,
                                     0.125, 0.125, 0.125, 0.125, 0.5]
GOOSEY_GOOSEY_GANDER["beat_onset"] = [1, 0, 0, 0, 0, 0,
                                      1, 0, 0, 0, 0, 0,
                                      1, 0, 0, 0, 0, 0,
                                      1, 0, 0, 0, 0, 0,
                                      1, 0, 0, 0, 0, 0, 0,
                                      1, 0, 0, 0, 0, 0, 0,
                                      1, 0, 0, 0, 0, 0, 0,
                                      1, 0, 0, 0, 0]


MOZART_VARIATION1 = {"melody": [], "durations": [], "beat_onset": [], 'rests': []}

MOZART_VARIATION1["melody"] = [2, 0, -1, 0, -1, 0, -1, 0,
                               9, 8, 5, 7, 5, 7, 5, 7,
                               8, 9, 12, 11, 14, 12, 11, 9,
                               9, 7, 16, 14, 12, 11, 9, 7,
                               7, 5, 14, 12, 11, 9, 7, 5,
                               5, 4, 12, 11, 9, 7, 5, 4,
                               2, 9, 7, -1,
                               0, 99999]
MOZART_VARIATION1["durations"] = [0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625,
                                  0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625,
                                  0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625,
                                  0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625,
                                  0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625,
                                  0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625,
                                  0.125, 0.125, 0.125, 0.125,
                                  0.25, 0.25]
MOZART_VARIATION1["beat_onset"] = [1, 0, 0, 0, 0, 0, 0, 0,
                                   1, 0, 0, 0, 0, 0, 0, 0,
                                   1, 0, 0, 0, 0, 0, 0, 0,
                                   1, 0, 0, 0, 0, 0, 0, 0,
                                   1, 0, 0, 0, 0, 0, 0, 0,
                                   1, 0, 0, 0, 0, 0, 0, 0,
                                   1, 0, 0, 0,
                                   1, 0]
MOZART_VARIATION1['rests'] = [0 if i != 99999 else 1 for i in MOZART_VARIATION1["melody"]]

MOZART_VARIATION2 = {"melody": [], "durations": [], "beat_onset": [], 'rests': []}

MOZART_VARIATION2["melody"] = [0, 0,
                               7, 7,
                               9, 5,
                               7, 4,
                               0, 2,
                               2, -3] # TODO: Variation 2 incomplete

MOZART_VARIATION3 = {"melody": [], "durations": [], "beat_onset": [], 'rests': []}
MOZART_VARIATION3["melody"] = [-12, -8, -5, 0, 4, 7,
                               12, 7, 5, 4, 2, 0,
                               10, 7, 9, 12, 11, 9,
                               10, 5, 7, 7, 12, 16,
                               16, 5, 5, 5, 11, 14,
                               14, 4, 4, 4, 9, 12,
                               12, 2, 9, 9, 7, -1,
                               0, 99999]

MOZART_VARIATION3["durations"] = [0.08333333, 0.08333333,0.08333333,0.08333333,0.08333333,0.08333333,
                                  0.08333333, 0.08333333,0.08333333,0.08333333,0.08333333,0.08333333,
                                  0.08333333, 0.08333333,0.08333333,0.08333333,0.08333333,0.08333333,
                                  0.08333333, 0.08333333,0.08333333,0.08333333,0.08333333,0.08333333,
                                  0.08333333, 0.08333333,0.08333333,0.08333333,0.08333333,0.08333333,
                                  0.08333333, 0.08333333,0.08333333,0.08333333,0.08333333,0.08333333,
                                  0.08333333, 0.08333333,0.08333333,0.08333333,0.08333333,0.08333333,
                                  0.25, 0.25]
MOZART_VARIATION3["beat_onset"] = [1, 0, 0, 0, 0, 0,
                                   1, 0, 0, 0, 0, 0,
                                   1, 0, 0, 0, 0, 0,
                                   1, 0, 0, 0, 0, 0,
                                   1, 0, 0, 0, 0, 0,
                                   1, 0, 0, 0, 0, 0,
                                   1, 0, 0, 0, 0, 0,
                                   1, 0]

MOZART_VARIATION4 = {"melody": [], "durations": [], "beat_onset": [], 'rests': []}
#### TODO: Variation 4 incomplete

MOZART_VARIATION5 = MOZART_VARIATION4
MOZART_VARIATION5["melody"] = [0, 99999, 0,
                               7, 99999, 7,
                               9, 99999, 9,
                               7, 999999, 7,
                               999999, 4, 999999, 2,
                               999999, 2, 999999, 0,
                               999999, 0, 999999, 1,
                               0, 999999]

MOZART_VARIATION5["durations"] = [0.25, 0.125, 0.125,
                                  0.25, 0.125, 0.125,
                                  0.25, 0.125, 0.125,
                                  0.25, 0.125, 0.125,
                                  0.125, 0.125, 0.125, 0.125,
                                  0.125, 0.125, 0.125, 0.125,
                                  0.125, 0.125, 0.125, 0.125,
                                  0.25, 0.25]
MOZART_VARIATION5["beat_onset"] = [1, 0, 0,
                                  1, 0, 0,
                                  1, 0, 0,
                                  1, 0, 0,
                                  1, 0, 0, 0,
                                  1, 0, 0, 0,
                                  1, 0, 0, 0,
                                  1, 0]


MOZART_VARIATION6 = {"melody": [], "durations": [], "beat_onset": [], 'rests': []}
#### TODO: VARIATION 6 incomplete


MOZART_VARIATION7 = {"melody": [], "durations": [], "beat_onset": [], 'rests': []}
MOZART_VARIATION7["melody"] = [-12, -10, -8, -7, -5, -3, -1,
                               0, 2, 4, 5, 7, 9, 11, 12,
                               11, 10, 7, 9, 14, 12, 11, 9,
                               9, 8, 5, 7, 99999, 7, 16, 7,
                               99999, 5, 16, 5, 99999, 5, 14, 5,
                               99999, 4, 14, 4, 99999, 4, 12, 4,
                               99999, 2, 12, 2, 99999, 2, 11, 2,
                               12, 99999]

MOZART_VARIATION7["durations"] = [0.125, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625,
                                  0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625,
                                  0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625,
                                  0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625,
                                  0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625,
                                  0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625,
                                  0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625,
                                  0.25, 0.25]
MOZART_VARIATION7["beat_onset"] = [1, 0, 0, 0, 0, 0, 0,
                                  1, 0, 0, 0, 0, 0, 0, 0,
                                  1, 0, 0, 0, 0, 0, 0, 0,
                                  1, 0, 0, 0, 0, 0, 0, 0,
                                  1, 0, 0, 0, 0, 0, 0, 0,
                                  1, 0, 0, 0, 0, 0, 0, 0,
                                  1, 0, 0, 0, 0, 0, 0, 0,
                                  1, 0]

def GetAll():
    return [AH_VOUS_ORIGINAL, SYAMALE_MEENAKSHI, PAHI_RAMACHANDRA, TWINKLE_TWINKLE, GOOSEY_GOOSEY_GANDER,  MOZART_THEME, MOZART_VARIATION1, MOZART_VARIATION3, MOZART_VARIATION5, MOZART_VARIATION7]

def GetLabels():
    return ["Ah! vous dirai-je(1774)", "Shaymale Meenakshi(1905)", "Pahi Ramachandra(oral)", "The Star(1838)", "Goosey Goosey Gander(1784)",  "Ah! vous dirai-je(1785)", "Mozart-Variation 1(1785)", "Mozart-Variation 3(1785)", "Mozart-Variation 5(1785)", "Mozart-Variation 7(1785)"]

def GetMeasureData(dict):
    lines = []

    iter = 0
    lines_done = -1
    curr_line = []
    while iter < len(dict["melody"]):

        if dict["beat_onset"][iter] == 1:
            lines_done += 1
            curr_line = []

        curr_line.append(dict["melody"][iter])


        if  curr_line not in lines:
            lines.append(curr_line)

        iter = iter + 1

    return lines




def GetNMeasures(dict, n, start=1):
    mel = dict["melody"]
    final = []
    indices = []
    num_measures_encountered = -1
    iter = 0
    add = False
    while iter < len(mel):
        if dict["beat_onset"][iter] == 1:
            num_measures_encountered += 1
        if n != 'all':
            if num_measures_encountered == start - 1:
                add = True

            if num_measures_encountered == start + n - 1:
                iter = 99999
        else:
            add = True

        if iter != 99999 and add:
            final.append(mel[iter])
            indices.append(iter)

        iter += 1

    return final, indices

def GetNMeasuresAdjusted(dict, n, start=1):
    get_int_dur_array()
    mel, indices = GetNMeasures(dict, n, start)
    n_mel = len(mel)
    dur_ints = dict["int_durations"][indices[0]:indices[n_mel - 1]]
    final = []
    for dur, m in zip(dur_ints, mel):
        for i in range(dur):
            final.append(m)
    return final

def get_least_duration():
    data = GetAll()
    min_dur = 2
    for dict in data:
        for dur in dict["durations"]:
            print("duration: {}, {}".format(dur, dur * 480))
    return min_dur

import math

def get_int_dur_array():
    data = GetAll()
    for dict in data:
        dict["int_durations"] = []
        for dur in dict["durations"]:
            dict["int_durations"].append(math.ceil(dur*48))


def compute_adjusted_melody():
    data = GetAll()
    get_int_dur_array()
    for dict in data:
        dict["adjusted_melody"] = []
        for dur, mel in zip(dict["int_durations"], dict["melody"]):
            for i in range(dur):
                dict["adjusted_melody"].append(mel)

def PruneRests(arr):
    final = []
    for ele in arr:
        if not ele >= 99999:
            final.append(ele)
    return final

if __name__ == '__main__':
    # print("min dur: {}".format(get_least_duration()))
    # print("names: {}".format(GetLabels()))
    # print(GetNMeasuresAdjusted(SYAMALE_MEENAKSHI, 'all'))
    # print(PruneRests(GetNMeasuresAdjusted(MOZART_VARIATION5, 'all')))
    dicts = GetAll()
    x = dicts[1]["melody"]
    y = dicts[1]["durations"]
    z = []
    z_start = -1
    for ele in dicts[1]["beat_onset"]:
        if ele == 1:
            z_start += 1
        z.append(z_start)
    x1 = dicts[2]["melody"]
    y1 = dicts[2]["durations"]
    z1 = []
    z1_start = -1
    for ele in dicts[2]["beat_onset"]:
        if ele == 1:
            z1_start += 1
        z1.append(z1_start)

    from mpl_toolkits import mplot3d
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    ax.plot3D(x, z, y, 'black')
    ax.plot3D(x1, z1, y1, 'red')
    ax.set_title("Syamale Meenakshi(black) vs Pahi Ramchandra(red)")
    plt.show()
