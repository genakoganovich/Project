import os
import shutil

# исходная папка
source_folder = r"c:\Users\gennady\PycharmProjects\input\020_coord_by_format"
# папка для файлов с 6 колонками
target_folder = os.path.join(source_folder, "001_txt_6")

# создаём целевую папку, если её нет
os.makedirs(target_folder, exist_ok=True)

# перебираем файлы в исходной папке
for filename in os.listdir(source_folder):
    filepath = os.path.join(source_folder, filename)
    if os.path.isfile(filepath):
        # читаем первую строку и считаем число колонок
        with open(filepath, "r", encoding="utf-8") as f:
            first_line = f.readline().strip()
            num_columns = len(first_line.split()) if first_line else 0

        # если колонок 6 — перемещаем файл
        if num_columns == 6:
            shutil.move(filepath, os.path.join(target_folder, filename))
            print(f"Файл {filename} перемещён")

print("Готово!")
