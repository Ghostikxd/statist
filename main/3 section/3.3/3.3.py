from scipy import stats


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


def perform_bartlett_test(samples):
    """
    Выполнение теста Бартлетта для оценки равенства дисперсий.

    Parameters:
    - samples (list): Список выборок.

    Returns:
    - statistic (float): Значение статистики теста.
    - p_value (float): P-значение теста.
    """
    statistic, p_value = stats.bartlett(*samples)
    return statistic, p_value


def save_results(result_path, statistic, p_value):
    """
    Сохранение результатов теста в файл.

    Parameters:
    - result_path (str): Путь к файлу для сохранения результатов.
    - statistic (float): Значение статистики теста.
    - p_value (float): P-значение теста.
    """
    with open(result_path, 'a+') as result_file:
        result_file.write(f"Статистика критерия: {statistic}\n")
        result_file.write(f"P-значение: {p_value}\n")

        alpha = 0.05
        if p_value < alpha:
            result_file.write(
                "Отвергаем нулевую гипотезу: Дисперсии не равны.\n")
        else:
            result_file.write(
                "Не отвергаем нулевую гипотезу: Дисперсии равны.\n")


if __name__ == "__main__":
    # Путь к файлу с выборками
    file_path = "main\\3 section\\3.3\\barlet.inp"

    # Чтение выборок из файла
    samples = read_samples(file_path)

    # Выполнение теста Бартлетта
    statistic, p_value = perform_bartlett_test(samples)

    # Путь к файлу для сохранения результатов
    result_path = "main\\3 section\\3.3\\barlet.out"

    # Сохранение результатов теста в файл
    save_results(result_path, statistic, p_value)

    print(f"Результаты сохранены в файле: {result_path}")
