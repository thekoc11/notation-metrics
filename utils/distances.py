import ETC
from scipy.spatial.distance import hamming
import numpy as np
# import similaritymeasures

def LCSubSeq(X, Y, m, n):
    """
    Longest Common Subsequence in X (of length m) and Y (of length n). Naturally, len(subsequence) <= min(m, n)
    """
    LCSuff = [[0 for k in range (n+1)] for l in range(m+1)]
    result = 0

    for i in range(m+1):
        for j in range(n+1):
            if (i==0 or j==0):
                LCSuff[i][j] =  0
            elif (X[i-1] == Y[j - 1]):
                LCSuff[i][j] = LCSuff[i-1][j-1] + 1
                result = max(result, LCSuff[i][j])
            else:
                LCSuff[i][j] = 0
    return result

def editDist(X, Y, m, n, normalize_len=False):
    """
    Returns the edit distance between array-likes X and Y
    :param X: array-like
    :param Y: array-like
    :param m: length of X
    :param n: length of Y
    :return: (int) minimum number of edits required to make X = Y
    """
    if normalize_len:
        if m < n:
            quot = n // m
            new_X = []
            for i in range(quot):
                new_X += X
            X = new_X
            # print("Normalized length for X: {}".format(len(X)))
        else:
            quot = m // n
            new_Y = []
            for i in range(quot):
                new_Y += Y
            Y = new_Y
            # print("Normalized length for Y: {}".format(len(Y)))


    dp = [[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):

            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif X[i-1] == Y[j-1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i-1][j], dp[i-1][j-1])

    return dp[m][n]

def etcDist(seq_x, seq_y, normalize_len=False):
    """
    Returns the ETC distance between the two sequences
    :param seq_x: array-like
    :param seq_y: array-like
    :return: (int) ETC distance between the sequences
    """
    if normalize_len:
        m = len(seq_x)
        n = len(seq_y)
        if m < n:
            quot = n // m
            new_X = []
            for i in range(quot):
                new_X += list(seq_x)
            seq_x = new_X
        else:
            quot = m // n
            new_Y = []
            for i in range(quot):
                new_Y += list(seq_y)
            seq_y = new_Y

    # Compute ETC of individual sequences
    seq_x_ETC = ETC.compute_1D(seq_x, order=2, verbose=False, truncate=True)["ETC1D"]
    seq_y_ETC = ETC.compute_1D(seq_y, order=2, verbose=False, truncate=True)["ETC1D"]

    # Compute ETC of concatenated sequences
    seq_xy_ETC = ETC.compute_1D(seq_x + seq_y, order=2, verbose=False, truncate=True)["ETC1D"]
    seq_yx_ETC = ETC.compute_1D(seq_y + seq_x, order=2, verbose=False, truncate=True)["ETC1D"]

    # Compute dETC as defined in Otu and Sayood 2003 as Distance Measure 3
    # Refer: http://europepmc.org/article/MED/14594718
    dETC = 0.5 * (seq_xy_ETC + seq_yx_ETC - seq_x_ETC - seq_y_ETC)  # take average

    # Return a dictionary of results
    return dETC

def hammingDist(X, Y, m, n):
    if m < n:
        Y = Y[0:m]
    elif n < m:
        X = X[0: n]

    dist = hamming(X, Y)
    return dist

def dtwDist(X, Y, m, n):
    """
    Computes the Dynamic Time-Warping distance between two one-dimensional sequences
    :param X: array_like
    :param Y: array_like
    :param m: length of X
    :param n: length of Y
    :return: int -> DTW distance between X and Y
    """
    dtw = np.zeros((m + 1, n + 1), dtype='int64')
    for i in range(m + 1):
        for j in range(n + 1):
            dtw[i, j] = 99999
    dtw[0, 0] = 0

    for i in range(1, m+1):
        for j in range(1, n + 1):
            cost = abs(X[i - 1] - Y[j - 1])
            last_min = np.min([dtw[i, j-1], dtw[i - 1, j], dtw[i-1, j-1]])
            dtw[i, j] = cost  + last_min
    # print(dtw)
    return dtw[m, n]

