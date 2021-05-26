import multiprocessing
import time

import ETC
import numpy as np
from itertools import product, combinations
import concurrent.futures
import threading

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

def TrueLZPCausality_listParallel(list, labels, mela):
    p = multiprocessing.Pool()
    res = p.starmap(ETC.CCM_causality, combinations(list, r=2))
    iter = 0
    dist = np.zeros((len(list), len(list)))
    true_causes = 0
    total_causes = 0
    strengths = [0]
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            cause = res[iter]['LZP_cause']
            strength = res[iter]['LZP_strength']
            mj1 = mela in labels[i] and mela not in labels[j]
            mj2 = mela in labels[j] and mela not in labels[i]
            if mj1 or mj2:
                total_causes += 1
            if (mj1 and cause == 'x') or (mj2 and cause == 'y'):
                true_causes += 1
                if strength > strengths[-1]:
                    strengths.append(strength)

            iter += 1
    if len(strengths) > int(total_causes / 10):
        strengths = strengths[-(total_causes // 10):]
    print("{} true causes out of {} total connections".format(true_causes, total_causes))
    return true_causes, total_causes, strengths

def PooledProcessRunner(target, args, n=24):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        pool = [executor.submit(target, *args) for _ in range(n)]
        for i in concurrent.futures.as_completed(pool):
            print("Return Value: {}".format(i.result()))

def UniformConcurrentExecutor(target, args, n_threads=24):
    """
    Runs the function :param target with :param args concurrently in :param n_threads threads

    :param args: should be a list of all the args needed by :param target. The first element should be a dummy value,
                    which will get replaced by the thread index it is running on. Should also contain a dictionary which will
                    collect the resultant values
    """
    threads = []
    for i in range(n_threads):
        args[0] = i
        t = threading.Thread(target=target, args=args)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

def sleepTest(thread_idx, nums, oper, ret_dict={}):
    num1 = np.random.choice(nums)
    num2 = np.random.choice(nums)
    end = 0
    if oper == '+':
        end = num2 + num1
    elif oper == '*':
        end = num2 * num1

    if end < 0 and oper == '+':
        end = num2 * num1

    print("Thread {} Sleeping for {} seconds".format(thread_idx, end))
    time.sleep(end)
    print("Done Sleeping")
    ret_dict[thread_idx] = end


if __name__ == '__main__':
    # PooledProcessRunner(sleepTest, ([-1, -2, 3, 5, 7, 6, 4, 8], "+"))
    # n_eles = 8
    # n_processes = len(list(combinations(np.arange(n_eles), 2)))
    # l = []
    # for i in range(n_eles):
    #     for j in range(i, n_eles):
    #         if i != j:
    #             print(i, j)
    #             l.append((i//n_eles, i % n_eles))
    # print(n_processes, len(l))
    # print(multiprocessing.cpu_count())
    # lists = []
    # process_lists = []
    d = {}
    UniformConcurrentExecutor(sleepTest, [0, [-1, -2, 3, 5, 7, 4, 6, 8], "+", d])
    #
    # for i in range(24):
    #     n = np.random.randint(0, 26, 4)
    #     lists.append(n)
    # q = multiprocessing.Queue()
    #
    # for i in range(50):
    #     p = threading.Thread(target=sleepTest, args=(i, [-1, -2, 3, 5, 7, 6, 4, 8], "+", d))
    #     process_lists.append(p)
    #
    # p3 = multiprocessing.Process(target=print_queue, args=(q, ))
    #
    # for p in process_lists:
    #     p.start()
    #
    # for p in process_lists:
    #     p.join()

    print(d)
    #
    # p3.start()
    # p3.join()


