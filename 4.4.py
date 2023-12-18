from scipy.stats import chi2_contingency
import numpy as np


def read_data(file_path):
    with open(file_path, 'r') as f:
        data = [list(map(int, line.strip().split())) for line in f.readlines()]
    return np.array(data)


file_path = "Inp\\chi_square.inp"


observed_data = read_data(file_path)


chi2_stat, p_value, _, _ = chi2_contingency(observed_data)


result_path = "Out\\chi_square.out"


with open(result_path, 'w') as result_file:
    result_file.write(f"Статистика критерия хи-квадрат: {chi2_stat}\n")
    result_file.write(f"P-значение: {p_value}\n")

    alpha = 0.05
    if p_value < alpha:
        result_file.write(
            "Отвергаем нулевую гипотезу: Наблюдаемые частоты значимо различаются от ожидаемых.\n")
    else:
        result_file.write(
            "Не отвергаем нулевую гипотезу: Нет значимого различия между наблюдаемыми и ожидаемыми частотами.\n")


print(f"Результаты сохранены в файле: {result_path}")
