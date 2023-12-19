from scipy.stats import shapiro


def read_samples(file_path):
    """
    Чтение выборок из файла.

    Parameters:
    - file_path (str): Путь к файлу с выборками.

    Returns:
    - samples (list): Список выборок.
    """
    with open(file_path, 'r') as f:
        samples = [list(map(float, line.strip().split()))
                   for line in f.readlines()]
    return samples


def perform_shapiro_test(samples):
    """
    Выполнение теста Шапиро-Уилка для оценки нормальности распределения.

    Parameters:
    - samples (list): Список выборок.

    Returns:
    - results (list): Список результатов теста для каждой выборки.
    """
    results = [shapiro(sample) for sample in samples]
    return results


def save_results(result_path, results):
    """
    Сохранение результатов теста в файл.

    Parameters:
    - result_path (str): Путь к файлу для сохранения результатов.
    - results (list): Список результатов теста.
    """
    with open(result_path, 'a+') as result_file:
        for i, result in enumerate(results):
            stat, p_value = result
            result_file.write(
                f"Статистика критерия для выборки {i+1}: {stat}\n")
            result_file.write(f"P-значение для выборки {i+1}: {p_value}\n")

            alpha = 0.05
            if p_value < alpha:
                result_file.write(
                    f"Отвергаем нулевую гипотезу для выборки {i+1}: Распределение не нормальное.\n")
            else:
                result_file.write(
                    f"Не отвергаем нулевую гипотезу для выборки {i+1}: Распределение нормальное.\n")


if __name__ == "__main__":
    # Путь к файлу с выборками
    input_file_path = "main\\4 section\\4.1\\shapiro.inp"

    # Чтение выборок из файла
    samples = read_samples(input_file_path)

    # Выполнение теста Шапиро-Уилка
    results = perform_shapiro_test(samples)

    # Путь к файлу для сохранения результатов
    output_result_path = "main\\4 section\\4.1\\shapiro.out"

    # Сохранение результатов теста в файл
    save_results(output_result_path, results)

    print(f"Результаты сохранены в файле: {output_result_path}")
