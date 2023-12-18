from show_distr import *
from prints import *
from nctlimit_exact import *
from scipy import stats
from cum import *
from scipy.optimize import minimize
from scipy import stats
import scipy.special as sc
from numpy import linalg
from more_itertools import distinct_permutations as dp
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
from collections import Counter
from pandas.core.common import flatten
from time import time
import math
from nctlimit_app import *


def sample():
    beta = [0.95, 0.99]
    p = [0.5, 0.7, 0.9, 0.95, 0.99, 0.995, 0.999]
    delta = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

    f = open('Out\Direct_Plan.out', 'w')
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
