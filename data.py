
#### TODO: Define a more systematic way of manually parsing notations, in case the use of auto-parser is not needed/infeasible

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

TWINKLE_TWINKLE["beat_onset"] = [1, 0, 0, 0,
                                 1, 0, 0,
                                 1, 0, 0, 0,
                                 1, 0, 0,
                                 1, 0, 0, 0,
                                 1, 0, 0,
                                 1, 0, 0, 0,
                                 1, 0, 0,
                                 1, 0, 0, 0,
                                 1, 0, 0,
                                 1, 0, 0, 0,
                                 1, 0, 0]


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
                               2, -3]

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

Quick_March = {"beat_onset": [], "melody": [], "durations": [], 'rests': []}

Quick_March["melody"] = [7, 12, 12, 11, 12,
                        16, 12, 16, 12,
                        7, 12, 16, 12,
                        16, 14, 14, 14, 7,
                        7, 12, 12, 11, 12,
                        16, 12, 16, 12,
                        7, 12, 16, 12,
                        14, 12, 12, 12]
Quick_March["durations"] = [0.25, 0.125, 0.125, 0.125, 0.125,
                        0.25, 0.125, 0.25, 0.125,
                        0.25, 0.125, 0.25, 0.125,
                        0.125, 0.125, 0.125, 0.25, 0.125,
                        0.25, 0.125, 0.125, 0.125, 0.125,
                        0.25, 0.125, 0.25, 0.125,
                        0.25, 0.125, 0.25, 0.125,
                        0.125, 0.125, 0.125, 0.375]

Quick_March["Measure"] = [0, 0, 0, 0, 0,
                          1,1,1,1,
                          2, 2, 2, 2,
                          3, 3, 3, 3, 3,
                          4, 4, 4, 4, 4,
                          5, 5, 5, 5,
                          6, 6, 6, 6,
                          7, 7, 7, 7]

Quick_March[" Duration"] = [i / 0.75 for i in Quick_March["Measure"]]

British_Grenadaire = {"Measure": [], " Note": [], " Duration": []}

British_Grenadaire[" Note"] = [12, 7, 12, 14,
                               17, 16, 14, 16,
                               17, 16, 14, 12,
                               14, 14, 14, 14, 7,
                               12, 7, 12, 14,
                               16, 14, 16, 17,
                               19, 12, 16, 14, 12, 11,
                               12]

British_Grenadaire[" Duration"] = [3/16, 1/16, 1/8, 1/8,
                               3/16, 1/16, 1/8, 1/8,
                               3/16, 1/16, 1/8, 1/8,
                               1/8, 1/16, 1/16, 1/8, 1/8,
                               3/16, 1/16, 1/8, 1/8,
                               1/4, 1/8, 1/16, 1/16,
                               1/8, 1/8, 1/16, 1/16, 1/16, 1/16,
                               1/2]

British_Grenadaire["Measure"] = [0, 0, 0, 0,
                               1, 1, 1, 1,
                               2, 2, 2, 2,
                               3, 3, 3, 3, 3,
                               4, 4, 4, 4,
                               5, 5, 5, 5,
                               6, 6, 6, 6, 6, 6,
                               7]

British_Grenadaire[" Duration"] = [i* 2 for i in British_Grenadaire[" Duration"]]


#### TODO: ALl the manually parsed compositions defined above should be encapsulated in a data class.
#### The class may also cover the following methods as members

def GetAll():
    """
    Get a list of parsed compositions. GetLabels() prints the corresponding labels
    """
    return [AH_VOUS_ORIGINAL, SYAMALE_MEENAKSHI, PAHI_RAMACHANDRA, TWINKLE_TWINKLE, GOOSEY_GOOSEY_GANDER,  MOZART_THEME, MOZART_VARIATION1, MOZART_VARIATION3, MOZART_VARIATION5, MOZART_VARIATION7]

def GetLabels():
    """
    returns, as a list, the labels for the compositions returned in GetAll()
    """
    return ["Ah! vous dirai-je(1774)", "Shaymale Meenakshi(1905)", "Pahi Ramachandra(oral)", "The Star(1838)", "Goosey Goosey Gander(1784)",  "Ah! vous dirai-je(1785)", "Mozart-Variation 1(1785)", "Mozart-Variation 3(1785)", "Mozart-Variation 5(1785)", "Mozart-Variation 7(1785)"]

def GetSignificantLabels():
    """
    returns, as a list, the labels for a subset of compositions in GetAll()
    """
    return ["Ah! Vous Dirai-Je (1774)(celtic)", "Shaymale Meenakshi (1905)", "Pahi Ramachandra (Traditional)", "The Star (1838)(celtic)", "Goosey Goosey Gander (1784)(celtic)",  "Ah! Vous Dirai-Je(1785)(celtic)"]


def GetMeasureData(dict):
    """
    Get a list of all the measures in a given composition. These measure
    :param dict -> a Dictionary: The composition whose measure data is expected
    :return lines -> list: a list of all the measures, containing the melody information at each measure
    """
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

