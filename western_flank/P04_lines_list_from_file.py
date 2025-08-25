import csv
import os

# путь к исходному файлу
input_file = r"c:\Users\gennady\PycharmProjects\input\018_lines\western-flank-up-hole-data-20250821_remove_6_lines.csv"

# имя выходного файла
output_file = os.path.join(os.path.dirname(input_file), "first_column.txt")

# читаем файл и вытаскиваем первую колонку
with open(input_file, newline='', encoding="utf-8") as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    first_column = [row[0] for row in reader if row]  # row[0] — первая колонка

# сохраняем в текстовый файл
with open(output_file, "w", encoding="utf-8") as f:
    for item in first_column:
        f.write(item + "\n")

print(f"Первая колонка сохранена в {output_file}")
