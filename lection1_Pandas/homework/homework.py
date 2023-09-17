import pandas as pd

# Загрузить, посмотреть, определить количество строк и объединить 3 датасета:
# marketing_campaign.csv, users.csv и subscribers.csv.

df_marketing_campaign = pd.read_csv('./marketing_campaign.csv', sep=',')
print(f"Количество строк в датасете 'marketing_campaign.csv' = {df_marketing_campaign.shape[0]}")

df_users = pd.read_csv('./users.csv', sep=',')
print(f"Количество строк в датасете 'users.csv' = {df_users.shape[0]}")

df_subscribers = pd.read_csv('./subscribers.csv', sep=',')
print(f"Количество строк в датасете 'subscribers.csv' = {df_subscribers.shape[0]}")

df_general = df_marketing_campaign.merge(df_users, on='user_id').merge(df_subscribers, on='user_id')

# Определить типы и статистики колонок

print(f"\nТипы колонок в объединенном датафрейме:\n\n{df_general.dtypes}")  # определение типов колонок

df_general_describe = df_general.describe(include='all')  # определение статистик колонок

print(f"\nОпределение статистик колонок:\n\n{df_general_describe}")

# Определить эффективность маркетинговых каналов по привлечению платящих игроков

df_channel_effective = df_general.groupby('marketing_channel').agg(
    total_users=('user_id', 'count'),
    total_converted=('converted', 'sum'),
)

df_channel_effective['conversion_rate'] = \
    (df_channel_effective['total_converted'] / df_channel_effective['total_users']) * 100

print(f"\nЭффективность маркетинговых каналов:\n{df_channel_effective['conversion_rate']}")

# Определить количество игроков в каждой возрастной группе

df_general_users_for_age = df_general.groupby('age_group').agg(total_users=('user_id', pd.Series.nunique))
print(f"\nКоличество игроков по возрастным группам:\n{df_general_users_for_age}")

# Определить самую раннюю дату подписки на сервис

df_general['date_subscribed'] = pd.to_datetime(df_general['date_subscribed'], format='%m/%d/%y')
earliest_subscribe_date = df_general['date_subscribed'].min()
print(f"\nСамая ранняя дата подписки на сервис: {earliest_subscribe_date}")

# Определить портрет аудитории удержанных подписчиков (по возрасту и языку)

df_general_retained = df_general[df_general['is_retained'] == 1].groupby(['age_group', 'language_preferred']).agg(
    total_retained_users=('user_id', pd.Series.nunique)
)

total_retained_users = df_general[df_general['is_retained'] == 1]['user_id'].nunique()

age_group_totals = df_general_retained.groupby('age_group')['total_retained_users'].transform('sum')

df_general_retained['percentage_within_age_group'] = \
    (df_general_retained['total_retained_users'] / age_group_totals) * 100
df_general_retained['language_preferred_rate'] = \
    (df_general_retained['total_retained_users'] / total_retained_users) * 100

print(f"\n Портрет аудитории удержанных подписчиков:\n{df_general_retained}")
