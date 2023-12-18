from scipy.stats import anderson
import numpy as np


def read_samples(file_path):
    with open(file_path, 'r') as f:
        samples = [list(map(float, line.strip().split()))
                   for line in f.readlines()]
    return samples


file_path = "Inp\\anderson.inp"


samples = read_samples(file_path)


results = [anderson(sample, dist='norm') for sample in samples]


result_path = "Out\\anderson.out"
with open(result_path, 'a+') as result_file:
    for i, result in enumerate(results):
        stat = result.statistic
        critical_values = result.critical_values
        significance_level = result.significance_level
        result_file.write(f"Статистика критерия для выборки {i+1}: {stat}\n")
        result_file.write(f"Критические значения: {critical_values}\n")
        result_file.write(f"Уровень значимости: {significance_level}\n")

        alpha = 0.05
        if stat > critical_values[2] and significance_level < alpha:
            result_file.write(
                f"Отвергаем нулевую гипотезу для выборки {i+1}: Распределение не нормальное.\n")
        else:
            result_file.write(
                f"Не отвергаем нулевую гипотезу для выборки {i+1}: Распределение нормальное.\n")


print(f"Результаты сохранены в файле: {result_path}")
