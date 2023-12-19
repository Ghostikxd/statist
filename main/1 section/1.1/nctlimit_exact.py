from scipy import stats
import numpy as np

def nctlimit_exact(f,beta,delta):
    tlow=stats.nct.ppf(1-beta,f,delta)
    tup=stats.nct.ppf(beta,f,delta)
    return(tlow,tup)