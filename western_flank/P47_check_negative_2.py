import pandas as pd

file_path = r"c:\Users\gennady\PycharmProjects\input\029_convert_coord\Final-western-flank-up-hole-data_merged.csv"

# читаем файл (разделитель табуляция)
df = pd.read_csv(file_path, sep="\t")

# маски для отрицательных X и Y
neg_x = df["X"] < 0
neg_y = df["Y"] < 0

# проверка наличия
print("Есть ли отрицательные значения в X:", neg_x.any())
print("Есть ли отрицательные значения в Y:", neg_y.any())

# количество строк с отрицательными значениями
count_neg_x = neg_x.sum()
count_neg_y = neg_y.sum()
count_neg_xy = (neg_x | neg_y).sum()

print("Число строк с отрицательными X:", count_neg_x)
print("Число строк с отрицательными Y:", count_neg_y)
print("Число строк с отрицательными X или Y:", count_neg_xy)

# при желании показать такие строки
if count_neg_xy > 0:
    print("\nСтроки с отрицательными X или Y:")
    print(df[neg_x | neg_y])
