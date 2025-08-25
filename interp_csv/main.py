import pandas as pd
import numpy as np

# Загружаем данные (табуляция — \t, если ты сохранял в таком виде)
df = pd.read_csv("input.csv", sep=r"\s+")

# Список для хранения результатов
all_results = []
t_val = 1.5
t_delta = 0.1
a_val = 0.0
delta_a_val = 1.55334

# Группировка по (x, y)
for (x_val, y_val), group in df.groupby(['XCoord', 'YCoord'], sort=False):
    # Сортируем по t на всякий случай
    group_sorted = group.sort_values('T')

    # Разделяем: те, у кого t <= 1.5 — для интерполяции
    mask_interp = group_sorted['T'] <= t_val
    group_interp = group_sorted[mask_interp]
    group_rest = group_sorted[~mask_interp]

    # Сетка для интерполяции
    t_new = np.arange(0, t_val + 0.001, t_delta)


    # Интерполяция только если есть хотя бы 2 точки
    if len(group_interp) >= 2:
        v_new = np.interp(t_new, group_interp['T'], group_interp['V'])
        delta_v_new = np.interp(t_new, group_interp['T'], group_interp['DeltaV'])
        delta_a_new = np.interp(t_new, group_interp['T'], group_interp['DeltaA'])
        a_new = np.interp(t_new, group_interp['T'], group_interp['A'])

        df_interp = pd.DataFrame({
            'XCoord': x_val,
            'YCoord': y_val,
            'V': v_new,
            'A': a_new,
            'T': t_new,
            'DeltaV': delta_v_new,
            'DeltaA': delta_a_new
        })
    else:
        df_interp = group_interp  # если недостаточно точек — не интерполируем

    # Объединяем интерполированные и остальные точки
    group_final = pd.concat([df_interp, group_rest], ignore_index=True)
    all_results.append(group_final)

# Финальный DataFrame
df_result = pd.concat(all_results, ignore_index=True)

# Округляем до 3 знаков
df_result = df_result.round({'XCoord': 3, 'YCoord': 3, 'T': 3, 'A': 3, 'V': 3, 'DeltaV': 3, 'DeltaA': 3})

# Форматируем числа как строки с 3 знаками после запятой
df_result["T"] = df_result["T"].map("{:.3f}".format)
df_result["V"] = df_result["V"].map("{:.3f}".format)

# Вывод результата
print(df_result)

# Сохраняем в файл (по желанию)
df_result.to_csv("interpolated_output.csv", sep="\t", index=False)
