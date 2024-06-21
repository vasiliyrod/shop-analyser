import pandas as pd
import numpy as np

# Устанавливаем количество записей в датасете
num_records = 1000

# Генерация данных
np.random.seed(42)
ids = np.arange(1, num_records + 1)
genders = np.random.choice(['Мужской', 'Женский'], size=num_records)
ages = np.random.randint(10, 80, size=num_records)
days_of_week = np.random.choice(['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'], size=num_records)
amounts_spent = np.round(np.random.uniform(50, 5000, size=num_records), 2)
purchase_times = np.random.choice(pd.date_range('08:00', '22:00', freq='T').time, size=num_records)

# Создаем DataFrame
df = pd.DataFrame({
    'ID': ids,
    'Пол': genders,
    'Возраст': ages,
    'День недели': days_of_week,
    'Потраченная сумма': amounts_spent,
    'Время покупки': purchase_times
})

# Сохраняем DataFrame в CSV файл
df.to_csv('data/grocery_store_data.csv', index=False)

df.head()
