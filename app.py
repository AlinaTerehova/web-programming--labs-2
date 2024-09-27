from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect ('/menu', code=302)

@app.route("/menu")
def menu():
    return """

<!document>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    <head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <nav>
            <ul>
                <li><a href="/lab1">Первая лабораторная</a></li>
            </ul>
        </nav>

        <footer> 
            &copy; Алина Терехова, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
    """

@app.route("/lab1")
def lab1():
    return """
<!document>
<html>
    <head>
        <title> Терехова Алина Сергеевна, Лабораторная 1</title>
    <head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1></h1>
        <div>
        Flask — фреймворк для создания веб-приложений на языке программирования Python, использующий набор инструментов Werkzeug, а также шаблонизатор Jinja2. Относится к категории так называемых микрофреймворков — минималистичных каркасов веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        <div>

        <div>
            <a href='""" + url_for('menu') + """'>Меню</a>
        </div>

        <h2>Реализованные роуты</h2>
        <ul>
            <li><a href='""" + url_for('oak') + """'>/lab1/oak</a></li>
            <li><a href='""" + url_for('student') + """'>/lab1/student</a></li>
            <li><a href='""" + url_for('python') + """'>/lab1/python</a></li>
            <li><a href='""" + url_for('aqua') + """'>/lab1/aqua</a></li>
        </ul>

        <footer> 
            &copy; Алина Терехова, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
    """


@app.route("/lab1/oak")
def oak():
    return """

<!document>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
        <link rel="stylesheet" type="text/css" href='""" + url_for('static', filename='lab1.css') + """'>
    </head>
        <body>
            <h1>Дуб</h1>
            <img src='""" + url_for('static', filename='oak.jpg') + """'>
        </body>

</html>
    """

@app.route("/lab1/student")
def student():
    return """

<!document>
<html>
     <head>
        <title> Терехова Алина Сергеевна, Лабораторная 1</title>
    <head>
    <style> 
            body {
                font-family: 'Stem Text', sans-serif;
                background-color: white;
                color: black;
                display: flex;
                justify-content: center;
                align-items: center;            
                text-align: center;
                font-family: 'Stem Text';
            }
    </style>
    <body>
        <div>
            <h1>Терехова Алина Сергеевна</h1>
            <img src='""" + url_for('static', filename='logo.webp') + """'>
        <div>      
    </body>
</html>
    """

@app.route("/lab1/python")
def python():
    return """

<!document>
<html>
     <head>
        <title> Терехова Алина Сергеевна, Лабораторная 1</title>
    <head>
    <style> 
            body {
                font-family: 'Atial', sans-serif;
                background-color: white;
                color: black;
                margin: 20px;
                text-align: justify; 
                line-height: 1.6; 
                text-indent: 30px;
            }
    </style>
    <body>
        <div>
            <h1>Python</h1>
            <img src='""" + url_for('static', filename='python.webp') + """'>
            <p>
                Python — мультипарадигмальный высокоуровневый язык программирования общего назначения с 
                динамической строгой типизацией и автоматическим управлением памятью, ориентированный на повышение производительности разработчика, читаемости кода и его качества,
                  а также на обеспечение переносимости написанных на нём программ. Язык является полностью объектно-ориентированным в том плане, что всё является объектами. Необычной 
                  особенностью языка является выделение блоков кода отступами. Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает необходимость обращаться к 
                  документации. Сам же язык известен как интерпретируемый и используется в том числе для написания скриптов. Недостатками языка являются зачастую более низкая скорость
                    работы и более высокое потребление памяти написанных на нём программ по сравнению с аналогичным кодом, написанным на компилируемых языках, таких как C или C++.
            </p>
            <p>
                Python является мультипарадигменным языком программирования, поддерживающим императивное, процедурное, структурное, объектно-ориентированное программирование,
                  метапрограммирование, функциональное программирование, и асинхронное программирование. Задачи обобщённого программирования решаются за счёт динамической 
                  типизации. Аспектно-ориентированное программирование частично поддерживается через декораторы, более полноценная поддержка обеспечивается дополнительными 
                  фреймворками. Такие методики как контрактное и логическое программирование можно реализовать с помощью библиотек или расширений. Основные архитектурные черты —
                    динамическая типизация, автоматическое управление памятью, полная интроспекция, механизм обработки исключений, поддержка многопоточных вычислений с глобальной
                      блокировкой интерпретатора (GIL), высокоуровневые структуры данных. Поддерживается разбиение программ на модули, которые, в свою очередь, могут объединяться
                        в пакеты.
            </p>
            
        <div>      
    </body>
</html>
    """

