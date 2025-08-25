import pandas as pd

# Пути к файлам
input_file = r"c:\Users\gennady\PycharmProjects\input\023_concat_fix_fold\concat\concatenated.txt"
output_file = r"c:\Users\gennady\PycharmProjects\input\023_concat_fix_fold\concat\duplicates_SP.txt"

# Читаем файл (табуляция, без заголовков)
df = pd.read_csv(input_file, sep="\t", header=None, names=["line", "SP", "x", "y"])

# Приводим SP к числовому типу
df["SP"] = pd.to_numeric(df["SP"], errors="coerce")

# Убираем строки с некорректным SP
df = df.dropna(subset=["SP"])

# Находим дубликаты SP внутри каждой линии
duplicates = df[df.duplicated(subset=["line", "SP"], keep=False)]

# Сохраняем дубликаты в отдельный файл
duplicates.to_csv(output_file, sep="\t", index=False, header=False)

print(f"Найдено {len(duplicates)} строк-дубликатов. Сохранено в {output_file}")
