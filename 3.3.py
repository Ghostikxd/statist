from scipy import stats


def read_samples(file_path):
    with open(file_path, 'r') as f:
        samples = [list(map(float, line.strip().split()))
                   for line in f.readlines()]
    return samples


file_path = "Inp/barlet.inp"


samples = read_samples(file_path)


statistic, p_value = stats.bartlett(*samples)


result_path = "Out/barlet.out"
with open(result_path, 'a+') as result_file:
    result_file.write(f"Статистика критерия: {statistic}\n")
    result_file.write(f"P-значение: {p_value}\n")

    alpha = 0.05
    if p_value < alpha:
        result_file.write("Отвергаем нулевую гипотезу: Дисперсии не равны.\n")
    else:
        result_file.write("Не отвергаем нулевую гипотезу: Дисперсии равны.\n")


print(f"Результаты сохранены в файле: {result_path}")
