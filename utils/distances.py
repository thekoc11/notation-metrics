import ETC
from scipy.spatial.distance import hamming

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

def editDist(X, Y, m, n):
    """
    Returns the edit distance between array-likes X and Y
    :param X: array-like
    :param Y: array-like
    :param m: length of X
    :param n: length of Y
    :return: (int) minimum number of edits required to make X = Y
    """
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

def etcDist(seq_x, seq_y):
    """
    Returns the ETC distance between the two sequences
    :param seq_x: array-like
    :param seq_y: array-like
    :return: (int) ETC distance between the sequences
    """
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