@app.route("/lab1/aqua")
def aqua():
    return """
<!doctype html>
<html>
    <head>
        <title>Терехова Алина Сергеевна, Лабораторная 1</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background-color: white;
                color: black;
                padding: 20px;
                display: flex;
                justify-content: center;
                align-items: center;
                margin-top: 20px
                line-height: 1.6;
                text-indent: 30px;
            }
            h1 { 
                color: #00a4e8; 
                font-size: 60px;
            }
            .content {
                display: flex;
                justify-content: space-between; /* Разделить пространство между блоками */ 
            }
            .text-block {
                width: 70%; 
                padding: 20px;
            }
            .image-block {
                width: 30%; 
                padding: 20px;
            }
            p {
                text-align: justify;
            }
            img {
                height: 40%
            }
        </style>
        </head>
        <body>
            <div class="content">
                <div class="text-block">
                    <h1>BonAqua</h1>
                    <p>
                        BonAqua (рус. БонАква) — немецкая торговая марка, производитель бутилированной и минеральной питьевой воды. 
                        Основанный в 1988 году бренд BonAqua принадлежит корпорации «The Coca-Cola Company».
                    </p>

                    <p>
                        История бренда BonAqua началась в 1988 году в Германии. Продукция торговой марки изначально поставлялась 
                        в столовые, кафе и магазины Западной Германии под торговым обозначением Bonaqa. В 1989 году произошло объединение 
                        Германии, и практически сразу после этого Bonaqa начала экспансию в Европу. За несколько лет под разными именами — Bonaqua,
                        BonAqua и BonAqua Silver — вода появилась во многих европейских странах, а в 1994 году BonAqua добралась до России.
                    </p>
                    <p>
                        В 2004 году компания выпустила для европейского рынка несколько вариантов BonAqua с фруктовыми вкусами — яблоко-груша и 
                        апельсин-ананас. Позже, эти напитки появились в России под названием BonAqua Viva, и сейчас в этой линейке, обновленной 
                        в 2016 году, три вкуса — яблоко, лимон и лайм.
                    </p>
                    <p>
                        Компания Coca‑Cola Россия производит чистую питьевую воду на 10 заводах, рассредоточенных по всей стране.
                        Одно из основных производств находится в Московской области, в городе Истра. Всё начинается со скважин глубиной 
                        от 130 до 240 метров, у истринского завода их три. Путь воды от источника до линии розлива занимает 20 минут.
                    </p>
                    <p>
                        Классическая вода BonAqua на российском рынке представлена в двух видах — 
                        сильногазированная и негазированная. Воду разливают в стеклянные бутылки 0,33 л и пластиковые — от 0,5 л до 5 л.
                    </p>
                </div>
                <div class="image-block">
                    <img src='""" + url_for('static', filename='aqua.jpg') + """' alt="BonAqua">
                </div>
            </div>
        </body>

</html>
    """

@app.route('/lab2/a')
def a():
    return 'без слеша'

@app.route('/lab2/a/')
def a2():
    return 'со слешем'

flower_list = ['Роза', 'Тюльпан', 'Незабудка', 'Ромашка',]

@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return 'Такого цветка нет', 404
    else:
        return "Цветок: " + flower_list[flower_id]
    
@app.route('/lab2/add_flowers/<name>')
def add_flowers(name):
    flower_list.append(name)
    return f'''
<!doctype html>
<html>
    <body>
    <h1> Добавлен новый цветок </h1>
    <p> Название нового цветка: {name} </p>
    <p> Всего цветов: {len(flower_list)} </p>
    <p> Полный список: {flower_list} </p>
    </body>
</html>
'''

@app.route('/lab2/example')
def example():
    name, name_title, group, lab_num, number_course = 'Алина Терехова', 'Терехова Алина', 'ФБИ-24', 2, 3
    fruits = [
        {'name': 'Яблоки', 'price': 100},
        {'name': 'Груши', 'price': 120},
        {'name': 'Апельсины', 'price': 80},
        {'name': 'Мандарины', 'price': 95},
        {'name': 'Манго', 'price': 321},
    ]
    return render_template('example.html', name = name, group=group,
                           lab_num = lab_num, number_course=number_course, name_title=name_title,
                            fruits=fruits )
 
@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')