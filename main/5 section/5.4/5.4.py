from scipy.stats import kruskal


def write_to_file(file_path, statistic, p_value, hypothesis_result):
    # Запись результатов в файл
    with open(file_path, 'w') as result_file:
        result_file.write(
            f"Статистика критерия Краскела-Уоллиса: {statistic}\n")
        result_file.write(f"P-значение: {p_value}\n")
        result_file.write(hypothesis_result)


def read_from_file(file_path):
    # Чтение данных из файла
    with open(file_path, 'r') as file:
        lines = file.readlines()
        groups = [list(map(float, line.strip().split())) for line in lines]
    return groups


# Пути к файлам
input_file_path = "main\\5 section\\5.4\\kruskal_input.inp"
output_file_path = "main\\5 section\\5.4\\kruskal_result.out"

# Чтение данных из файла
data_groups = read_from_file(input_file_path)

# Выполнение критерия Краскела-Уоллиса
statistic, p_value = kruskal(*data_groups)

alpha = 0.05
# Определение результата гипотезы
if p_value < alpha:
    hypothesis_result = "Отвергаем нулевую гипотезу: Есть статистически значимые различия между группами."
else:
    hypothesis_result = "Не отвергаем нулевую гипотезу: Нет статистически значимых различий между группами."

# Запись результатов в файл
write_to_file(output_file_path, statistic, p_value, hypothesis_result)
print(f"Результаты сохранены в файле: {output_file_path}")
