import pandas as pd
import numpy as np
from scipy.interpolate import interp1d

# Пути к файлам
file_concat = r"c:\Users\gennady\PycharmProjects\input\028_interpolate\concatenated.txt"
file_lines = r"c:\Users\gennady\PycharmProjects\input\028_interpolate\Final-western-flank-up-hole-data_remove_6_lines.csv"

# ---------- Чтение файлов ----------
df_concat = pd.read_csv(
    file_concat,
    sep="\t",
    header=None,
    names=["line", "SP", "x", "y"],
    dtype=str
)

df_lines = pd.read_csv(
    file_lines,
    sep="\t",
    header=None,
    names=["line", "SP", "t", "z"],
    dtype=str
)

# ---------- Приведение типов ----------
df_concat["SP"] = pd.to_numeric(df_concat["SP"], errors="coerce")
df_concat["x"] = pd.to_numeric(df_concat["x"], errors="coerce")
df_concat["y"] = pd.to_numeric(df_concat["y"], errors="coerce")

df_lines["SP"] = pd.to_numeric(df_lines["SP"], errors="coerce")
df_lines["t"] = pd.to_numeric(df_lines["t"], errors="coerce")
df_lines["z"] = pd.to_numeric(df_lines["z"], errors="coerce")

# Убираем строки с NaN в числовых колонках
df_concat = df_concat.dropna(subset=["SP", "x", "y"])
df_lines = df_lines.dropna(subset=["SP", "t", "z"])

# ---------- Убираем дубликаты SP ----------
df_concat = df_concat.groupby(["line", "SP"], as_index=False).mean()

# ---------- Интерполяция ----------
df_lines["x"] = np.nan
df_lines["y"] = np.nan

for line_id in df_lines["line"].unique():
    subset = df_concat[df_concat["line"] == line_id].sort_values("SP")
    if len(subset) < 2:
        continue  # нужно хотя бы 2 точки для интерполяции

    f_x = interp1d(subset["SP"], subset["x"], kind="linear", fill_value="extrapolate")
    f_y = interp1d(subset["SP"], subset["y"], kind="linear", fill_value="extrapolate")

    mask = df_lines["line"] == line_id
    df_lines.loc[mask, "x"] = f_x(df_lines.loc[mask, "SP"])
    df_lines.loc[mask, "y"] = f_y(df_lines.loc[mask, "SP"])

# ---------- Замена NaN/inf ----------
# df_lines["x"] = pd.to_numeric(df_lines["x"], errors="coerce")
# df_lines["y"] = pd.to_numeric(df_lines["y"], errors="coerce")

# df_lines["x"].replace([np.inf, -np.inf], np.nan, inplace=True)
# df_lines["y"].replace([np.inf, -np.inf], np.nan, inplace=True)

# df_lines["x"] = df_lines["x"].fillna(method="ffill").fillna(method="bfill").fillna(0)
# df_lines["y"] = df_lines["y"].fillna(method="ffill").fillna(method="bfill").fillna(0)

df_lines["x"] = pd.to_numeric(df_lines["x"], errors="coerce")
df_lines["y"] = pd.to_numeric(df_lines["y"], errors="coerce")

df_lines["x"] = df_lines["x"].replace([np.inf, -np.inf], np.nan)
df_lines["y"] = df_lines["y"].replace([np.inf, -np.inf], np.nan)

df_lines["x"] = df_lines["x"].ffill().bfill().fillna(0)
df_lines["y"] = df_lines["y"].ffill().bfill().fillna(0)

# ---------- Округление ----------
df_lines["x"] = df_lines["x"].round().astype(int)
df_lines["y"] = df_lines["y"].round().astype(int)

# ---------- Сохранение ----------
df_lines.to_csv(file_lines, sep="\t", index=False, header=False)

print(f"Файл сохранён: {file_lines}")
