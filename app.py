import dash
from dash import dcc, html, Input, Output, State
import plotly.express as px
import pandas as pd
import base64
import io
import datetime

# Создание приложения Dash
app = dash.Dash(__name__)

# Описание макета приложения
app.layout = html.Div(className='container', children=[

    html.H1("Анализ данных продуктового магазина"),

    # Загрузка файла
    html.Div(className='upload-data', children=[
        dcc.Upload(
            id='upload-data',
            children=html.Div(['Перетащите или ', html.A('выберите файл')]),
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin-top': '10px',
                'margin-bottom': '10px',
                'background-color': '#e9ecef'
            },
            multiple=False
        ),
        html.Div(id='output-data-upload')
    ]),
    # таблица датасета
    html.Div(className='graph', children=[
        html.Div(id='show-dataset')
    ]),

    # "мужчина-женщина" круговая
    html.Div(className='graph', children=[
        html.H2("Мужчина-Женщина"),
        dcc.Graph(id='gender-dist')
    ]),

    # "возраст" столбчатая
    html.Div(className='graph', children=[
        html.H2("Возраст"),
        dcc.Graph(id='age-dist')
    ]),

    # "дни недели" столбчатая
    html.Div(className='graph', children=[
        html.H2("Дни недели"),
        dcc.Graph(id='day-dist')
    ]),

    # "вывод" столбчатая
    html.Div(className='graph', children=[
        html.H2("Вывод"),
        dcc.Graph(id='amount-by-age-gender')
    ]),

    html.Div(className='footer', children=[
        "Copyright © Змеееды, 2024. Никакие права не защищены."
    ])
])


def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            df = pd.read_excel(io.BytesIO(decoded))
        else:
            return html.Div(['Недопустимый формат файла. Пожалуйста, загрузите файл в формате CSV или Excel.'])

        return df
    except Exception as e:
        print(e)
        return html.Div(['Произошла ошибка при обработке файла.'])


@app.callback(
    Output('output-data-upload', 'children'),
    Output('gender-dist', 'figure'),
    Output('age-dist', 'figure'),
    Output('day-dist', 'figure'),
    Output('amount-by-age-gender', 'figure'),
    Output('show-dataset', 'children'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename'),
    State('upload-data', 'last_modified'))
def update_output(contents, filename, date):
    if contents is not None:
        df = parse_contents(contents, filename, date)
        df1 = df

        age_bins = [0, 18, 25, 35, 60, 100]
        age_labels = ['<18', '18-25', '26-35', '36-60', '60+']
        df['Возрастная группа'] = pd.cut(df['Возраст'], bins=age_bins, labels=age_labels, right=False)
        df.sort_values(by='Возрастная группа', inplace=True)

        color_map = {'Мужской': 'blue', 'Женский': 'red'}
        age_color = ['yellow']

        gender_fig = px.pie(df, names='Пол', color='Пол', color_discrete_map=color_map)
        age_fig = px.histogram(df, x='Возрастная группа', color_discrete_sequence=age_color)
        day_fig = px.histogram(df, x='День недели', category_orders={
            'День недели': ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']})
        amount_fig = px.histogram(df, x='Возрастная группа', y='Потраченная сумма', color='Пол', barmode='group',
                                  title='Потраченная сумма по возрасту и полу', color_discrete_map=color_map)

        return (html.Div([
            html.H5(filename),
            html.H6(datetime.datetime.fromtimestamp(date))]),
                gender_fig,
                age_fig,
                day_fig,
                amount_fig,
                generate_table(df1))

    return html.Div(['Пожалуйста, загрузите файл.']), {}, {}, {}, {}


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


# Запуск приложения
if __name__ == '__main__':
    app.run_server(debug=True)
