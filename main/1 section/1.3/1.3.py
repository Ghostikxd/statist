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


def MLS_Normal():
    finp = open("main\\1 section\\1.3\\MLS_Normal.inp")
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

    fout = open('main\\1 section\\1.3\\MLS_Normal.out', 'w')
    n = len(y)
    print("MO and Std by observed values", file=fout)

    b, db = mlsordern(n, y)
    a = b[0]
    s = b[1]

    print("a=", a, file=fout)
    print("s=", s, file=fout)
    print("Sample size n=", n, file=fout)
    prints("Sample:", y, fout)

    w = cum(n)
    print("Observed values sample size n=", len(w), file=fout)
    prints("Empirical probability:", w, fout)
    w = stats.norm.ppf(w)
    zp = stats.norm.ppf(p)
    delta = zp*np.sqrt(n)
    print("Tolerance probability=", beta, file=fout)
    f = n-1

    db = db*n
    print("D{b}=", db, file=fout)
    t1 = db[0][0]
    t2 = db[1][1]
    t12 = db[0][1]

    print("Tolerance probability=", beta, file=fout)
    tlow, tup = nctlimit_app(n, beta, zp, t1, t2, t12)

    # tlow,tup=nctlimit_exact(f,beta,delta)

    prints("Probability range:", p, fout)
    prints("Normal quantiles:", w, fout)
    prints("Upper non central t quantile", tup, fout)
    prints("Low non central t quantile", tlow, fout)
    xp = a+s*zp
    xpup = a+s*tup/np.sqrt(n)
    xplow = a+s*tlow/np.sqrt(n)
    prints("Upper tolerance limit", xpup, fout)
    prints("Quantile estimations", xp, fout)
    prints("Low tolerance limit", xplow, fout)
    fout.close()

    show_distr("Normal", True, True, y, w, xp, zp, xplow, zp, xpup, zp, grid_size=n,
               distr_name=r'$N({a=}$'+str(round(a, 4))+",${s=}$"+str(round(s, 4))+")")


def mls(x, y, v):
    db = np.linalg.inv((np.dot(np.dot(x.transpose(), v), x)))
    b = np.dot(np.dot(np.dot(db, x.transpose()), v), y)
    return (b, db)


def mlsordern(n, y):
    x = np.ones((n, 2))
    v = np.ones((n, n))
    for i in range(n):
        x[i][1] = ordern(i+1, n)
        for j in range(i, n):
            v[j][i] = covordern(i+1, j+1, n)
            v[i][j] = v[j][i]
    v = np.linalg.inv(v)
    b, db = mls(x, y, v)
    return (b, db)


def ordern(r, n):

    p = 1
    pr = r/(n+1)
    qr = 1 - pr
    xr = stats.norm.ppf(pr)
    dr = stats.norm.pdf(xr)
    xr1 = p / dr
    xr2 = xr * (p / dr) ** 2
    xr3 = (2 * xr ** 2 + 1) * (p / dr) ** 3
    xr4 = (6 * xr ** 3 + 7 * xr) * (p / dr) ** 4
    xr5 = (24 * xr ** 4 + 46 * xr ** 2 + 7) * (p / dr) ** 5
    xr6 = (120 * xr ** 5 + 326 * xr ** 3 + 127 * xr) * (p / dr) ** 6
    er = xr + pr * qr * xr2 / (2 * (n + 2)) + pr * qr * ((qr - pr) * xr3 / 3 + pr * qr * xr4 / 8) / (n + 2) ** 2 + pr * qr * (-(
        qr - pr) * xr3 / 3 + ((qr - pr) ** 2 - pr * qr) * xr4 / 4 + qr * pr * (qr - pr) * xr5 / 6 + (qr * pr) ** 2 * xr6 / 48) / (n + 2) ** 3
    return (er)


