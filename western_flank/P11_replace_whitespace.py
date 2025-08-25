import os

# папка с файлами
folder = r"c:\Users\gennady\PycharmProjects\input\020_coord_by_format\004_txt_4_col"

# куда сохранить исправленные файлы
output_folder = os.path.join(folder, "tabbed")
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    if os.path.isfile(filepath):
        output_file = os.path.join(output_folder, filename)

        with open(filepath, "r", encoding="utf-8") as f_in, open(output_file, "w", encoding="utf-8") as f_out:
            for line in f_in:
                # убираем лишние пробелы по краям и разбиваем по любому количеству пробелов
                parts = line.strip().split()
                # соединяем табами
                f_out.write("\t".join(parts) + "\n")

        print(f"Файл {filename} преобразован → {output_file}")

print("Готово!")
