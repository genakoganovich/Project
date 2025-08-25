import os
from pathlib import Path

# Пути
input_dir = Path(r"c:\Users\gennady\PycharmProjects\input\025_remove_str_duplication")
output_dir = Path(r"c:\Users\gennady\PycharmProjects\output\025_remove_str_duplication")

# Создать папку для результатов, если её нет
output_dir.mkdir(parents=True, exist_ok=True)

# Обойти все файлы в input_dir
for file in input_dir.glob("*"):
    if file.is_file():
        # Читать все строки
        lines = file.read_text(encoding="utf-8").splitlines()

        # Удалить дубликаты, сохранив порядок
        seen = set()
        unique_lines = []
        for line in lines:
            if line not in seen:
                seen.add(line)
                unique_lines.append(line)

        # Сохранить в output_dir с тем же именем
        out_file = output_dir / file.name
        out_file.write_text("\n".join(unique_lines) + "\n", encoding="utf-8")

        print(f"✔ {file.name} → {out_file}")

print("Готово!")
