from est_simple import *
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

#MLE_Normal()
#MLE_Weibull()
#MLS_Normal()
#MLS_Weibull()
#sample()
#Plan_Disp()

xlow=-5
xup=5
step=0.01
n=int((xup-xlow)/step)
x=[0 for i in range(n)]
y=[0 for i in range(n)]
for i in range (n):
  x[i]=xlow+i*step
  y[i]=stats.norm.cdf(x[i],0,1)
plt.plot(x,y)
plt.grid()
plt.show()

xlow=-5
xup=5
step=0.01
n=int((xup-xlow)/step)
x=[0 for i in range(n)]
y=[0 for i in range(n)]
for i in range (n):
  x[i]=xlow+i*step
  y[i]=stats.norm.pdf(x[i],0,2)
plt.plot(x,y)
plt.grid()
xlow=-5
xup=5
step=0.01
n=int((xup-xlow)/step)
x=[0 for i in range(n)]
y=[0 for i in range(n)]
for i in range (n):
  x[i]=xlow+i*step
  y[i]=stats.norm.pdf(x[i],0,1)
plt.plot(x,y)

xlow=-5
xup=5
step=0.01
n=int((xup-xlow)/step)
x=[0 for i in range(n)]
y=[0 for i in range(n)]
for i in range (n):
  x[i]=xlow+i*step
  y[i]=stats.norm.pdf(x[i],1,1)
plt.plot(x,y)
plt.show()