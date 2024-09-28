from flask import Flask, redirect, url_for
from lab1 import lab1
from lab2 import lab2

app = Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)

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
                <li><a href="/lab2">Вторая лабораторная</a></li>
            </ul>
        </nav>

        <footer> 
            &copy; Алина Терехова, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
    """


@app.errorhandler(404)
def not_found(err):
    css_err = url_for("static", filename="err.css")
    img_err = url_for("static", filename="404.png")
    return f'''
        <!doctype html>
        <html>
            <head>
                <title>Страница не найдена</title>
                <link rel="stylesheet" href="{css_err}">
            </head>
            <body>
                <h1>Страница не найдена</h1>
                <p>К сожалению, запрашиваемая Вами страница не была найдена.</p>
                <p>Вы можете перейти на <a href="/">главную страницу</a> или попробовать воспользоваться поиском.</p>
                <img src="{img_err}">
            </body>
        </html>''', 404


@app.errorhandler(500)
def server_error(err):
    return '''
        <!doctype html>
        <html>
            <head>
                <title>Внутренняя ошибка сервера</title>
            </head>
            <body>
                <h1>Произошла внутренняя ошибка сервера</h1>
                <p>
                    Приносим свои извинения за неудобства. Пожалуйста, попробуйте обновить страницу или вернуться позже.
                </p>
            </body>
        </html>''', 500