def covordern(r, s, n):
    p = 1
    pr = r/(n+1)
    qr = 1 - pr
    xr = stats.norm.ppf(pr)
    dr = stats.norm.pdf(xr)
    xr1 = p / dr
    xr2 = xr * (p / dr) ** 2
    xr3 = (2 * xr ** 2 + 1) * (p / dr) ** 3
    xr4 = (6 * xr ** 3 + 7 * xr) * (p / dr) ** 4
    xr5 = (24 * xr ** 4 + 46 * xr ** 2 + 7) * (p / dr) ** 5
    xr6 = (120 * xr ** 5 + 326 * xr ** 3 + 127 * xr) * (p / dr) ** 6
    ps = s/(n+1)
    qs = 1 - ps
    xs = stats.norm.ppf(ps)
    ds = stats.norm.pdf(xs)
    xs1 = p / ds
    xs2 = xs * (p / ds) ** 2
    xs3 = (2 * xs ** 2 + 1) * (p / ds) ** 3
    xs4 = (6 * xs ** 3 + 7 * xs) * (p / ds) ** 4
    xs5 = (24 * xs ** 4 + 46 * xs ** 2 + 7) * (p / ds) ** 5
    xs6 = (120 * xs ** 5 + 326 * xs ** 3 + 127 * xs) * (p / ds) ** 6
    z1 = (qr - pr) * xr2 * xs1 + (qs - ps) * xr1 * xs2 + pr * qr * \
        xr3 * xs1 / 2 + ps * qs * xr1 * xs3 / 2 + pr * qs * xr2 * xs2 / 2
    z1 = z1 * pr * qs / (n + 2) ** 2
    z2 = -(qr - pr) * xr2 * xs1 - (qs - ps) * xr1 * \
        xs2 + ((qr - pr) ** 2 - pr * qr) * xr3 * xs1
    z3 = ((qs - ps) ** 2 - ps * qs) * xr1 * xs3 + (1.5 * (qr - pr)
                                                   * (qs - ps) + 0.5 * ps * qr - 2 * pr * qs) * xr2 * xs2
    z4 = (5 / 6) * pr * qr * (qr - pr) * xr4 * xs1 + (5 / 6) * ps * qs * (qs - ps) * \
        xr1 * xs4 + (pr * qs * (qr - pr) + 0.5 *
                     pr * qr * (qs - ps)) * xr3 * xs2
    z5 = (pr * qs * (qs - ps) + 0.5 * ps * qs * (qr - pr)) * xr2 * xs3 + \
        (1 / 8) * (pr * qr) ** 2 * xr5 * xs1 + \
        (1 / 8) * (ps * qs) ** 2 * xr1 * xs5
    z6 = 0.25 * pr ** 2 * qr * qs * xr4 * xs2 + 0.25 * pr * ps * qs ** 2 * \
        xr2 * xs4 + (2 * (pr * qs) ** 2 + 3 * pr *
                     qr * ps * qs) * xr3 * xs3 / 12
    z7 = z2 + z3 + z4 + z5 + z6
    vrs = z1 + pr * qs * z7 / (n + 2) ** 3 + pr * qs * xr1 * xs1 / (n + 2)
    return (vrs)


MLS_Normal()


def MLS_Weibull():
    finp = open("main\\1 section\\1.3\\MLS_Weibull.inp")
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

    fout = open('Out\MLS_Weibull.out', 'w')
    n = len(y)

    logy = np.log(y)
    bw, db = mlsorderw(n, logy)
    db = db*n
    print("D{b}=", db, file=fout)

    wcum = cum(n)
    zwcum = np.log(np.log(1/(1-np.array(wcum))))
    zw = np.log(np.log(1/(1-np.array(p))))
    t1 = db[0][0]
    t2 = db[1][1]
    t12 = db[0][1]

    # ln(Xp)=a+zw*s - quantile
    a = bw[0]  # shift
    s = bw[1]  # scale

    # F(x)=1-exp[-(x/c)^b] #cdf
    # f(x)=dF(x)/dx=(b/c)*(x/c)^(b-1)*exp[-(x/c)^b]  #pdf

    b = 1/s
    c = np.exp(a)

    print("a and s by MLS", file=fout)
    print("a=", a, "s=", s, file=fout)

    print("b and c by MLS", file=fout)
    print("c=", c, "b=", b, file=fout)

    print("Sample size n=", n, file=fout)
    prints("Sample:", y, fout)
    prints("Sample log:", logy, fout)

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

    show_distr("Weibull", True, True, logy, zwcum, xp, zw, xplow, zw, xpup, zw,
               grid_size=n, distr_name=r'$N({a=}$'+str(round(a, 4))+",${s=}$"+str(round(s, 4))+")")


def mlsorderw(n, y):
    x = np.ones((n, 2))
    v = np.ones((n, n))
    for i in range(n):
        x[i][1] = orderw(i+1, n)
        for j in range(i, n):
            v[j][i] = covorderw(i+1, j+1, n)
            v[i][j] = v[j][i]
    v = np.linalg.inv(v)
    b, db = mls(x, y, v)
    return (b, db)