def dtwDistSymbolic(X, Y, m, n):
    """
    Symbolic DTW computes a distance similar to DTW on symbols whose magnitudes can not be computed.
    In this scenario, cost = 0 if X[i] == Y[j] else 1
    :param X: array_like
    :param Y: array_like
    :param m: int -> length of X
    :param n: int -> length of Y
    :return: int -> comparative similarity between two symbolic sequences
    """
    dtw = np.zeros((m + 1, n + 1), dtype='int64')
    C = []
    for i in range(m + 1):
        for j in range(n + 1):
            dtw[i, j] = 99999
    dtw[0, 0] = 0

    for i in range(1, m+1):
        for j in range(1, n + 1):
            cost = 0 if X[i - 1] == Y[j - 1] else 1
            last_min = np.min([dtw[i, j-1], dtw[i - 1, j], dtw[i-1, j-1]])
            dtw[i, j] = cost  + last_min
    # print(dtw)
    return dtw[m, n]


def dtwEuclidean(X, Y):
    """
    Euclidean DTW is able to compute DTW distance between two multidimensional arrays (assuming both have the same
    dimensionality) by computing the euclidean distance between the individual elements.
    Read More: https://en.wikipedia.org/wiki/Dynamic_time_warping
    :param X: multidimensional array_like
    :param Y: multidimensional array_like
    :return: float64 -> DTW distance
    """
    m = len(X)
    n = len(Y)

    dtw = np.zeros((m + 1, n + 1), dtype='float64')
    for i in range(m + 1):
        for j in range(n + 1):
            dtw[i, j] = 99999
    dtw[0, 0] = 0

    for i in range(1, m+1):
        for j in range(1, n + 1):
            cost = _euclideanDistance(X[i - 1], Y[j - 1]) #0 if X[i - 1] == Y[j - 1] else 1
            last_min = np.min([dtw[i, j-1], dtw[i - 1, j], dtw[i-1, j-1]])
            dtw[i, j] = cost  + last_min
    # print(dtw)
    return dtw[m, n]

def frechetEuclidean(X, Y):
    """
    Euclidean Frechet is able to compute the Frechet distance between two multidimensional arrays
    (assuming both have the same dimensionality) by computing the euclidean distance between the individual elements.
    Read More: https://en.wikipedia.org/wiki/Fr%C3%A9chet_distance
    :param X: multidimensional array_like
    :param Y: multidimensional array_like
    :return: float64 -> Frechet distance
    """
    m = len(X)
    n = len(Y)
    ca = np.zeros((m, n), dtype='float64')
    ca.fill(-1.0)

    def calculate(i, j):
        if ca[i, j] > -1.0:
            return ca[i, j]

        d = _euclideanDistance(X[i], Y[j])
        if i == 0 and j == 0:
            ca[i, j] = d
        elif i > 0 and j == 0:
            ca[i,  j] = max(calculate(i-1, 0), d)
        elif i == 0 and j > 0:
            ca[i, j] = max(calculate(0, j-1), d)
        elif i > 0 and j > 0:
            ca[i, j] = max(min(calculate(i - 1, j),
                               calculate(i - 1, j - 1),
                               calculate(i, j - 1)), d)
        else:
            ca[i, j] = np.infty

        return ca[i, j]
    return calculate(m - 1, n - 1)




def GetLZPCausality(X, Y):
    """
    Utility function; uses ETC-Py to compute Compression Complexity Measure (CCM) Causality between :param X and Y
    :param X: array_like: time-series sequence
    :param Y: array_like: time-series sequence
    :return: returns 1 if X -> Y, otherwise returns 0
    """
    return 1 if ETC.CCM_causality(X, Y)['LZP_cause'] == 'x' else 0

