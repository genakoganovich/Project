import os

# путь к входному файлу
input_file = r"c:\Users\gennady\PycharmProjects\input\018_lines\first_column.txt"

# путь к выходному файлу
output_file = os.path.join(os.path.dirname(input_file), "unique_names.txt")

# читаем строки, убираем повторы
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

# сохраняем только уникальные имена (в том порядке, как встречались в файле)
unique_lines = list(dict.fromkeys(lines))

# записываем результат
with open(output_file, "w", encoding="utf-8") as f:
    for line in unique_lines:
        f.write(line + "\n")

print(f"Уникальные имена сохранены в {output_file}")
