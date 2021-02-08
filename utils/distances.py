import ETC
from scipy.spatial.distance import hamming
import numpy as np

def LCSubSeq(X, Y, m, n):
    """
    Longest Common Subsequence
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
    dtw = np.zeros((m + 1, n + 1), dtype='int64')
    C = []
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


def dtwEuclidean(X, Y, m, n):
    if len(X[0]) != 3 or len(Y[0])  != 3:
        raise ValueError("Threee dimensional data expected. One or both of X and Y are not three dimensional")
    dtw = np.zeros((m + 1, n + 1), dtype='int64')
    C = []
    for i in range(m + 1):
        for j in range(n + 1):
            dtw[i, j] = 99999
    dtw[0, 0] = 0

    for i in range(1, m+1):
        for j in range(1, n + 1):
            cost = _euclideanDistance(X[i-1][0], X[i-1][1], X[i-1][2], Y[j-1][0], Y[j-1][1], Y[j-1][2]) #0 if X[i - 1] == Y[j - 1] else 1
            last_min = np.min([dtw[i, j-1], dtw[i - 1, j], dtw[i-1, j-1]])
            dtw[i, j] = cost  + last_min
    # print(dtw)
    return dtw[m, n]

def _euclideanDistance(note1, dur1, meas1, note2, dur2, meas2):
    return np.sqrt((note2 - note1)**2 + (dur2 - dur1)**2 + (meas2-meas1)**2)


def GetDistanceMeasures(arrs, rest_pruner=None, adder=36):
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


    return LCSMatrix, EDMatrix, EDNormMatrix, DTWMatrix, HDMatrix, dETCMatrix, Causility_Matrix, Causility_Matrix_LZ, Causility_Matrix_ETCP


if __name__ == '__main__':
    X = ETC.generate(size=5, partitions=2)
    Y = ETC.generate(size=8, partitions=2)
    print(dtwDist(X, Y, 5, 8))
