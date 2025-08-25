import csv
import os
import re

# путь к входному файлу
input_file = r"c:\Users\gennady\PycharmProjects\input\018_lines\western-flank-up-hole-data-20250820_fixed.csv"

# путь к выходному файлу
output_file = os.path.join(os.path.dirname(input_file), "invalid_names.txt")

# регулярное выражение для формата "xxx-yyy"
pattern = re.compile(r"^[^-]+-[^-]+$")

invalid_names = []

# читаем TSV (разделён табами)
with open(input_file, newline='', encoding="utf-8") as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        if row:  # если строка не пустая
            name = row[0].strip()
            if not pattern.match(name):
                invalid_names.append(name)

# сохраняем список
with open(output_file, "w", encoding="utf-8") as f:
    for name in invalid_names:
        f.write(name + "\n")

print(f"Найдено {len(invalid_names)} неподходящих имён. Результат сохранён в {output_file}")
