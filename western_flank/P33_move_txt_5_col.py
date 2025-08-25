import shutil
from pathlib import Path

# Пути
src_dir = Path(r"c:\Users\gennady\PycharmProjects\input\026_coord_by_ext\001_txt")
dst_dir = src_dir / "005_txt_5_col"
ref_dir = Path(r"c:\Users\gennady\PycharmProjects\input\020_coord_by_format\005_txt_5_col\selected_columns")

# Создать целевую папку, если её нет
dst_dir.mkdir(parents=True, exist_ok=True)

# Получить имена файлов из эталонной папки
ref_files = {f.name for f in ref_dir.iterdir() if f.is_file()}

# Переложить только совпадающие
for file in src_dir.iterdir():
    if file.is_file() and file.name in ref_files:
        target = dst_dir / file.name
        shutil.move(str(file), str(target))
        print(f"✔ {file.name} → {dst_dir}")

print("Готово!")
