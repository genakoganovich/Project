import os

# Пути к файлам
input_file = r"c:\Users\gennady\PycharmProjects\input\029_convert_coord\Final-western-flank-up-hole-data_merged.csv"
output_file = os.path.splitext(input_file)[0] + "_converted.csv"

with open(input_file, "r", encoding="utf-8") as fin, open(output_file, "w", encoding="utf-8") as fout:
    for line in fin:
        # Найти позиции всех "-" в строке
        positions = [i for i, ch in enumerate(line) if ch == "-"]

        if len(positions) >= 2:
            # Второй "-" заменить на табуляцию
            pos = positions[1]
            line = line[:pos] + "\t" + line[pos+1:]

        fout.write(line)

print(f"Готово! Результат сохранен в: {output_file}")
