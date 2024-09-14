from flask import Flask, redirect, url_for
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