import numpy as np
import pandas as pd
from scipy.stats import f, t, ttest_ind
from vibork import *

# Параметры для первой выборки
mean1, std1, size1 = 0, 1, 15
# Параметры для второй выборки
mean2, std2, size2 = 5, 2, 10

# Генерация данных для первой выборки
data1, sample_mean1, sample_std1 = vibork(mean1, std1, size1)
# Генерация данных для второй выборки
data2, sample_mean2, sample_std2 = vibork(mean2, std2, size2)

# Вычисление F-статистики для теста на равенство дисперсий
f_statistic = (sample_std1 ** 2) / (sample_std2 ** 2)
# Критическое значение F-статистики
f_critical_value = f.ppf(1 - 0.05, size1 - 1, size2 - 1)

if f_statistic < f_critical_value:
    # Если дисперсии равны, выполняем t-тест
    t_statistic, p_value = ttest_ind(data1, data2)
    # Критическое значение t-статистики
    t_critical_value = t.ppf(1 - 0.05, size1 + size2 - 2)

    if t_statistic > t_critical_value:
        print('Отвергаем нулевую гипотезу: средние значения выборок не равны.')
    else:
        print('Не можем отвергнуть нулевую гипотезу: средние значения выборок равны.')
else:
    # Если дисперсии не равны, выполняем t-тест для независимых выборок с разными дисперсиями
    t_statistic, p_value = ttest_ind(data1, data2, equal_var=False)
    # Критическое значение t-статистики
    t_critical_value = t.ppf(1 - 0.05, min(size1, size2) - 1)

    if t_statistic > t_critical_value:
        print('Отвергаем нулевую гипотезу: средние значения выборок не равны.')
    else:
        print('Не можем отвергнуть нулевую гипотезу: средние значения выборок равны.')
