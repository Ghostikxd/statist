import os

import numpy as np
import pandas as pd
from scipy.stats import f
from vibork import vibork


def generate_and_save_samples(parameters, filename, directory='main/3 section/3.2'):
    data, mean, std = vibork(*parameters)
    results = pd.DataFrame({filename: data})

    # Получаем текущую директорию
    current_directory = os.getcwd()

    # Собираем полный путь к файлу
    file_path = os.path.join(current_directory, directory, filename + '.csv')

    # Сохраняем CSV-файл
    results.to_csv(file_path, index=False)
    return results


def calculate_and_print_f_statistic(std1, std2, n1, n2):
    f_stat = (std1 ** 2) / (std2 ** 2)
    f_critical = f.ppf(1 - 0.05, n1 - 1, n2 - 1)
    print(f'F-статистика: {f_stat}')
    print(f'Критическое значение: {f_critical}')

    if f_stat > f_critical:
        print('Отвергаем нулевую гипотезу: дисперсии выборок не равны.')
    else:
        print('Не можем отвергнуть нулевую гипотезу: дисперсии выборок равны.')


# Параметры для первой выборки
mo1, s1, n1 = 0, 1, 15
# Параметры для второй выборки
mo2, s2, n2 = 5, 2, 10

# Генерация и сохранение данных для первой выборки
generate_and_save_samples((mo1, s1, n1), 'Sample 1')

# Генерация и сохранение данных для второй выборки
generate_and_save_samples((mo2, s2, n2), 'Sample 2')

# Чтение данных из сохраненных файлов
read1 = pd.read_csv(os.path.join('main/3 section/3.2', 'Sample 1.csv'))
read2 = pd.read_csv(os.path.join('main/3 section/3.2', 'Sample 2.csv'))

# Подсчет стандартных отклонений
std1 = read1['Sample 1'].std()
std2 = read2['Sample 2'].std()

# Новые размеры выборок
n1 = 100
n2 = 120

# Расчет F-статистики и вывод результатов
calculate_and_print_f_statistic(std1, std2, n1, n2)

# Конкатенация DataFrames
df = pd.concat([read1, read2], axis=1)

# Получаем текущую директорию
current_directory = os.getcwd()

# Собираем полный путь к файлу
file_path = os.path.join(current_directory, 'main/3 section/3.2/sample.csv')

# Сохраняем DataFrame в CSV-файл с указанием пути
df.to_csv(file_path, index=False)
