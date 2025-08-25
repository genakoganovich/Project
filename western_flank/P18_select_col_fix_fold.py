import os

# папка с исходными файлами
source_folder = r"c:\Users\gennady\PycharmProjects\input\020_coord_by_format\001_txt_6_col\002_fixed_fold"
# папка для новых файлов
target_folder = os.path.join(source_folder, "selected_columns")

# создаём папку для результатов
os.makedirs(target_folder, exist_ok=True)

# индексы нужных колонок (нумерация с 0)
cols = [0, 1, 3, 4]

for filename in os.listdir(source_folder):
    filepath = os.path.join(source_folder, filename)
    if os.path.isfile(filepath):
        output_file = os.path.join(target_folder, filename)

        with open(filepath, "r", encoding="utf-8") as f_in, open(output_file, "w", encoding="utf-8") as f_out:
            for line in f_in:
                parts = line.strip().split()
                # проверим, что колонок достаточно
                if len(parts) >= max(cols) + 1:
                    selected = [parts[i] for i in cols]
                    f_out.write("\t".join(selected) + "\n")

        print(f"Создан файл {output_file}")

print("Готово!")
