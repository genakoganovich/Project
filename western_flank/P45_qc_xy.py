import pandas as pd
import matplotlib.pyplot as plt

file_updated = r"c:\Users\gennady\PycharmProjects\input\030_set_coord_by_key\Final-western-flank-up-hole-data_updated.csv"
file_ref = r"c:\Users\gennady\PycharmProjects\input\030_set_coord_by_key\Final-western-flank-up-hole-data_merged_to7854.csv"

# читаем обновленный файл
df_updated = pd.read_csv(file_updated, sep="\t")

# читаем эталонный файл
df_ref = pd.read_csv(file_ref, sep="\t")
df_ref[["Line name", "SP"]] = df_ref["Line name-SP"].str.rsplit("-", n=1, expand=True)
df_ref = df_ref.drop(columns=["Line name-SP"])

# приведение к строковому виду
df_updated["SP"] = df_updated["SP"].astype(str).str.strip()
df_ref["SP"] = df_ref["SP"].astype(str).str.strip()
df_updated["Line name"] = df_updated["Line name"].astype(str).str.strip()
df_ref["Line name"] = df_ref["Line name"].astype(str).str.strip()

# объединение по ключам
merged = df_updated.merge(df_ref, on=["Line name", "SP"], suffixes=("_upd", "_ref"))

# график 1: X сравнение
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(merged["X_ref"], merged["X_upd"], alpha=0.6)
plt.plot([merged["X_ref"].min(), merged["X_ref"].max()],
         [merged["X_ref"].min(), merged["X_ref"].max()],
         'r--')
plt.xlabel("X_ref (из merged_to7854)")
plt.ylabel("X_upd (из updated)")
plt.title("Сравнение X")

# график 2: Y сравнение
plt.subplot(1, 2, 2)
plt.scatter(merged["Y_ref"], merged["Y_upd"], alpha=0.6)
plt.plot([merged["Y_ref"].min(), merged["Y_ref"].max()],
         [merged["Y_ref"].min(), merged["Y_ref"].max()],
         'r--')
plt.xlabel("Y_ref (из merged_to7854)")
plt.ylabel("Y_upd (из updated)")
plt.title("Сравнение Y")

plt.tight_layout()
plt.show()

# график 3: сравнение координат на карте
plt.figure(figsize=(6,6))
plt.scatter(merged["X_ref"], merged["Y_ref"], label="Ref (merged_to7854)", alpha=0.6)
plt.scatter(merged["X_upd"], merged["Y_upd"], label="Updated", alpha=0.6, marker="x")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Координаты Ref vs Updated")
plt.legend()
plt.show()
