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


def Plan_Disp():
    txt = "Inp/Plan_Disp.inp"
    finp = open(txt)
    st = finp.readline()
    beta = list(map(float, finp.readline().split()))
    st = finp.readline()
    kstart = int(finp.readline())
    st = finp.readline()
    kfinish = int(finp.readline())
    finp.close()

    kb = len(beta)
    txt = "Out/Plan_Disp.out"
    fout = open(txt, 'w')
    print("Sample size to evaluate the variance with beta=", file=fout)
    print(beta, file=fout)
    for i in range(kb):
        print("Beta=", beta[i], file=fout)
        bb1 = 1.-beta[i]
        bb2 = 1.+beta[i]
        for j in range(kstart, kfinish+1):
            b1 = stats.chi2.ppf(1-0.5*bb1, j)
            b2 = stats.chi2.ppf(1-0.5*bb2, j)
            delta = np.sqrt(b1/b2)-1.
            print("f=", j, ": delta=", delta, file=fout)
    fout.close()


Plan_Disp()
