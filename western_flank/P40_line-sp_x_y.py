import pandas as pd
from pathlib import Path

# Пути
input_file = Path(r"c:\Users\gennady\PycharmProjects\input\028_interpolate\Final-western-flank-up-hole-data_remove_6_lines.csv")
output_file = input_file.with_name("Final-western-flank-up-hole-data_merged.csv")

# Чтение файла (без заголовков)
df = pd.read_csv(input_file, sep="\t", header=None, dtype=str)

# Удаляем 3-ю и 4-ю колонки (индексы 2 и 3)
df = df.drop(columns=[2, 3])

# Объединяем первую и вторую колонки через '-'
df[0] = df[0].astype(str) + '-' + df[1].astype(str)

# Убираем вторую колонку (она уже объединена)
df = df.drop(columns=[1])

# Удаляем дубликаты строк
df = df.drop_duplicates()

# Сохраняем в новый файл
df.to_csv(output_file, sep="\t", index=False, header=False)

print(f"Файл сохранён: {output_file}")
