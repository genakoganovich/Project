import os
import shutil

# Пути
base_dir = r"c:\data\BeachEnergy\WesternFlank\Coordinates"
input_dir = os.path.join(base_dir, "input")
fixed_dir = os.path.join(base_dir, "Coordinates_fixed")

# 1. Создать папку input, если её нет
os.makedirs(input_dir, exist_ok=True)

# 2. Получить список файлов из Coordinates_fixed
fixed_files = set(os.listdir(fixed_dir))

# 3. Копировать файлы из Coordinates, если имена совпадают
for filename in fixed_files:
    source_file = os.path.join(base_dir, filename)
    if os.path.isfile(source_file):  # только файлы
        target_file = os.path.join(input_dir, filename)
        shutil.copy2(source_file, target_file)
        print(f"Скопирован: {filename}")

print("Готово!")
