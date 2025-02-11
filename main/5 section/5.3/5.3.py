from scipy.stats import wilcoxon


def write_to_file(file_path, statistic, p_value, hypothesis_result):
    # Запись результатов в файл
    with open(file_path, 'w') as result_file:
        result_file.write(
            f"Статистика двухвыборочного критерия Уилкоксона: {statistic}\n")
        result_file.write(f"P-значение: {p_value}\n")
        result_file.write(hypothesis_result)


def read_from_file(file_path):
    # Чтение данных из файла
    with open(file_path, 'r') as file:
        lines = file.readlines()
        data_group1 = list(map(float, lines[0].split()))
        data_group2 = list(map(float, lines[1].split()))
    return data_group1, data_group2


# Пути к файлам
input_file_path = "main\\5 section\\5.3\\wilcoxon_2sample_input.inp"
output_file_path = "main\\5 section\\5.3\\wilcoxon_2sample_result.out"

# Чтение данных из файла
data_group1, data_group2 = read_from_file(input_file_path)

# Выполнение двухвыборочного критерия Уилкоксона
statistic, p_value = wilcoxon(data_group1, data_group2)

alpha = 0.05
# Определение результата гипотезы
if p_value < alpha:
    hypothesis_result = "Отвергаем нулевую гипотезу: Есть статистически значимые различия."
else:
    hypothesis_result = "Не отвергаем нулевую гипотезу: Нет статистически значимых различий."

# Запись результатов в файл
write_to_file(output_file_path, statistic, p_value, hypothesis_result)
print(f"Результаты сохранены в файле: {output_file_path}")
