import os

# путь к папке
folder = r"c:\Users\gennady\PycharmProjects\input\020_coord_by_format"

# имя выходного CSV файла
output_file = os.path.join(folder, "file_columns_table.csv")

# список для данных
table = []

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    if os.path.isfile(filepath):
        name_without_ext = os.path.splitext(filename)[0]

        # считаем число колонок в первой строке
        with open(filepath, "r", encoding="utf-8") as f:
            first_line = f.readline().strip()
            num_columns = len(first_line.split()) if first_line else 0

        table.append([name_without_ext, num_columns])

# сохраняем таблицу в CSV
with open(output_file, "w", encoding="utf-8") as f:
    f.write("Filename,NumColumns\n")
    for row in table:
        f.write(f"{row[0]},{row[1]}\n")

print(f"Таблица сохранена в {output_file}")