def _euclideanDistance(A, B):
    """
    Computes the Euclidean Distance between two points represented in an n-dimensional space
    :param A: array_like: Let A = (a_1, a_2, ..., a_n)
    :param B: array_like: Let B = (b_1, b_2, ..., b_n)
    :return: returns th Euclidean distance = sqrt((b_1 - a_1)**2 + (b_2 - a_2)**2 + ... + (b_n - a_n)**2)
    """
    if len(A) != len(B):
        raise ValueError("A and B must have the same number of dimensions")
    sqr_dist = 0
    for i in range(len(A)):
        sqr_dist += (A[i] - B[i])**2
    return np.sqrt(sqr_dist)

#### TODO: Try to formulate a more efficient way to to this. This function acts like a dirty hack
def GetDistanceMeasures(arrs, rest_pruner=None, adder=36):
    """
    Returns a Tuple of all the distances between pairs of elements in different arrays
    :param arrs: The required arrays
    :param rest_pruner: For some distance metrics (like @dtwDist()), it makes sense to prune off the 99999's of rests
    :param adder: In case of melodies being passed in :param arrs, the default value transposes them by three octaves
            (assuming they were parsed in a twelve tonal-scale), or 36 semitones.
    :return: Tuple -> (LCS, ED, Normalised ED, DTW, HD, ETC)
    """
    LCSMatrix = np.zeros((len(arrs), len(arrs)))
    EDMatrix = np.zeros((len(arrs), len(arrs)))
    EDNormMatrix = np.zeros((len(arrs), len(arrs)))
    DTWMatrix = np.zeros((len(arrs), len(arrs)))
    HDMatrix = np.zeros((len(arrs), len(arrs)))
    dETCMatrix = np.zeros((len(arrs), len(arrs)))
    Causility_Matrix = np.zeros((len(arrs), len(arrs)))
    Causility_Matrix_LZ = np.zeros((len(arrs), len(arrs)))
    Causility_Matrix_ETCP = np.zeros((len(arrs), len(arrs)))

    for i in range(len(arrs)):
        m_i = arrs[i]
        if not rest_pruner == None:
            m_i_no_rests = rest_pruner(m_i)
        else:
            m_i_no_rests = m_i
        m_i = [x + adder for x in m_i]

        for ii in range(len(arrs)):
            m_ii = arrs[ii]
            if not rest_pruner == None:
                m_ii_no_rests = rest_pruner(m_ii)
            else:
                m_ii_no_rests = m_ii
            m_ii = [x + adder for x in m_ii]
            LCSMatrix[i][ii] = LCSubSeq(m_i, m_ii, len(m_i), len(m_ii))
            EDMatrix[i][ii] = editDist(m_i, m_ii, len(m_i), len(m_ii), normalize_len=True)
            DTWMatrix[i][ii] = dtwDist(m_i_no_rests, m_ii_no_rests, len(m_i_no_rests), len(m_ii_no_rests))
            HDMatrix[i][ii] = hammingDist(m_i, m_ii, len(m_i), len(m_ii))
            dETCMatrix[i][ii] = etcDist(m_i, m_ii)
            # Causility_Matrix[i][ii] =  1 if ETC.CCM_causality(m_i_no_rests, m_ii_no_rests)['ETCE_cause'] == 'x' else 0
            # Causility_Matrix_LZ[i][ii] =  1 if ETC.CCM_causality(m_i_no_rests, m_ii_no_rests)['LZP_cause'] == 'x' else 0
            # Causility_Matrix_ETCP[i][ii] =  1 if ETC.CCM_causality(m_i_no_rests, m_ii_no_rests)['ETCP_cause'] == 'x' else 0

    for i in range(len(arrs)):
        EDNormMatrix[i] = EDMatrix[i] / LCSMatrix[i][i]


    return LCSMatrix, EDMatrix, EDNormMatrix, DTWMatrix, HDMatrix, dETCMatrix#, Causility_Matrix, Causility_Matrix_LZ, Causility_Matrix_ETCP

