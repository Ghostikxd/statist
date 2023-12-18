from scipy.stats import shapiro


def read_samples(file_path):
    with open(file_path, 'r') as f:
        samples = [list(map(float, line.strip().split()))
                   for line in f.readlines()]
    return samples


file_path = "Inp\\shapiro.inp"


samples = read_samples(file_path)


results = [shapiro(sample) for sample in samples]


result_path = "Out\\shapiro.out"
with open(result_path, 'a+') as result_file:
    for i, result in enumerate(results):
        stat, p_value = result
        result_file.write(f"Статистика критерия для выборки {i+1}: {stat}\n")
        result_file.write(f"P-значение для выборки {i+1}: {p_value}\n")

        alpha = 0.05
        if p_value < alpha:
            result_file.write(
                f"Отвергаем нулевую гипотезу для выборки {i+1}: Распределение не нормальное.\n")
        else:
            result_file.write(
                f"Не отвергаем нулевую гипотезу для выборки {i+1}: Распределение нормальное.\n")


print(f"Результаты сохранены в файле: {result_path}")
