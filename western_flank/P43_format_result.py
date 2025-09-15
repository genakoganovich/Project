import os
import csv

# Пути к файлам
input_file = r"c:\Users\gennady\PycharmProjects\input\029_convert_coord\Final-western-flank-up-hole-data_merged_converted_to7854.csv"
output_file = os.path.splitext(input_file)[0] + "_final.csv"

with open(input_file, "r", encoding="utf-8") as fin, open(output_file, "w", encoding="utf-8", newline="") as fout:
    reader = csv.reader(fin, delimiter="\t")
    writer = csv.writer(fout, delimiter="\t")

    for row in reader:
        if len(row) < 6:
            continue  # если строка слишком короткая, пропускаем

        # 1. Объединяем первую и вторую колонки через "-"
        col1 = f"{row[0]}-{row[1]}"

        # 2. Удаляем колонки 3 и 4 (X, Y исходные)
        # 3. Колонки 5 и 6 (конечные координаты) - оставляем только целую часть
        try:
            col2 = str(int(float(row[4])))  # колонка 5
            col3 = str(int(float(row[5])))  # колонка 6
        except ValueError:
            col2 = row[4]
            col3 = row[5]

        # Записываем новую строку
        writer.writerow([col1, col2, col3])

print(f"Готово! Результат сохранен в: {output_file}")
