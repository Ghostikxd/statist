import numpy as np
import pandas as pd
from scipy.stats import f


def vibork(mo, s0, n0):
    rng = np.random.default_rng()
    z = (rng.standard_normal(n0)) * s0 + mo
    disp_mean = np.mean(z)
    disp_std = np.sqrt((n0/(n0-1.))) * np.std(z)
    return z, disp_mean, disp_std
