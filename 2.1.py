import math
from math import sqrt
from collections import defaultdict
from scipy import stats
import numpy as np
from grubbs import *


def grubbs_test():
    finp = open("Inp\Grubbs.inp")
    finp.readline()
    data = tuple(map(float, finp.readline().split(" ")))
    ss = finp.readline()
    alpha = float(finp.readline())
    finp.close()
    fout = open('Out\Grubbs.out', 'w')

    data = sorted(data)
    n = len(data)
    t = stats.t.ppf(alpha / (n), n - 2)
    critical_value = (n-1)*(math.sqrt(t**2/(n*(n-2+t**2))))

    mean = np.mean(data)
    std_dev = np.std(data, ddof=1)
    max_value = np.max(data)

    test_statistic = (max_value - mean) / std_dev
    is_outlier = test_statistic > critical_value

    ualpha = max_test_indices(data, alpha)

    if is_outlier:
        print("Критикал = ", critical_value)
        print("Тест = ", test_statistic)
        print("Ready", ualpha)
        print("Выброс обнаружен.")
        fout.write("Выброс обнаружен.")
    else:
        print("Критикал = ", critical_value)
        print("Тест = ", test_statistic)
        print("Ready", ualpha)
        print("Выброс не обнаружен.")
        fout.write("Выброс не обнаружен.")

    fout.close()


grubbs_test()
