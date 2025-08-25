import pandas as pd
from pathlib import Path

# Пути к файлам
input_file = Path(r"c:\Users\gennady\PycharmProjects\input\028_interpolate\Final-western-flank-up-hole-data_remove_6_lines.csv")
output_file = input_file.with_name("Final-western-flank-up-hole-data_clean.csv")

# Чтение файла (без заголовков)
df = pd.read_csv(input_file, sep="\t", header=None, dtype=str)

# Удаляем колонки 1, 3, 4 (индексы 0, 2, 3)
df = df.drop(columns=[0, 2, 3])

# Удаляем дубликаты строк
df = df.drop_duplicates()

# Сохраняем результат
df.to_csv(output_file, sep="\t", index=False, header=False)

print(f"Файл сохранён: {output_file}")
