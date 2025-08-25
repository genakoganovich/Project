import os
from pathlib import Path
import shutil

# Папка с исходными файлами
input_dir = Path(r"c:\Users\gennady\PycharmProjects\input\026_coord_by_ext")

# Пройти по всем файлам в папке
for file in input_dir.iterdir():
    if file.is_file():
        ext = file.suffix.lower().lstrip(".")  # расширение без точки, напр. "txt"
        if not ext:  # если файл без расширения
            ext = "noext"

        # Папка для этого расширения
        target_dir = input_dir / ext
        target_dir.mkdir(exist_ok=True)

        # Куда переносить
        target_file = target_dir / file.name

        # Переносим файл
        shutil.move(str(file), str(target_file))
        print(f"✔ {file.name} → {target_dir}")

print("Готово!")
