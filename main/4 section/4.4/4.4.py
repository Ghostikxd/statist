import numpy as np
from scipy.stats import chi2_contingency


def read_data(file_path):
    """
    Чтение данных из файла.

    Parameters:
    - file_path (str): Путь к файлу с данными.

    Returns:
    - np.array: Двумерный массив с данными.
    """
    with open(file_path, 'r') as f:
        data = [list(map(int, line.strip().split())) for line in f.readlines()]
    return np.array(data)


def perform_chi_square_test(observed_data):
    """
    Выполнение критерия хи-квадрат для таблицы сопряженности.

    Parameters:
    - observed_data (np.array): Двумерный массив с наблюдаемыми данными.

    Returns:
    - tuple: Кортеж с результатами теста (статистика хи-квадрат, p-значение, ...).
    """
    chi2_stat, p_value, _, _ = chi2_contingency(observed_data)
    return chi2_stat, p_value


def save_results(result_path, chi2_stat, p_value):
    """
    Сохранение результатов теста в файл.

    Parameters:
    - result_path (str): Путь к файлу для сохранения результатов.
    - chi2_stat (float): Статистика критерия хи-квадрат.
    - p_value (float): P-значение.
    """
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


if __name__ == "__main__":
    # Путь к файлу с данными
    input_file_path = "main\\4 section\\4.4\\chi_square.inp"

    # Чтение данных из файла
    observed_data = read_data(input_file_path)

    # Путь к файлу для сохранения результатов
    output_result_path = "main\\4 section\\4.4\\chi_square.out"

    # Выполнение критерия хи-квадрат
    chi2_stat, p_value = perform_chi_square_test(observed_data)

    # Сохранение результатов теста в файл
    save_results(output_result_path, chi2_stat, p_value)

    print(f"Результаты сохранены в файле: {output_result_path}")
