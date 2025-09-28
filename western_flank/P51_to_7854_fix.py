import os
import csv
from pyproj import Transformer

# Пути к файлам
epsg_file = r"c:\Users\gennady\PycharmProjects\input\031_convert_coord_fix\WesternFlank_orig_epsg_20250928.csv"
data_file = r"c:\Users\gennady\PycharmProjects\input\031_convert_coord_fix\Final-western-flank-up-hole-data_merged_columns.csv"
output_file = os.path.splitext(data_file)[0] + "_to7854.csv"

# --- Шаг 1. Загружаем соответствие "линия -> EPSG"
line_to_epsg = {}
with open(epsg_file, "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        if len(row) >= 2:
            line, epsg = row[0].strip(), row[1].strip()
            if epsg.isdigit():
                line_to_epsg[line] = f"EPSG:{epsg}"

# --- Шаг 2. Обрабатываем данные и конвертируем координаты
with open(data_file, "r", encoding="utf-8") as fin, open(output_file, "w", encoding="utf-8", newline="") as fout:
    reader = csv.reader(fin, delimiter="\t")
    writer = csv.writer(fout, delimiter="\t")

    for row in reader:
        if len(row) < 4:
            writer.writerow(row)
            continue

        line, sp, x_str, y_str = row[0], row[1], row[2], row[3]

        try:
            x, y = float(x_str), float(y_str)
        except ValueError:
            writer.writerow(row)
            continue

        # Ищем EPSG для линии
        epsg_code = line_to_epsg.get(line)
        if not epsg_code:
            writer.writerow(row)  # если нет EPSG, оставляем строку как есть
            continue

        # Создаем трансформер
        transformer = Transformer.from_crs(epsg_code, "EPSG:7854", always_xy=True)

        # Переводим координаты
        lon, lat = transformer.transform(x, y)

        # Записываем результат (добавляем новые координаты)
        writer.writerow([line, sp, x, y, lon, lat])

print(f"Готово! Результат сохранен в: {output_file}")
