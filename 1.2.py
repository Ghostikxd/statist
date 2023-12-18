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


def MLE_Weibull():

    finp = open("Inp\MLE_Weibull.inp")
    finp.readline()
    n = int(finp.readline())
    ss = finp.readline()
    beta = float(finp.readline())
    ss = finp.readline()
    y = tuple(map(float, finp.readline().split(" ")))
    ss = finp.readline()
    kp = int(finp.readline())
    ss = finp.readline()
    p = tuple(map(float, finp.readline().split(" ")))
    finp.close()

    fout = open('Out\MLE_Weibull.out', 'w')
    n = len(y)
    b = 0.5
    c = 1.5
    bnds = ((0, None), (0, None))

    res = minimize(WeibullMinFunction, (b, c), args=(
        y, n), method='Nelder-Mead', bounds=bnds, tol=1e-12, options={'disp': True})

    b = res.x[0]
    c = (sum(y**b))/n
    a = (np.log(c))/b
    s = 1/b
    print("b and c by MLE", file=fout)
    print("a=", a, "s=", s, file=fout)
    print("FunMin="+str(WeibullMinFunction(res.x, y, n)), file=fout)
    print("Sample size n=", n, file=fout)
    prints("Sample:", y, fout)

    y = np.log(y)
    wcum = cum(n)
    zwcum = np.log(np.log(1/(1-np.array(wcum))))
    zw = np.log(np.log(1/(1-np.array(p))))
    v = CovMatrixMleW(n, (y-a)/s)
    t1 = v[0][0]
    t2 = v[1][1]
    t12 = v[0][1]

    print("Observed values sample size n=", n, file=fout)
    prints("Empiricalr probability:", wcum, fout)
    print("Tolerance probability=", beta, file=fout)

    tlow, tup = nctlimit_app(n, beta, zw, t1, t2, t12)

    prints("Probability range:", p, fout)
    prints("Weibull quantiles:", zw, fout)
    prints("Upper non central t quantile", tup, fout)
    prints("Low non central t quantile", tlow, fout)
    xp = a+zw*s
    xpup = a+s*tup/np.sqrt(n)
    xplow = a+s*tlow/np.sqrt(n)
    prints("Upper tolerance limit", xpup, fout)
    prints("Quantile estimations", xp, fout)
    prints("Low tolerance limit", xplow, fout)
    fout.close()

    show_distr("Weibull", True, True, y, zwcum, xp, zw, xplow, zw, xpup, zw, grid_size=n,
               distr_name=r'$N({a=}$'+str(round(a, 4))+",${s=}$"+str(round(s, 4))+")")


def WeibullMinFunction(x, y, n):
    b = x[0]
    z = y**b
    c = sum(z)/n
    s2 = sum(z*np.log(z))
    s1 = sum(np.log(z))
    c1 = n+s1-s2/c
    return (c1**2)


def CovMatrixMleW(n, z):
    v = np.zeros((2, 2))
    v[0][0] = 1.
    v[0][1] = 1.+sum(z)/n
    v[1][0] = v[0][1]
    v[1][1] = 1.+sum(z**2*np.exp(z))/n
    v = linalg.inv(v)
    return (v)


MLE_Weibull()
