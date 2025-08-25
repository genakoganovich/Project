import os

# путь к папке
folder = r"c:\Users\gennady\PycharmProjects\input\019_coord"

# имя выходного файла
output_file = os.path.join(folder, "file_list.txt")

# собираем имена файлов без расширений
filenames = [
    os.path.splitext(f)[0]
    for f in os.listdir(folder)
    if os.path.isfile(os.path.join(folder, f))
]

# сохраняем в текстовый файл
with open(output_file, "w", encoding="utf-8") as f:
    for name in filenames:
        f.write(name + "\n")

print(f"Список сохранён в {output_file}")
