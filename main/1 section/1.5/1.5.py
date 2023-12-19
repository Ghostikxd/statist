import math
import re
from collections import Counter
from time import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.special as sc
from cum import *
from more_itertools import distinct_permutations as dp
from nctlimit_app import *
from nctlimit_exact import *
from numpy import linalg
from pandas.core.common import flatten
from prints import *
from scipy import stats
from scipy.optimize import minimize
from show_distr import *


def sample():
    # тут почему-то от руки задаем значения, хотя есть инпут-файл
    beta = [0.95, 0.99]
    p = [0.5, 0.7, 0.9, 0.95, 0.99, 0.995, 0.999]
    delta = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

    f = open('main\\1 section\\1.5\\Direct_Plan.out', 'w')
    f.write("P="+"           ")
    for i in range(len(p)):
        f.write(str(p[i])+"__")
    f.write("\n")
    for m in range(len(beta)):
        f.write("beta="+str(beta[m])+"\n")
        for k in range(len(delta)):
            f.write("delta=")
            f.write(str(delta[k])+":")
            for i in range(len(p)):
                for j in range(3, 4000):
                    n = j
                    df = n-1
                    zp = stats.norm.ppf(p[i])
                    nc = zp*np.sqrt(n)
                    t = (delta[k]+zp)*np.sqrt(n)
                    bet = stats.nct.cdf(t, df, nc)
                    if (bet >= beta[m]):
                        break
                f.write(str(n)+(5-len(str(n)))*"_")
            f.write("\n")

    f.close()


sample()
