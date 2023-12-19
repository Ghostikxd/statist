from scipy.stats import wilcoxon


def read_data(file_path):
    # Функция для чтения данных из файла
    with open(file_path, 'r') as f:
        data = [float(line.strip()) for line in f.readlines()]
    return data


file_path_before = "main\\5 section\\5.1\\median_before.inp"
file_path_after = "main\\5 section\\5.1\\median_after.inp"

# Чтение данных до и после
data_before = read_data(file_path_before)
data_after = read_data(file_path_after)

# Выполнение критерия Вилкоксона для парных выборок
statistic, p_value = wilcoxon(data_before, data_after)

result_path = "main\\5 section\\5.1\\median.out"

# Запись результатов в файл
with open(result_path, 'w') as result_file:
    result_file.write(f"Статистика критерия знаков для медианы: {statistic}\n")
    result_file.write(f"P-значение: {p_value}\n")

    alpha = 0.05
    if p_value < alpha:
        result_file.write(
            "Отвергаем нулевую гипотезу: Есть статистически значимые различия в медиане.\n")
    else:
        result_file.write(
            "Не отвергаем нулевую гипотезу: Нет статистически значимых различий в медиане.\n")

print(f"Результаты сохранены в файле: {result_path}")
