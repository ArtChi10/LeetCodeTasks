from itertools import combinations
import numpy as np

def count_arrangements(matrix_size=3, ones_count=4):
    # Общее количество ячеек в матрице
    total_cells = matrix_size ** 2

    # Генерируем все возможные комбинации индексов для размещения 4 единиц
    combinations_of_ones = combinations(range(total_cells), ones_count)

    # Инициализируем счётчики
    arrangement_count = 0
    row_or_column_count = 0

    # Перебираем все комбинации
    for combination in combinations_of_ones:
        # Создаём матрицу 3x3, заполненную нулями
        matrix = np.zeros((matrix_size, matrix_size), dtype=int)

        # Расставляем единицы в матрице
        for index in combination:
            row = index // matrix_size  # Номер строки
            col = index % matrix_size  # Номер столбца
            matrix[row, col] = 1

        # Проверяем, есть ли три или более единиц в одной строке или столбце
        row_sums = matrix.sum(axis=1)
        col_sums = matrix.sum(axis=0)

        if 3 in row_sums or 3 in col_sums:
            row_or_column_count += 1

        arrangement_count += 1

    return arrangement_count, row_or_column_count

# Подсчёт всех возможных вариантов
result, row_or_column_result = count_arrangements()
print(f"Общее количество способов расставить 4 единицы в матрице 3x3: {result}")
print(f"Количество способов, где три или более единиц находятся в одной строке или столбце: {row_or_column_result}")
