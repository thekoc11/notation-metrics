import multiprocessing
import numpy as np
from itertools import product

result  = []

def square_list(my_list, idx, q):
    new_list = []
    for num in my_list:
        new_list.append(num * num)
    q.put((idx, new_list))

def print_queue(q):
    print("Queue elements:")
    while not q.empty():
        print(q.get())
    print("Queue is now empty!")

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
    n_processes = n_eles * n_eles#len(list(combinations(np.arange(n_eles), 2)))
    # for i in range(n_processes):
    #     print(i//n_eles, i % n_eles)
    print(list(product(np.arange(n_eles), repeat=2)))
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


