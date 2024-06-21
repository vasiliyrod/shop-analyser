import pandas as pd
import numpy as np

# Устанавливаем количество записей в датасете
num_records = 1000

# Генерация данных
np.random.seed(44)
ids = np.arange(1, num_records + 1)

# Генерация полов с более реальным распределением
genders = np.random.choice(['Мужской', 'Женский'], size=num_records, p=[0.48, 0.52])

# Генерация возраста с различным распределением для полов
ages_male = np.random.normal(35, 15, size=num_records // 2).astype(int)
ages_female = np.random.normal(40, 15, size=num_records // 2).astype(int)
ages = np.concatenate([ages_male, ages_female])
ages = np.clip(ages, 10, 80)  # Ограничение возраста в диапазоне от 10 до 80

# Генерация дней недели с различным распределением
days_of_week = np.random.choice(
    ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'],
    size=num_records,
    p=[0.1, 0.1, 0.15, 0.15, 0.2, 0.15, 0.15]
)

# Генерация потраченной суммы с зависимостью от возраста
amounts_spent = np.random.normal(1000, 500, size=num_records) + (ages - 35) * 20
amounts_spent = np.round(np.clip(amounts_spent, 50, 5000), 2)  # Ограничение сумм в диапазоне от 50 до 5000

# Генерация времени покупки с различным распределением для возрастов
purchase_times = []
for age in ages:
    if age < 20:
        purchase_times.append(np.random.choice(pd.date_range('14:00', '20:00', freq='min').time))
    elif age < 40:
        purchase_times.append(np.random.choice(pd.date_range('10:00', '22:00', freq='min').time))
    else:
        purchase_times.append(np.random.choice(pd.date_range('08:00', '20:00', freq='min').time))

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
df.to_csv('data/grocery_store_data4.csv', index=False)

df.head()
