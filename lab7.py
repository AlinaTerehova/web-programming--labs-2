from flask import Blueprint, render_template, abort, request, jsonify
from datetime import datetime

lab7 = Blueprint('lab7', __name__)

@lab7.route('/lab7/')
def lab():
    return render_template('lab7/lab7.html')

films = [
    {
        "title": "The Intern",
        "title_ru": "Стажер",
        "year": 2015,
        "description": "70-летний вдовец Бен Уитакер обнаруживает, \
         что выход на пенсию — еще не конец. Пользуясь случаем, он становится\
           старшим стажером в интернет-магазине модной одежды под руководством Джулс Остин."
    },
    {
        "title": "Dead Poets Society",
        "title_ru": "Общество мёртвых поэтов",
        "year": 1989,
        "description": "Джон Китинг — новый преподаватель английской словесности в \
        консервативном американском колледже. От чопорной массы учителей его выгодно \
        отличают легкость общения, эксцентричное поведение и пренебрежение к программе \
        обучения. Однажды он посвящает своих подопечных в тайну Общества мёртвых поэтов.\
        С этого момента каждый из учеников старается обрести свой собственный голос в \
        безликом хоре, взглянуть на окружающий мир, высоко подпрыгнув над серой школьной оградой."
    },
    {
        "title": "A Beautiful Mind",
        "title_ru": "Игры разума",
        "year": 2001,
        "description": "От всемирной известности до греховных глубин — все это познал на своей \
        шкуре Джон Форбс Нэш-младший. Математический гений, он на заре своей карьеры сделал\
        титаническую работу в области теории игр, которая перевернула этот раздел математики\
        и практически принесла ему международную известность. Однако буквально в то же время \
        заносчивый и пользующийся успехом у женщин Нэш получает удар судьбы, который переворачивает уже его собственную жизнь."
    },
    {
        "title": "The Imitation Game",
        "title_ru": "Игра в имитацию",
        "year": 2014,
        "description": "Английский математик и логик Алан Тьюринг пытается взломать код немецкой шифровальной машины Enigma во время Второй мировой войны."
    },
    {
        "title": "The Silence of the Lambs",
        "title_ru": "Молчание ягнят",
        "year": 1991,
        "description": "Психопат похищает и убивает молодых женщин по всему Среднему Западу. ФБР, уверенное, что все преступления \
        совершены одним и тем же человеком, поручает агенту Клариссе Старлинг встретиться с заключенным-маньяком Ганнибалом \
        Лектером, который мог бы помочь составить психологический портрет убийцы. Сам Лектер отбывает наказание за убийства и каннибализм. Он согласен помочь Клариссе лишь в том случае, если она попотчует его больное воображение подробностями своей личной жизни."
    }
]

@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return jsonify(films)

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    if id < 0 or id >= len(films):
        abort(404)
    return jsonify(films[id])

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    if id < 0 or id >= len(films):
        abort(404)
    del films[id]
    return '', 204

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    if id < 0 or id >= len(films):
        abort(404)

    film = request.get_json() 

    if film.get('description', '') == '':
        return jsonify({'description': 'Заполните описание'}), 400
    elif len(film['description']) > 2000:
        return jsonify({'description': 'Описание не должно превышать 2000 символов'}), 400

    if not film.get('title') and not film.get('title_ru'):
        return jsonify({'title': 'Заполните поля с названиями'}), 400
    if not film.get('title_ru'):
        return jsonify({'title_ru': 'Заполните русское название'}), 400
    if film.get('title', '') == '':
        film['title'] = film['title_ru']

    if not film.get('year'):
        return jsonify({'year': 'Укажите год выпуска фильма'}), 400
    elif not str(film['year']).isdigit() or int(film['year']) < 1895 or int(film['year']) > 2100:
        return jsonify({'year': 'Введите корректный год (1800-2100)'}), 400
        
    films[id] = film
    return jsonify(films[id])

@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_film():
    film = request.get_json()
    if not film:
        abort(400)
  
    if film.get('description', '') == '':
        return jsonify({'description': 'Заполните описание'}), 400
    elif len(film['description']) > 2000:
        return jsonify({'description': 'Описание не должно превышать 2000 символов'}), 400

    if not film.get('title') and not film.get('title_ru'):
        return jsonify({'title': 'Заполните поля с названиями'}), 400
    if not film.get('title_ru'):
        return jsonify({'title_ru': 'Заполните русское название'}), 400
    
    if film.get('title', '') == '':
        film['title'] = film['title_ru']

    if not film.get('year'):
        return jsonify({'year': 'Укажите год выпуска фильма'}), 400
    elif not str(film['year']).isdigit() or int(film['year']) < 1895 or int(film['year']) > 2100:
        return jsonify({'year': 'Введите корректный год (1800-2100)'}), 400
  

    films.append(film)
    return jsonify(film), 201
