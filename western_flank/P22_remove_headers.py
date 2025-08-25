import os


def is_data_line(line):
    """
    Проверяет, является ли строка строкой данных.
    Строка считается данными, если все колонки могут быть приведены к float.
    """
    line = line.strip()
    if not line:
        return False  # пустая строка
    parts = line.split("\t")  # разделитель таб
    try:
        [float(p) for p in parts]
        return True
    except ValueError:
        return False


# Папки
input_folder = r"c:\Users\gennady\PycharmProjects\input\024_remove_headers"
output_folder = r"c:\Users\gennady\PycharmProjects\output\024_remove_headers"
os.makedirs(output_folder, exist_ok=True)

# Обработка файлов
for filename in os.listdir(input_folder):
    input_path = os.path.join(input_folder, filename)

    if not os.path.isfile(input_path):
        continue

    # Читаем все строки
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Оставляем только строки данных (числовые строки)
    data_lines = [line for line in lines if is_data_line(line)]

    # Сохраняем в новую папку
    output_path = os.path.join(output_folder, filename)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(data_lines)

    print(f"Файл обработан: {filename}, строк осталось: {len(data_lines)}")

print("Готово! Все файлы обработаны и сохранены.")
