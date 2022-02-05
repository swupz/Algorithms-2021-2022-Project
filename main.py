import importlib
from time import perf_counter
from private import proutils

# In this file change only the group_id
group_id = 0

def test_v1(gid, filename, stock="AAPL"):
    g = importlib.import_module('group{}.project'.format(gid))
    start = perf_counter()
    g.prepare(filename)
    end = perf_counter()
    print('Prepare: {}ms'.format(round(1000 * (end - start))))

    # query
    start = perf_counter()
    res_aapl = g.stock_stats(stock)
    end = perf_counter()
    print('Query: {}ms'.format(round(1000 * (end - start))))
    print(proutils.check_stats_solution(gid, stock, res_aapl[0], res_aapl[2], res_aapl[1]))
    importlib.reload(g)

test_v1(group_id, "data/small_dataset.txt", "AAPL")
test_v1(group_id, "data/small_dataset.txt", "TSLA")
test_v1(group_id, "data/small_dataset.txt", "FB")


