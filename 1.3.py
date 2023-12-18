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

def MLS_Normal():
    finp=open("Inp\MLS_Normal.inp")
    finp.readline()
    n=int(finp.readline())
    ss=finp.readline()
    beta=float(finp.readline())
    ss=finp.readline()
    y=tuple(map(float,finp.readline().split(" ")))
    ss=finp.readline()
    kp=int(finp.readline())
    ss=finp.readline()
    p=tuple(map(float,finp.readline().split(" ")))
    finp.close()

    fout=open('Out\MLS_Normal.out','w')
    n=len(y)
    print("MO and Std by observed values",file=fout)
 
    b,db=mlsordern(n,y)          
    a=b[0]
    s=b[1]

    print("a=",a,file=fout)
    print("s=",s,file=fout)
    print("Sample size n=",n,file=fout)
    prints("Sample:",y,fout)

    w=cum(n)
    print("Observed values sample size n=",len(w),file=fout)
    prints("Empirical probability:",w,fout)
    w=stats.norm.ppf(w)
    zp=stats.norm.ppf(p)
    delta=zp*np.sqrt(n)
    print("Tolerance probability=",beta,file=fout)
    f=n-1

    db=db*n
    print("D{b}=",db,file=fout)
    t1=db[0][0];t2=db[1][1];t12=db[0][1] 
 
    print("Tolerance probability=",beta,file=fout)
    tlow,tup=nctlimit_app(n,beta,zp,t1,t2,t12)   

    #tlow,tup=nctlimit_exact(f,beta,delta)

    prints("Probability range:",p,fout)
    prints("Normal quantiles:",w,fout)
    prints("Upper non central t quantile",tup,fout)
    prints("Low non central t quantile",tlow,fout)
    xp=a+s*zp
    xpup=a+s*tup/np.sqrt(n)
    xplow=a+s*tlow/np.sqrt(n)
    prints("Upper tolerance limit",xpup,fout)
    prints("Quantile estimations",xp,fout)
    prints("Low tolerance limit",xplow,fout)
    fout.close()

    show_distr("Normal",True,True,y,w,xp,zp,xplow,zp,xpup,zp,grid_size=n,distr_name=r'$N({a=}$'+str(round(a,4))+",${s=}$"+str(round(s,4))+")")

MLS_Normal()