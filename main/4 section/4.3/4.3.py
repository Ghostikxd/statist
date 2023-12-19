from scipy.stats import anderson


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


def perform_anderson_test(samples):
    """
    Выполнение теста Андерсона-Дарлинга для оценки нормальности распределения.

    Parameters:
    - samples (list): Список выборок.

    Returns:
    - results (list): Список результатов теста для каждой выборки.
    """
    results = [anderson(sample, dist='norm') for sample in samples]
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
            stat = result.statistic
            critical_values = result.critical_values
            significance_level = result.significance_level
            result_file.write(
                f"Статистика критерия для выборки {i+1}: {stat}\n")
            result_file.write(f"Критические значения: {critical_values}\n")
            result_file.write(f"Уровень значимости: {significance_level}\n")

            alpha = 0.05
            if stat > critical_values[2] and significance_level < alpha:
                result_file.write(
                    f"Отвергаем нулевую гипотезу для выборки {i+1}: Распределение не нормальное.\n")
            else:
                result_file.write(
                    f"Не отвергаем нулевую гипотезу для выборки {i+1}: Распределение нормальное.\n")


if __name__ == "__main__":
    # Путь к файлу с выборками
    input_file_path = "main\\4 section\\4.3\\anderson.inp"

    # Чтение выборок из файла
    samples = read_samples(input_file_path)

    # Путь к файлу для сохранения результатов
    output_result_path = "main\\4 section\\4.3\\anderson.out"

    # Выполнение теста Андерсона-Дарлинга
    results = perform_anderson_test(samples)

    # Сохранение результатов теста в файл
    save_results(output_result_path, results)

    print(f"Результаты сохранены в файле: {output_result_path}")
