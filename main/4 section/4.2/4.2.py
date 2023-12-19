from scipy.stats import kstest


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


def perform_kstest(samples):
    """
    Выполнение теста Колмогорова-Смирнова для оценки нормальности распределения.

    Parameters:
    - samples (list): Список выборок.

    Returns:
    - results (list): Список результатов теста для каждой выборки.
    """
    results = [kstest(sample, 'norm') for sample in samples]
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
            stat, p_value = result.statistic, result.pvalue
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
    input_file_path = "main\\4 section\\4.2\\smirnov.inp"

    # Чтение выборок из файла
    samples = read_samples(input_file_path)

    # Выполнение теста Колмогорова-Смирнова
    results = perform_kstest(samples)

    # Путь к файлу для сохранения результатов
    output_result_path = "main\\4 section\\4.2\\smirnov.out"

    # Сохранение результатов теста в файл
    save_results(output_result_path, results)

    print(f"Результаты сохранены в файле: {output_result_path}")