# Deprecated
def GetCausalityMetrics(adjusted_melodies, *args):
    raise DeprecationWarning("This function is deprecated. Look at 'raga_surrogate_causality.ipynb' for a "
                             "better alternative")
    # ETCE = np.zeros((len(adjusted_melodies), len(adjusted_melodies)))  if 'ETCE' in args else None
    #
    # ETCP = np.zeros((len(adjusted_melodies), len(adjusted_melodies))) if 'ETCP' in args else None
    # LZP = np.zeros((len(adjusted_melodies), len(adjusted_melodies)))
    #
    # for i in range(len(adjusted_melodies)):
    #     for j in range(len(adjusted_melodies)):
    #         if ETCE is not None:
    #             ETCE[i][j] = 1 if ETC.CCM_causality(adjusted_melodies[i], adjusted_melodies[j])['ETCE_cause'] == 'x' else 0
    #         if ETCP is not None:
    #             ETCP[i][j] = 1 if ETC.CCM_causality(adjusted_melodies[i], adjusted_melodies[j])['ETCP_cause'] == 'x' else 0
    #         LZP[i][j] = 1 if ETC.CCM_causality(adjusted_melodies[i], adjusted_melodies[j])['LZP_cause'] == 'x' else 0
    #
    # return  LZP, ETCE, ETCP

import data
if __name__ == '__main__':
    X = data.PruneRestsMultiAxis(data.GetSongCoords2d(data.PAHI_RAMACHANDRA), note_axis=1)
    Y = data.PruneRestsMultiAxis(data.GetSongCoords2d(data.SYAMALE_MEENAKSHI), note_axis=1)
    Z = data.PruneRestsMultiAxis(data.GetSongCoords2d(data.MOZART_THEME), note_axis=1)
    W = data.PruneRestsMultiAxis(data.GetSongCoords2d(data.MOZART_VARIATION5), note_axis=1)
    V = data.PruneRestsMultiAxis(data.GetSongCoords2d(data.AH_VOUS_ORIGINAL), note_axis=1)
    print("DTW Distance between Pahi and Syamale: {}".format(dtwEuclidean(X, Y)))
    print("DTW Distance between Pahi and Mozart: {}".format(dtwEuclidean(X, Z)))
    print("DTW Distance between Syamale and Mozart: {}".format(dtwEuclidean(Y, Z)))
    print("DTW Distance between Syamale and Ah Vous: {}".format(dtwEuclidean(Y, V)))
    print("DTW Distance between Pahi and Ah Vous: {}".format(dtwEuclidean(X, V)))
    print("Frechet Distance between Pahi and Syamale: {}".format(frechetEuclidean(X, Y)))
    print("Frechet Distance between Pahi and Mozart: {}".format(frechetEuclidean(X, Z)))
    print("Frechet Distance between Pahi and Ah Vous: {}".format(frechetEuclidean(X, V)))
    print("Frechet Distance between Syamale and Mozart: {}".format(frechetEuclidean(Y, Z)))
    print("Frechet Distance between Syamale and Ah Vous: {}".format(frechetEuclidean(Y, V)))
    print("Frechet Distance between Pahi and Mozart5: {}".format(frechetEuclidean(X, W)))
    print("Frechet Distance between Syamale and Mozart5: {}".format(frechetEuclidean(Y, W)))
    print("Frechet Distance between MOZART and Mozart5: {}".format(frechetEuclidean(Z, W)))
    print("Frechet Distance between MOZART and Ah vous: {}".format(frechetEuclidean(Z, V)))

    X = data.xtractAxes(X)
    Y = data.xtractAxes(Y)
    X[0] = X[0][0:len(Y[0])]
    X[1] = X[1][0:len(Y[1])]
    # print(similaritymeasures.frechet_dist(X, Y))
