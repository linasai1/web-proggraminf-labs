from flask import  Blueprint, redirect, url_for
lab2 = Blueprint('lab2', __name__)


@lab2.route('/lab2/')
def lab():
    return render_template('lab2.html') 


@lab2.route('/lab2/example')
def example():
    name = 'Алина Сайфулина'
    numCour = '3'
    group = 'ФБИ-13'
    labNum = '2'

    fruits = [
        {'name': 'яблоки', 'price': 100}, 
        {'name': 'груши', 'price': 120}, 
        {'name': 'апельсины', 'price': 80}, 
        {'name': 'мандарины', 'price': 95}, 
        {'name': 'манго', 'price': 321}
        ]
    books = [
        {'authorName' : 'Ф.М. Достоевский', 'bookName' : 'Преступление и наказание', 'kind': 'Роман', 'pages': 500},
        {'authorName' : 'И.С. Тургенев', 'bookName' : 'Муму', 'kind': 'Рассказ', 'pages': 257},
        {'authorName' : 'Эрих Мария Ремарк', 'bookName' : 'Три товарища', 'kind': 'Роман', 'pages': 387},
        {'authorName' : 'Л.Н. Толстой', 'bookName' : 'Воскресение', 'kind': 'Роман', 'pages':367 },
        {'authorName' : 'М. Булгаков', 'bookName' : 'Мастер и Маргарита', 'kind': 'Роман', 'pages': 623},
        {'authorName' : 'М.Ю. Лермонтов', 'bookName' : 'Герой нашего времени', 'kind': 'Роман', 'pages': 267},
        {'authorName' : 'А.С. Пушкин', 'bookName' : 'Капитанская дочка', 'kind': 'Роман', 'pages':144 },
        {'authorName' : 'В.В. Набоков', 'bookName' : 'Лолита', 'kind': 'Роман', 'pages': 367},
        {'authorName' : 'Даниэль Дефо', 'bookName' : 'Робинзон Крузо', 'kind': 'Роман', 'pages': 1000},
        {'authorName' : 'Н.В. Гоголь', 'bookName' : 'Мертвые души', 'kind': 'Роман', 'pages': 627}
        ]
    return render_template('example.html', name = name, numCour = numCour, group = group, labNum = labNum, fruits = fruits, books = books) 


@lab2.route('/lab2/cars/')
def puppys():
    return render_template('cars.html') 
    