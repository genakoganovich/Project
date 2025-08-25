import os

# пути к файлам
file_unique = r"c:\Users\gennady\PycharmProjects\output\019_coord\unique_names.txt"
file_coord  = r"c:\Users\gennady\PycharmProjects\output\019_coord\coord_file_list.txt"

# путь к выходному файлу
output_file = os.path.join(os.path.dirname(file_unique), "names_not_in_coord.txt")

# читаем списки
with open(file_unique, "r", encoding="utf-8") as f:
    unique_names = set(f.read().splitlines())

with open(file_coord, "r", encoding="utf-8") as f:
    coord_names = set(f.read().splitlines())

# находим разницу (что есть в unique_names, но нет в coord_names)
diff_names = sorted(unique_names - coord_names)

# сохраняем результат
with open(output_file, "w", encoding="utf-8") as f:
    for name in diff_names:
        f.write(name + "\n")

print(f"Список отличий сохранён в {output_file}")