def covorderw(r, s, n):
    pr = r/(n+1)
    qr = 1 - pr
    xr = np.log(np.log(1 / (1 - pr)))
    xr1 = 1 / (np.log(1 / (1 - pr)) * (1 - pr))
    xr2 = xr1 * (1 / (1 - pr) - xr1)
    xr3 = xr2 ** 2 / xr1 + xr1 * (1 / (1 - pr) ** 2 - xr2)
    xr4 = (3 * xr1 * xr2 * xr3 - 2 * xr2 ** 3) / \
        xr1 ** 2 + xr1 * (2 / (1 - pr) ** 3 - xr3)
    xr55 = (-12 * xr1 * xr2 ** 2 * xr3 + 3 * xr1 ** 2 * xr3 **
            2 + 4 * xr1 ** 2 * xr2 * xr4 + 6 * xr2 ** 4)
    xr5 = xr55 / xr1 ** 3 + xr1 * (6 / (1 - pr) ** 4 - xr4)

    ps = s/(n+1)
    qs = 1-ps
    xs = np.log(np.log(1 / (1 - ps)))
    xs1 = 1 / (np.log(1 / (1 - ps)) * (1 - ps))
    xs2 = xs1 * (1 / (1 - ps) - xs1)
    xs3 = xs2 ** 2 / xs1 + xs1 * (1 / (1 - ps) ** 2 - xs2)
    xs4 = (3 * xs1 * xs2 * xs3 - 2 * xs2 ** 3) / \
        xs1 ** 2 + xs1 * (2 / (1 - ps) ** 3 - xs3)
    xs5 = (-12 * xs1 * xs2 ** 2 * xs3 + 3 * xs1 ** 2 * xs3 ** 2 + 4 * xs1 **
           2 * xs2 * xs4 + 6 * xs2 ** 4) / xs1 ** 3 + xs1 * (6 / (1 - ps) ** 4 - xs4)
    z1 = (qr - pr) * xr2 * xs1 + (qs - ps) * xr1 * xs2 + pr * qr * \
        xr3 * xs1 / 2 + ps * qs * xr1 * xs3 / 2 + pr * qs * xr2 * xs2 / 2
    z1 = z1 * pr * qs / (n + 2) ** 2
    z2 = -(qr - pr) * xr2 * xs1 - (qs - ps) * xr1 * \
        xs2 + ((qr - pr) ** 2 - pr * qr) * xr3 * xs1
    z3 = ((qs - ps) ** 2 - ps * qs) * xr1 * xs3 + (1.5 * (qr - pr)
                                                   * (qs - ps) + 0.5 * ps * qr - 2 * pr * qs) * xr2 * xs2
    z4 = (5 / 6) * pr * qr * (qr - pr) * xr4 * xs1 + (5 / 6) * ps * qs * (qs - ps) * \
        xr1 * xs4 + (pr * qs * (qr - pr) + 0.5 *
                     pr * qr * (qs - ps)) * xr3 * xs2
    z5 = (pr * qs * (qs - ps) + 0.5 * ps * qs * (qr - pr)) * xr2 * xs3 + \
        (1 / 8) * (pr * qr) ** 2 * xr5 * xs1 + \
        (1 / 8) * (ps * qs) ** 2 * xr1 * xs5
    z6 = 0.25 * pr ** 2 * qr * qs * xr4 * xs2 + 0.25 * pr * ps * qs ** 2 * \
        xr2 * xs4 + (2 * (pr * qs) ** 2 + 3 * pr *
                     qr * ps * qs) * xr3 * xs3 / 12
    z7 = z2 + z3 + z4 + z5 + z6
    vrs = z1 + pr * qs * z7 / (n + 2) ** 3 + pr * qs * xr1 * xs1 / (n + 2)
    return (vrs)


def orderw(r, n):
    pr = r/(n+1)
    qr = 1 - pr
    xr = np.log(np.log(1 / (1 - pr)))
    xr1 = 1 / (np.log(1 / (1 - pr)) * (1 - pr))
    xr2 = xr1 * (1 / (1 - pr) - xr1)
    xr3 = xr2 ** 2 / xr1 + xr1 * (1 / (1 - pr) ** 2 - xr2)
    xr4 = (3 * xr1 * xr2 * xr3 - 2 * xr2 ** 3) / \
        xr1 ** 2 + xr1 * (2 / (1 - pr) ** 3 - xr3)
    xr55 = (-12 * xr1 * xr2 ** 2 * xr3 + 3 * xr1 ** 2 * xr3 **
            2 + 4 * xr1 ** 2 * xr2 * xr4 + 6 * xr2 ** 4)
    xr5 = xr55 / xr1 ** 3 + xr1 * (6 / (1 - pr) ** 4 - xr4)
    a1 = -12 * xr2 ** 3 * xr3 - 12 * xr1 * \
        (2 * xr2 * xr3 ** 2 + xr2 ** 2 * xr4)
    b1 = 6 * xr1 * xr2 * xr3 ** 2 + 6 * xr1 ** 2 * xr3 * xr4
    c1 = 8 * xr1 * xr2 ** 2 * xr4 + 4 * xr1 ** 2 * (xr3 * xr4 + xr2 * xr5)
    d1 = 24 * xr2 ** 3 * xr3
    xr6 = (xr1 ** 3 * (a1 + b1 + c1 + d1) - 3 * xr1 ** 2 * xr2 * xr55) / \
        xr1 ** 6 + xr2 * (6 / (1 - pr) ** 4 - xr4) + \
        xr1 * (24 / (1 - pr) ** 5 - xr5)
    er = xr + pr * qr * xr2 / (2 * (n + 2)) + pr * qr * ((qr - pr) * xr3 / 3 + pr * qr * xr4 / 8) / (n + 2) ** 2 + pr * qr * (-(
        qr - pr) * xr3 / 3 + ((qr - pr) ** 2 - pr * qr) * xr4 / 4 + qr * pr * (qr - pr) * xr5 / 6 + (qr * pr) ** 2 * xr6 / 48) / (n + 2) ** 3
    return (er)


MLS_Weibull()
