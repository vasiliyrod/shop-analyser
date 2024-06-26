<h2 align="center"><strong> ФЕДЕРАЛЬНОЕ ГОСУДАРСТВЕННОЕ 
<br>ОБРАЗОВАТЕЛЬНОЕ УЧРЕЖДЕНИЕ ВЫСШЕГО ОБРАЗОВАНИЯ
<br>«НАЦИОНАЛЬНЫЙ ИССЛЕДОВАТЕЛЬСКИЙ УНИВЕРСИТЕТ
<br>"ВЫСШАЯ ШКОЛА ЭКОНОМИКИ"»</strong></h2>
<br><br>
<h3 align="center">Московский институт электроники и математики
<br>им. А.Н. Тихонова НИУ ВШЭ</h3>
<h3 align="center">Департамент компьютерной инженерии
<br>Курс: Python в науке данных</h3>
<br>
<h2 align="center"><strong>Поиск целевой аудитории магазина</strong></h2>
<h4 align="center">Над проектом работали студенты БИВ237:
<br><i>Чашкин Фёдор Борисович
<br>Родманич Василий Александрович
<br>Коршун Владислав Игоревич</i></h4>
<br>
<h4 align="center">Научный руководитель:
<br><i>Ролич Алексей Юрьевич</i></h4>
<br><br>
<p align="center">МОСКВА 2024</p>

---

# Программа по поиску целевой аудитории магазина

## Описание программы
Пользователь загружает файл с данными о покупках в магазине. Он должен иметь следующий вид (описание датасета):

* id — номер транзакции;
* gender — пол покупателя;
* age — возраст покупателя;
* week_day — день недели, в который была совершена транзация;
* amount — сумма покупки;
* time — время, в которое была совершена транзация.

На основе этих данных программа вычисляет целевую аудиторию магазина, строит графики и диаграммы,
чтобы на основе их анализа сделать соответствующий вывод:
кто тратит больше денег (мужчины или женщины),
когда они это делают (день недели, в который совершается наибольшее число транзакций) и как много денег тратят.

## Минимальные требования
Для корректной работы программы понадобится браузер любой операционной системы и стабильное интернет-соединение.
Устанавливать программу и какие-либо дополнительные компоненты не требуется.

## Установка и открытие программы
Приложение развёрнуто на сервере, поэтому установка дополнительных программ не предусмотрено.
Пользователю достаточно зайти на сайт в любом удобном ему браузере:<br>
```
http://0agresiiman.ru/python
```
<br>После чего можно быть готовым к использованию приложения.

## Запуск программы
Программа открывается при помощи соответствующей ссылки (см. раздел `Установка и открытие программы`).
<br>Для дальнейшей работы необходимо выполнить несколько простых шагов:
1. Ознакомиться с интерфейсом, прочитать описание программы;
2. Нажать на кнопку `Выберите или загрузите файл`;
3. В появившемся окне выбрать требуемый для анализа файл датасета;
4. Загрузить датасет на сайт;
5. Ознакомиться с появившейся таблицей датасета (сверить данные и
убедиться при необходимости в том, что файл был загружен корректно);
6. Ознакомиться с соответствующими диаграммами и графиками, анализирующими целевую аудиторию магазина.

---

# Общее описание функциональности разработанного ПО

Программное обеспечение предназначено для анализа покупательского поведения и определения целевой аудитории магазина.
Оно позволяет пользователям загружать датасеты с данными о покупках и автоматически обрабатывает эти данные
для создания информативных графиков и диаграмм.

## Ключевые функции

- **Загрузка данных**: Пользователи могут загружать файлы с данными о покупках, которые включают информацию о
транзакциях, поле и возрасте покупателей, времени и сумме покупок.
- **Анализ данных**: Программа анализирует загруженные данные и вычисляет ключевые метрики, такие как
общая сумма покупок, средний чек, распределение покупок по дням недели и полу.
- **Визуализация данных**: На основе анализа данных программа строит графики и диаграммы, позволяющие
визуально оценить покупательское поведение.
- **Определение целевой аудитории**: Программа делает общий вывод и помогает определить,
какие группы покупателей являются наиболее активными и прибыльными для магазина.

## Преимущества использования

Почему стоит пользоваться этим приложением? Востребованность данного продукта обусловлена рядом причин:

- **Простота использования**: Интуитивно понятный интерфейс и простой процесс загрузки данных
делают программу доступной для пользователей без специальных технических навыков.
- **Доступность**: Программа не требует установки дополнительных компонентов: у неё минимальные системные требования.
- **Экономия времени**: Автоматизация процесса анализа данных сокращает время, необходимое для получения результатов.
- **Поддержка принятия решений**: Визуализированные данные предоставляют ценную информацию для стратегического планирования и маркетинговых кампаний.

## Типичные сценарии использования

- **Маркетинговый анализ**: Определение наиболее прибыльных сегментов аудитории для нацеливания рекламных кампаний.
- **Оптимизация ассортимента**: Анализ покупательского поведения для определения наиболее популярных товаров и услуг.
- **Планирование акций**: Планирование маркетинговых акций и скидок на основе данных о наиболее активных днях недели и времени суток.

# Взаимодействие пользователя с системой

При заходе на сайт пользователь увидит следующую картину:

![Стартовая страница](https://i.ibb.co/YZ4jNkZ/image.png)

Далее программа попросит его загрузить датасет. При нажатии кнопки **«Перетащите или выберите файл»**
вылезет всплывающее окно:

![Перетащите или выберите файл](https://i.ibb.co/z6RrF2J/image.png)

При выборе нужного датасета программа выведет первые десять строк, чтобы пользователь
убедился, что данные считались корректно:

![Датасет](https://i.ibb.co/mhnDdPS/image.png)

Прокрутив страницу вниз, пользователь обнаружит остальные диаграммы, которые определяют
целевую аудиторию магазина:

![Диаграммы](https://i.ibb.co/PxkWVGk/image.png)