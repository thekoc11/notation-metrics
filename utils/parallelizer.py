import multiprocessing
import numpy as np
from itertools import product, combinations


def list_parallelizer(target, list):
    n_thrs = len(list) * len(list)
    pairs = []
    for i in range(n_thrs):
        pairs.append((list[i//len(list)], list[i % len(list)]))

    p = multiprocessing.Pool()
    res = p.starmap(target, product(list, repeat=2))

    dist = np.zeros((len(list), len(list)))
    for i in range(len(list)):
        for j in range(len(list)):
            dist[i, j] = res[i * len(list) + j]
    return dist


if __name__ == '__main__':
    n_eles = 8
    n_processes = len(list(combinations(np.arange(n_eles), 2)))
    l = []
    for i in range(n_eles):
        for j in range(i, n_eles):
            if i != j:
                print(i, j)
                l.append((i//n_eles, i % n_eles))
    # l = list(product(np.arange(n_eles), repeat=2))
    print(n_processes, len(l))
    print(multiprocessing.cpu_count())
    # lists = []
    # process_lists = []
    #
    # for i in range(24):
    #     n = np.random.randint(0, 26, 4)
    #     lists.append(n)
    # q = multiprocessing.Queue()
    #
    # for i in range(24):
    #     p = multiprocessing.Process(target=square_list, args=(lists[i], i, q))
    #     process_lists.append(p)
    #
    # p3 = multiprocessing.Process(target=print_queue, args=(q, ))
    #
    # for p in process_lists:
    #     p.start()
    #
    # for p in process_lists:
    #     p.join()
    #
    #
    # p3.start()
    # p3.join()


