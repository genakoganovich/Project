import os

# путь к исходному файлу
input_file = r"c:\Users\gennady\PycharmProjects\input\018_lines\western-flank-up-hole-data-20250820.csv"

# имя нового файла
output_file = os.path.join(os.path.dirname(input_file), "western-flank-up-hole-data-20250820_fixed.csv")

# читаем файл и заменяем
with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()

# замена
content = content.replace("92.CKY", "92-CKY")

# сохраняем в новый файл
with open(output_file, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Файл сохранён: {output_file}")
