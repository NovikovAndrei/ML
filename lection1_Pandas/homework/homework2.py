import numpy as np
import pandas as pd


df = pd.read_csv('./kc_house_data.csv', sep=',')
print(df.head())

# Изучите типы данных

print(df.info())

# Найдите количество пропущенных ячеек в данных

missing_values = df.isna().sum()
print(missing_values)
total_missing_values = missing_values.sum()
print(f"Общее кол-во пропущенных ячеек: {total_missing_values}")

# Посчитайте основные статистики по всем признакам и поизучайте их

df_stat = df.describe()
print(df_stat)


# Пишите выводы:

# Цена (Price)

# Средняя цена домов составляет примерно 540,088 USD.
# Минимальная и максимальная цена составляет 75,000 USD и 7,700,000 USD соответственно, что показывает огромный разброс цен на дома.

# Количество спален (Bedrooms)

# Среднее количество спален в доме — примерно 3.37.
# Есть дом с максимальным количеством спален — 33, что достаточно много.

# Количество ванных комнат (Bathrooms)

# Среднее количество ванных комнат — 2.11.
# Дома имеют вариативность в количестве ванных комнат от 0 до 8 (что достаточно странно для домов с такой этажностью).

# Площадь дома и участка (sqft_living и sqft_lot)

# Средняя площадь жилой зоны составляет 2079.9 квадратных футов, а участка — 15107 квадратных футов.
# Минимальная и максимальная площадь жилой зоны — 290 и 13540 квадратных футов соответственно, что показывает большой диапазон размеров домов.

# Количество этажей (Floors)

# Среднее количество этажей в домах составляет примерно 1.49.
# Дома имеют от 1 до 3.5 этажей.

# Год постройки и реновации (yr_built и yr_renovated)

# Средний год постройки домов — 1971 год.
# Некоторые дома были отремонтированы, с наиболее недавней реновацией в 2015 году.

# Оценка состояния и класс (Condition и Grade)

# Среднее значение состояния домов — 3.4, на шкале от 1 до 5, что говорит о хорошем состоянии большинства домов.
# Средний класс домов — 7.65, на шкале от 1 до 13, указывая на довольно высокий средний уровень класса домов.

# В каком диапазоне изменяются стоимости недвижимости?

min_price = df['price'].min()
max_price = df['price'].max()
print(min_price, max_price)

# # Какую долю в среднем занимают жилая площадь от всей площади по всем домам?

df['living_to_lot_ratio'] = df['sqft_living'] / df['sqft_lot']

average_living_to_lot_ratio = df['living_to_lot_ratio'].mean()
print(average_living_to_lot_ratio)

# Как много домов с разными этажами в данных?

unic_floors = df['floors'].value_counts()
print(unic_floors)
print(unic_floors.count())

# Насколько хорошее состояния у домов в данных?

df_condition = df['condition'].value_counts()
print(df_condition)
print(f"среднее состояние домов - {df['condition'].mean()}")

condition_stats = df['condition'].describe()
print(condition_stats)

# Найдите года, когда построили первый дом, когда построили последний дом в данных?

df_built = df['yr_built']
df_built_first = df_built.min()
df_built_last = df_built.max()
print(f'самый старый дом - {df_built_first}, самый новый дом - {df_built_last}')

# Сколько в среднем стоят дома, у которых 2 спальни?

two_bedrooms_houses = df[df['bedrooms'] == 2]
two_bedrooms_houses_count = (df['bedrooms'] == 2).sum()
print(two_bedrooms_houses_count)
print(two_bedrooms_houses)

print(two_bedrooms_houses['price'].mean())

# Какая в среднем общая площадь домов, у которых стоимость больше 600 000?

price_more_600000 = df[df['price'] > 600000]

average_total_area = (price_more_600000['sqft_living'] + price_more_600000['sqft_basement']).mean()
print(average_total_area)

# Как много домов коснулся ремонт?

renovated_houses = df[~(df['yr_renovated'] == 0)]
print(renovated_houses['id'].count())
print(renovated_houses.shape[0])

# Насколько в среднем стоимость домов с оценкой grade выше 10 отличается от стоимости домов с оценкой grade меньше 4?

grade_more_10 = df[df['grade'] > 10]
grade_less_4 = df[df['grade'] < 4]

average_price_more_10 = grade_more_10['price'].mean()
average_price_less_4 = grade_less_4['price'].mean()

print(average_price_more_10 - average_price_less_4)

# Выберите дом клиенту. Клиент хочет дом с видом на набережную, как минимум с тремя ванными и с подвалом. Сколько вариантов есть у клиента?

result = df[(df['waterfront'] == 1) & (df['bathrooms'] >= 3) & (df['sqft_basement'] > 0)]
print(result)
print(result.shape[0])

# Выберите дом клиенту. Клиент хочет дом либо с очень красивым видом из окна, либо с видом на набережную,
# в очень хорошем состоянии и год постройки не меньше 1980 года. В какой ценовом диапазоне будут дома?

result = df[((df['view'] == 4) | (df['waterfront'] == 1)) & (df['condition'] == 5) & (df['yr_built'] >= 1980)]
print(f"Ценовой диапазон от {result['price'].min()} до {result['price'].max()}")

# Выберите дом клиенту. Клиент хочет дом без подвала, с двумя этажами, стоимостью до 150000.
# Какая оценка по состоянию у таких домов в среднем?

result = df[(df['sqft_basement'] == 0) & (df['floors'] == 2) & (df['price'] <= 150000)]
print(result['condition'].mean())