import os

# папка с исходными файлами
source_folder = r"c:\Users\gennady\PycharmProjects\input\021_add_2_zeros"
# папка для сохранения новых файлов
target_folder = os.path.join(source_folder, "modified")
os.makedirs(target_folder, exist_ok=True)

for filename in os.listdir(source_folder):
    filepath = os.path.join(source_folder, filename)
    if os.path.isfile(filepath):
        output_file = os.path.join(target_folder, filename)

        with open(filepath, "r", encoding="utf-8") as f_in, open(output_file, "w", encoding="utf-8") as f_out:
            for line in f_in:
                parts = line.strip().split()
                if len(parts) >= 2:
                    value = parts[1]
                    # проверяем, целое ли число
                    if value.isdigit() or (value.startswith("-") and value[1:].isdigit()):
                        parts[1] = f"{int(value):.2f}"
                f_out.write("\t".join(parts) + "\n")

        print(f"Создан файл {output_file}")

print("Готово!")
