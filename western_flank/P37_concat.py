import os

# папка с исходными файлами
source_folder = r"c:\Users\gennady\PycharmProjects\input\027_concat"
# имя выходного файла
output_file = os.path.join(source_folder, "concatenated.txt")

with open(output_file, "w", encoding="utf-8") as f_out:
    for filename in os.listdir(source_folder):
        filepath = os.path.join(source_folder, filename)
        if os.path.isfile(filepath):
            with open(filepath, "r", encoding="utf-8") as f_in:
                lines = f_in.readlines()
                # убираем пустые строки в конце файла
                while lines and lines[-1].strip() == "":
                    lines.pop()
                # записываем очищенные строки
                for line in lines:
                    f_out.write(line.rstrip() + "\n")

print(f"Все файлы объединены в {output_file}")
