import os

# Пути
heads_file = r"c:\Users\gennady\.gPlatform_v4\GSpace\DEMO\demo_project\wells\Heads\Well_heads.txt"
folders = [
    r"c:\Users\gennady\.gPlatform_v4\GSpace\DEMO\demo_project\wells\Inclination\Others",
    r"c:\Users\gennady\.gPlatform_v4\GSpace\DEMO\demo_project\wells\Inclination\Wells with long P-wave & Density",
]

# --- 1. Считываем базовые имена файлов из первой колонки (со второй строки) ---
with open(heads_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

file_names_from_txt = [line.strip().split("\t")[0] for line in lines[1:] if line.strip()]

# --- 2. Собираем базовые имена файлов из папок ---
file_names_from_folders = []
for folder in folders:
    for f in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, f)):
            base_name = os.path.splitext(f)[0]  # убираем расширение
            file_names_from_folders.append(base_name)

# --- 3. Сравнение ---
set_txt = set(file_names_from_txt)
set_folders = set(file_names_from_folders)

missing_in_folders = set_txt - set_folders
extra_in_folders = set_folders - set_txt

print("Файлы, указанные в txt, но отсутствующие в папках:")
for f in sorted(missing_in_folders):
    print("  ", f)

print("\nФайлы, которые есть в папках, но отсутствуют в txt:")
for f in sorted(extra_in_folders):
    print("  ", f)
