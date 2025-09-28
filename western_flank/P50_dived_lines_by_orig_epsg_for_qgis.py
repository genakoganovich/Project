import pandas as pd
import os

# пути к файлам
map_file = r"c:\Users\gennady\PycharmProjects\input\031_convert_coord_fix\WesternFlank_orig_epsg_20250928.csv"
data_file = r"c:\Users\gennady\PycharmProjects\input\031_convert_coord_fix\Final-western-flank-up-hole-data_merged_columns.csv"
output_dir = r"c:\Users\gennady\PycharmProjects\input\031_convert_coord_fix\output"

# создаём папку для результатов
os.makedirs(output_dir, exist_ok=True)

# читаем маппинг line name -> epsg
map_df = pd.read_csv(map_file, sep="\t")

# читаем основной файл
data_df = pd.read_csv(data_file, sep="\t")

# объединяем по line name
merged_df = data_df.merge(map_df, on="line name", how="left")

# группируем по original epsg и сохраняем
for epsg, group in merged_df.groupby("original epsg"):
    out_file = os.path.join(output_dir, f"Final_western_flank_epsg_{epsg}.csv")
    group.drop(columns=["original epsg"]).to_csv(out_file, sep="\t", index=False)
    print(f"Сохранён файл: {out_file} (строк: {len(group)})")
