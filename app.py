import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Загрузка датасета
df = pd.read_csv('data/grocery_store_data.csv')

# Создание возрастных групп
age_bins = [0, 18, 25, 35, 60, 100]
age_labels = ['<18', '18-25', '26-35', '36-60', '60+']
df['Возрастная группа'] = pd.cut(df['Возраст'], bins=age_bins, labels=age_labels, right=False)

# Упорядочиваем столбец 'Возрастная группа' по возрастанию
df.sort_values(by='Возрастная группа', inplace=True)

# Создание приложения Dash
app = dash.Dash(__name__)

# Описание макета приложения
app.layout = html.Div(className='container', children=[
    html.H1("Анализ данных продуктового магазина"),

    # Первая диаграмма: "мужчина-женщина", круговая
    html.Div(className='graph', children=[
        html.H2("Мужчина-Женщина"),
        dcc.Graph(
            id='gender-dist',
            figure=px.pie(df, names='Пол', title='Мужчина-Женщина')
        )
    ]),

    # Вторая диаграмма: "возраст", столбчатая
    html.Div(className='graph', children=[
        html.H2("Возраст"),
        dcc.Graph(
            id='age-dist',
            figure=px.histogram(df, x='Возрастная группа', title='Возраст')
        )
    ]),

    # Третья диаграмма: "дни недели", столбчатая
    html.Div(className='graph', children=[
        html.H2("Дни недели"),
        dcc.Graph(
            id='day-dist',
            figure=px.histogram(df, x='День недели', title='Дни недели', category_orders={'День недели': ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']})
        )
    ]),

    # Четвёртая диаграмма: "вывод", столбчатая
    html.Div(className='graph', children=[
        html.H2("Вывод"),
        dcc.Graph(
            id='amount-by-age-gender',
            figure=px.histogram(df, x='Возрастная группа', y='Потраченная сумма', color='Пол', barmode='group', title='Потраченная сумма по возрасту и полу')
        )
    ]),

    html.Div(className='footer', children=[
        "Разработано с использованием Dash и Plotly"
    ])
])

# Запуск приложения
if __name__ == '__main__':
    app.run_server(debug=True)
