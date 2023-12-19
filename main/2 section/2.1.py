import math
from collections import defaultdict
from math import sqrt

import numpy as np
from grubbs import *
from scipy import stats


def grubbs_test():
    # Чтение данных из файла
    finp = open("main\\2 section\\Grubbs.inp")
    finp.readline()  # Пропускаем первую строку (предположительно, заголовок)
    data = tuple(map(float, finp.readline().split(" ")))
    ss = finp.readline()
    alpha = float(finp.readline())
    finp.close()

    fout = open('main\\2 section\\Grubbs.out', 'w')

    # Сортировка данных
    data = sorted(data)
    n = len(data)
    # Рассчитываем критическое значение для теста Граббса
    t = stats.t.ppf(alpha / (n), n - 2)
    critical_value = (n-1)*(math.sqrt(t**2/(n*(n-2+t**2))))

    # Расчет среднего, стандартного отклонения и максимального значения
    mean = np.mean(data)
    std_dev = np.std(data, ddof=1)
    max_value = np.max(data)

    # Расчет тестовой статистики
    test_statistic = (max_value - mean) / std_dev
    # Проверка наличия выброса
    is_outlier = test_statistic > critical_value

    # Поиск индексов максимальных значений (может потребоваться определение max_test_indices)
    ualpha = max_test_indices(data, alpha)

    if is_outlier:
        print("Критикал = ", critical_value)
        print("Тест = ", test_statistic)
        print("Ready", ualpha)
        print("Выброс обнаружен.")
        fout.write("Выброс обнаружен.")
    else:
        print("Критикал = ", critical_value)
        print("Тест = ", test_statistic)
        print("Ready", ualpha)
        print("Выброс не обнаружен.")
        fout.write("Выброс не обнаружен.")

    fout.close()


# Вызов функции теста
grubbs_test()
