import numpy as np
import pandas as pd
from scipy.stats import f
from vibork import *


mo1, s1, n1 = 0, 1, 15
mo2, s2, n2 = 5, 2, 10


Sample1, mean1, std1 = vibork(mo1, s1, n1)
Sample2, mean2, std2 = vibork(mo2, s2, n2)


results = pd.DataFrame({
    'Sample 1': Sample1, })
results2 = pd.DataFrame({
    'Sample 2': Sample2
})
results.to_csv('results.csv', index=False)
results2.to_csv('results2.csv', index=False)
df = pd.concat([results, results2], axis=1)
df.to_csv('sample.csv', index=False)
read = pd.read_csv('sample.csv')
std1 = read['Sample 1'].std()
std2 = read['Sample 2'].std()
n1 = 100
n2 = 120
f_stat = (std1 ** 2)/(std2**2)
f_critical = f.ppf(1-0.05, n1-1, n2-1)


print(f'F-статистика: {f_stat}')
print(f'Критическое значение: {f_critical}')
if f_stat > f_critical:
    print('Отвергаем нулевую гипотезу: дисперсии выборок не равны.')
else:
    print('Не можем отвергнуть нулевую гипотезу: дисперсии выборок равны.')
