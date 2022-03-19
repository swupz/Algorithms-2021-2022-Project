import importlib
from time import perf_counter
from private import proutils
import sys, os
from cachetools import cached, TTLCache

#implementation of caching
cache = TTLCache(maxsize=50, ttl=5000)

# put here your group id
your_group = 16

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

#-------------------------------------------# Proj v1 #-------------------------------------------#
@cached(cache)
def test_v1(gid, filename, stock="AAPL", num_queries=1):
    g = importlib.import_module('group{}.project'.format(gid))
    start = perf_counter()
    g.prepare(filename)
    end = perf_counter()
    prep_time = round(1000 * (end - start))

    # query
    start = perf_counter()
    for i in range(num_queries):
        g.stock_stats(stock)
    end = perf_counter()
    run_time = round(1000 * (end - start))
    importlib.reload(g)
    return prep_time, run_time

def test_perf_project_v1(gid=0, num_prepare=20, num_queries=1000):
    blockPrint()
    prep_time, run_time = 0, 0
    for i in range(num_prepare):
        tmp_prep_time, tmp_run_time = test_v1(gid, "data/small_dataset.txt", "AAPL", num_queries)
        run_time += tmp_run_time
        prep_time += tmp_prep_time
        tmp_prep_time, tmp_run_time = test_v1(gid, "data/small_dataset.txt", "TSLA", num_queries)
        run_time += tmp_run_time
        prep_time += tmp_prep_time
        tmp_prep_time, tmp_run_time = test_v1(gid, "data/small_dataset.txt", "FB", num_queries)
        run_time += tmp_run_time
        prep_time += tmp_prep_time

    enablePrint()
    print('Loading and Building data - Time: {}ms'.format(prep_time))
    print('Query - Time: {}ms'.format(run_time))

if __name__ == "__main__":
    num_prepare, num_queries = 50, 5000
    test_perf_project_v1(gid=your_group, num_prepare=num_prepare, num_queries=num_queries)