def GetEuclideanData(dict, n, start=1):
    """
    Converts the parsed data in :param dict to a 3D format, and returns that list
    :param dict -> Dictionary: the parsed composition
    :param n -> int/string: number of full measures to be parsed. The value of 'all' will process the full song
    :param start -> int:  the starting measure. The default value of 1 starts from the first measure.
    :return Tuple -> (list(Tuple), list(int)): where each element in the list(Tuple) is a Tuple of the form
                    (measure_index, pitch_index, event_duration), and list(int) is a list of indices with legitimate
                    pitches i.e. ignoring the index positions of rests.
    """
    mel=dict["melody"]
    dur=dict["durations"]
    meas_dat = dict["beat_onset"]
    meas_start = -1
    meas = []
    for d in meas_dat:
        if d == 1:
            meas_start += 1
        meas.append(meas_start)

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

        if iter < 99999:
            if not (mel[iter] < 99999):
                add = False
        if iter < 99999 and add:
            final.append(( meas[iter], mel[iter], dur[iter]))
            indices.append(iter)

        iter += 1

    return final, indices


def GetNMeasures(dict, n, start=1):
    """
    returns the melody of the composition :paran dict, :param n measures beginning at :param start - 1
    :param dict -> Dictionary: the parsed composition
    :param n -> int/string: number of full measures to be parsed. The value of 'all' will process the full song
    :param start -> int:  the starting measure. The default value of 1 starts from the first measure.
    :return Tuple -> (list(int), list(int)): where each element in the first list(int) is a pitch index,
                    and list(int) is a list of indices with legitimate pitches i.e. ignoring
                    the index positions of rests.
    """
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

        if iter < 99999 and add:
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

import numpy as np
def GetAdjustedMelody(euclideanData):
    ret = []
    for ele in euclideanData:
        int_duration = math.ceil(ele[2] * 480)
        if ele[1] < 99999:
            for i in range(int_duration):
                ret.append(ele[1] + 36)
    return np.array(ret, dtype='int64')

def GetSevenScale(arr, scale="mayamalavagowla"):
    # Raga Mayamalavagowla
    # 0 = 0
    # 1 = 1
    # 4 = 2
    # 5 = 3
    # 7 = 4
    # 8 = 5
    # 11 = 6
    scale_arr = []
    if scale == "mayamalavagowla":
        scale_arr = [0,1, 4, 5, 7, 8, 11]

    new_arr = []
    for ele in arr:
        if ele == 99999:
            new_arr.append(ele)
        elif ele in scale_arr:
            new_arr.append(scale_arr.index(ele))


    return new_arr



def GetSongCoords2d(coords3d):
    measures = -1
    retVal = []
    cum_dur = -1
    for i in range(len(coords3d["beat_onset"])):
        if coords3d["beat_onset"][i] == 1:
            measures = measures + 1
            cum_dur = coords3d["durations"][i]
        else:
            cum_dur += coords3d["durations"][i]

        x = measures + cum_dur
        y = coords3d["melody"][i]
        retVal.append((x, y))
    return retVal


############################ DEPRECATED FUNCTIONS ######################################################################

# Deprecated: DO NOT USE! use utils.plotter.handleRests() or fabricate something similar to that
def PruneRests(arr):
    final = []
    for ele in arr:
        if not ele >= 9999:
            final.append(ele)
    return final

# Deprecated: DO NOT USE! use utils.plotter.handleRests() or fabricate something similar to that
def PruneRestsMultiAxis(coords, note_axis=0):
    new_arr = []
    for c in coords:
        if c[note_axis] < 99999:
            new_arr.append(c)
    return new_arr



# Deprecated: Use utils.dataStructures.UnpackTuples() instead
def xtractAxes(tupList):
    size = len(tupList[0])
    retval = []
    for i in range(size):
        retval.append([])

    for item in tupList:
        for i in range(size):
            retval[i].append(item[i])
    return retval

from utils.player import Player

if __name__ == '__main__':
    # print("min dur: {}".format(get_least_duration()))
    # print("names: {}".format(GetLabels()))
    # print(GetNMeasuresAdjusted(SYAMALE_MEENAKSHI, 'all'))
    # print(PruneRests(GetNMeasuresAdjusted(MOZART_VARIATION5, 'all')))
    # dicts = GetAll()
    # x = dicts[1]["melody"]
    # y = dicts[1]["durations"]
    # z = []
    # z_start = -1
    # for ele in dicts[1]["beat_onset"]:
    #     if ele == 1:
    #         z_start += 1
    #     z.append(z_start)
    # x1 = dicts[2]["melody"]
    # y1 = dicts[2]["durations"]
    # z1 = []
    # z1_start = -1
    # for ele in dicts[2]["beat_onset"]:
    #     if ele == 1:
    #         z1_start += 1
    #     z1.append(z1_start)
    #
    # from mpl_toolkits import mplot3d
    # import matplotlib.pyplot as plt
    # fig = plt.figure()
    # ax = plt.axes(projection="3d")
    # ax.plot3D(x, z, y, 'black')
    # ax.plot3D(x1, z1, y1, 'red')
    # ax.set_title("Syamale Meenakshi(black) vs Pahi Ramchandra(red)")
    # plt.show()
    # print(GetEuclideanData(AH_VOUS_ORIGINAL, 4, 1)[0])
    # print(xtractAxes(GetSongCoords2d(SYAMALE_MEENAKSHI)))
    # p = Player(SYAMALE_MEENAKSHI, "syamale")
    # p1 = Player(AH_VOUS_ORIGINAL, "ah_orig")
    # p2 = Player(MOZART_THEME, "ah_moz")
    # p3 = Player(MOZART_VARIATION5, "moz_5")
    # p4 = Player(GOOSEY_GOOSEY_GANDER, "goose")
    p5 = Player(label='british_grenadire', note_len=44100)
    p5.compute_variables(Quick_March)
