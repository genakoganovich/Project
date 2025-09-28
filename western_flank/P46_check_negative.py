import pandas as pd

file_path = r"c:\data\BeachEnergy\WesternFlank\xlxs\20250928\Final-western-flank-up-hole-data_merged_columns_to7854_20280928.csv"

df = pd.read_csv(file_path, sep="\t")

# проверяем отрицательные значения
neg_x = df["X"] < 0
neg_y = df["Y"] < 0

print("Есть ли отрицательные значения в X:", neg_x.any())
print("Есть ли отрицательные значения в Y:", neg_y.any())

# количество строк с отрицательными X
count_neg_x = neg_x.sum()
print("Число строк с отрицательными X:", count_neg_x)

# при желании вывести строки с отрицательными X или Y
negatives = df[neg_x | neg_y]
if not negatives.empty:
    print("\nСтроки с отрицательными значениями:")
    print(negatives)
