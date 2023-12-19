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



def show_distr(tdistr,nbegin,nend,x,y,xp,yp,xplow,yplow,xpup,ypup,grid_size, distr_name):
    
    if tdistr=="Weibull":
        p=[0.01,0.025,0.05,0.1,0.2,0.3,0.5,0.7,0.9,0.95,0.995]
        zp=np.log(np.log(1./(1.-np.asarray(p))))
    if tdistr=="Normal":
        p=[0.005,0.01,0.025,0.05,0.1,0.2,0.3,0.5,0.7,0.8,0.9,0.95,0.975,0.99,0.995]
        zp=stats.norm.ppf(np.asarray(p),0,1)
    kp=len(p)
    ymin=zp[0]
    ymax=zp[kp-1]+0.5
    xmin=min(xplow)
    xmax=max(xpup)+0.5
   
    grid = np.linspace(xmin, xmax, grid_size) 
    #if nbegin==True:figure,axes=plt.subplots(figsize=(12, 10))
    if nbegin==True:figure,axes=plt.subplots()
    plt.plot(x,y,'r+',markersize=12,label=u'Выборка') 
    plt.plot(xp,yp,'black',lw=3,label=u'Distribution')
    plt.plot(xplow,yplow,'g-',lw=2,label=u'Xlow')
    plt.plot(xpup,ypup,'g-.',lw=2,label=u'Xup')
    
    for i in range(kp):
        xx=[xmin,xmax]
        yy=[zp[i],zp[i]] 
        plt.text (xmax,zp[i],str(100*p[i])+"%")
        plt.plot(xx,yy,'black',lw=1,label='',linestyle='dashed')
    plt.text(xmax,ymax,"P%")

    plt.grid(ls=':') 
    plt.xlabel(r'${X}$', fontsize=18) 
    plt.ylabel(r'${Zp}$', fontsize=18) 
    plt.xlim((xmin, xmax)) 
    plt.ylim((ymin, ymax)) 
    title = 'Distribution {}'.format(distr_name) 
    plt.title(title, fontsize=20) 
    
    if nbegin==True:axes.legend();
    if nbegin==True and nend==True:plt.show()
