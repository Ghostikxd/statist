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

def nctlimit_app(n,beta,zp,t1,t2,t12):
    zb=stats.norm.ppf(beta)
    d=zp*np.sqrt(n)
    f1x=t2/(n-1)
    f2x=2*t12/np.sqrt(n)
    f4x=1-f1x/2
    e3x=f4x**2-zb**2*f1x
    e11=f4x*d+zb**2*f2x/2
    e2x=d**2-zb**2*t1
    e44=np.sqrt(abs(e11**2-e2x*e3x))
    tlow=(e11-e44)/e3x
    tup=(e11+e44)/e3x
    return(tlow,tup)

