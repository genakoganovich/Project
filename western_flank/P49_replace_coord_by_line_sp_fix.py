import pandas as pd

file1 = r"c:\Users\gennady\PycharmProjects\input\031_set_coord_by_key_fix\Final-western-flank-up-hole-data_remove_6_lines.csv"
file2 = r"c:\Users\gennady\PycharmProjects\input\031_set_coord_by_key_fix\Final-western-flank-up-hole-data_merged_converted_to7854_20250928.csv"
output = r"c:\Users\gennady\PycharmProjects\input\031_set_coord_by_key_fix\Final-western-flank-up-hole-data_updated_20250928.csv"

# читаем первый файл (6 колонок, разделитель таб)
df1 = pd.read_csv(file1, sep="\t")

# читаем второй файл (разделитель таб)
df2 = pd.read_csv(file2, sep="\t")

# разбиваем Line name-SP по последнему минусу
df2[["Line name", "SP"]] = df2["Line name-SP"].str.rsplit("-", n=1, expand=True)
df2 = df2.drop(columns=["Line name-SP"])

# приведение к строковому виду для надежного join
df1["SP"] = df1["SP"].astype(str).str.strip()
df2["SP"] = df2["SP"].astype(str).str.strip()
df1["Line name"] = df1["Line name"].astype(str).str.strip()
df2["Line name"] = df2["Line name"].astype(str).str.strip()

# объединение по ключам
merged = df1.merge(df2, on=["Line name", "SP"], suffixes=("", "_new"))

# заменяем координаты
merged["X"] = merged["X_new"]
merged["Y"] = merged["Y_new"]
merged = merged.drop(columns=["X_new", "Y_new"])

# сохраняем результат
merged.to_csv(output, sep="\t", index=False)
