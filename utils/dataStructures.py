import numpy as np

def PackTuples(*args):
    l = len(args[0])
    for a in args:
        assert len(a) == l, "Length of all the argument arrays in not equal"

    if len(args) == 1 and isinstance(tuple, args[0][0]):
        return args[0]

    retList = []
    for i in range(l):
        loc = []
        for a in args:
            loc.append(a[i])
        fin = tuple(loc)
        retList.append(fin)
    return retList

def UnpackTuples(arr):
    l = [[] for _ in range(len(arr[0]))]
    for e in arr:
        for i in range(len(e)):
            l[i].append(e[i])

    return l


class EventList:
    def __init__(self, arr):
        self.shape = arr.shape if isinstance(arr, np.ndarray) else []
        if len(self.shape) == 0:
            val = self.shapeRecursor(arr)
            self.shape.reverse()
        self.dims = len(arr.shape) if isinstance(arr, np.ndarray) else len(self.shape)

        if isinstance(arr, np.ndarray):
            self.mainArray = arr
        else:
            self.mainArray = np.array(arr) if self.dims < 2 else np.array([np.array(a) for a in arr])
        self.classes = self._findclasses()
        self.classFreqSum = []
        self.classFreq = self._getClassFreq()

    def _findclasses(self):
        classes = []
        if self.dims > 1:
            for i in range(self.shape[0]):
                classes.append(np.unique(self.mainArray[i]))
        else:
            classes = np.unique(self.mainArray)

        return classes

    def _getClassFreq(self):
        freqs = []
        if self.dims > 1:
            for i in range(self.shape[0]):
                class_freqs = np.zeros_like(self.classes[i])
                for j in range(len(self.classes[i])):
                    for e in self.mainArray[i]:
                        if e == self.classes[i][j]:
                            class_freqs[j] += 1
                freqs.append(class_freqs)
                self.classFreqSum.append(np.sum(class_freqs))

        else:
            class_freqs = np.zeros_like(self.classes)
            for j in range(len(self.classes)):
                for e in self.mainArray:
                    if e == self.classes[j]:
                        class_freqs[j] += 1
            freqs = class_freqs
            self.classFreqSum.append(np.sum(class_freqs))

        return  freqs

    def shapeRecursor(self, arr):
        if isinstance(arr, np.ndarray) or  isinstance(arr, list) or isinstance(arr, tuple):
            self.shapeRecursor(arr[0])
            self.shape.append(len(arr))
            return len(arr)
        else: return -1

    def Add(self, *args):

        arr = self.mainArray
        for l in args:
            assert isinstance(l, EventList)
            arr = np.append(arr, l.mainArray, axis=1)
            # print(arr.shape)
        return EventList(arr)

class NoteEventList():
    def __init__(self, arr):
        note, dur = arr[0]
        self.List = arr
        self.classes = []
        self.classFreqs = []
        self._findClasses()

    def _findClasses(self):
        for e in self.List:
            if e not in self.classes:
                self.classes.append(e)
                self.classFreqs.append(1)
            else:
                ind = self.classes.index(e)
                self.classFreqs[ind] += 1
    def Add(self, *args):

        arr = self.List
        for l in args:
            assert isinstance(l, NoteEventList)
            arr += l.List
            # print(arr.shape)
        return NoteEventList(arr)

    def __len__(self):
        return len(self.List)


class NGramHolder:
    def __init__(self, alphabet, n):
        self.nrows = int(pow(len(alphabet), n))
        self.ncols = len(alphabet)
        self.N = n
        self.keys = [] if n > 1 else alphabet
        self.currents = list(alphabet)
        self.table = np.zeros((self.nrows, self.ncols), dtype='int64')
        self.totalPossibleTransitions = 0
        self.marginalProbs = []

    def AddOrUpdate(self, key, value):
        if key not in self.keys:
            self.keys.append(key)
        if value not in self.currents:
            raise ValueError("value not in alphabet. Please check!")

        # print("len keys: {}, len rows: {}".format(len(self.keys), self.nrows))
        assert len(self.keys) <= self.nrows

        i = list(self.keys).index(key)
        j = self.currents.index(value)
        self.table[i, j] += 1

    def CalculateFreq(self, array):
        for i in range(len(array) - self.N):
            key = array[i : i + self.N]
            if len(key) == 1:
                key = key[0]
            value = array[(i + self.N) % len(array)]
            self.AddOrUpdate(key, value)
        self.totalPossibleTransitions = len(array) - self.N

    def GetProbMatrix(self):
        assert len(self.keys) > 0
        matrix = self.table
        matrix = matrix.astype('float64')
        matrix /= self.totalPossibleTransitions

        sum = np.zeros(len(matrix))
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                sum[i] += matrix[i, j]
        self.marginalProbs = sum
        # print(sum)
        # print(sum.sum())
        return matrix

    def Generate(self, start=None, n_eles=1000):
        if start is None:
            ind = np.random.choice(np.arange(len(self.keys)))
            start = self.keys[ind]
        if self.N != 1:
            retVal = [*start]
        else:
            retVal = [start]
            start = [start]
        accepted = 0
        # new_probs_cum = np.zeros_like(new_probs)
        # for i in range(len(new_probs_cum)):
        #     if i == 0:
        #         new_probs_cum[i] = new_probs[i]
        #     else:
        #         new_probs_cum[i] = new_probs[i] + new_probs_cum[i - 1]
        # print(new_probs)
        iters = 0
        normal = lambda x, mu, sigma: (1 / sigma * np.sqrt(2 * np.pi)) * np.exp((-1 / 2) * ((x - mu) / sigma)**2)
        while len(retVal) < n_eles:
            sigma = 4
            candidate_ind = int(np.floor(np.random.normal(self.keys.index(start), sigma)))
            if candidate_ind >= len(self.currents) or candidate_ind < 0:
                continue
            prob = np.random.uniform(0, 1)
            i = self.keys.index(start)
            new_probs = self.table[i]
            new_probs = new_probs.astype('float64') / new_probs.sum()
            print("Current Selected Symbol: {}, Probability of Transition: {}".format(self.currents[candidate_ind], new_probs[candidate_ind]))
            if new_probs[candidate_ind] >= prob:
                retVal.append(int(self.currents[candidate_ind]))
                start.append(int(self.currents[candidate_ind]))
                start.pop(0)
                accepted += 1
            iters += 1
        # print(retVal[700:720])
        print("Acceptance rate: {}".format(accepted/iters * 100))


