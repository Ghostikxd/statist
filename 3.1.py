import numpy as np
import pandas as pd
from scipy.stats import f, t, ttest_ind
from vibork import *

mo1, s1, n1 = 0, 1, 15
mo2, s2, n2 = 5, 2, 10

Sample1, mean1, std1 = vibork(mo1, s1, n1)
Sample2, mean2, std2 = vibork(mo2, s2, n2)
f_stat = (std1 ** 2)/(std2**2)
f_critical = f.ppf(1-0.05, n1-1, n2-1)
if f_stat < f_critical:
    # Если дисперсии равны, выполняем t-тест
    t_stat, p_value = ttest_ind(Sample1, Sample2)
    t_critical = t.ppf(1-0.05, n1+n2-2)
    if t_stat > t_critical:
        print('Отвергаем нулевую гипотезу: средние значения выборок не равны.')
    else:
        print('Не можем отвергнуть нулевую гипотезу: средние значения выборок равны.')
else:
    # Если дисперсии не равны, выполняем t-тест для независимых выборок с разными дисперсиями
    t_stat, p_value = ttest_ind(Sample1, Sample2, equal_var=False)
    t_critical = t.ppf(1-0.05, min(n1, n2)-1)
    if t_stat > t_critical:
        print('Отвергаем нулевую гипотезу: средние значения выборок не равны.')
    else:
        print('Не можем отвергнуть нулевую гипотезу: средние значения выборок равны.')
