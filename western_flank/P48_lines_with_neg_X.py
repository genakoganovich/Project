import pandas as pd

file_path = r"c:\Users\gennady\PycharmProjects\input\029_convert_coord\Final-western-flank-up-hole-data_merged_converted_to7854_final.csv"

# читаем csv (разделитель табуляция)
df = pd.read_csv(file_path, sep="\t")

# маска для отрицательных значений
mask = (df["X"] < 0) | (df["Y"] < 0)

# фильтруем строки с отрицательными X или Y
neg_lines = df.loc[mask, "Line name-SP"]

# оставляем всё до последнего дефиса (отбрасываем "-SP")
line_names = neg_lines.str.rsplit("-", n=1).str[0].unique()

print("Есть ли отрицательные значения в X или Y:", mask.any())
print("Список Line name с отрицательными X или Y:")
for line in line_names:
    print(line)
