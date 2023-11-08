from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return '''
    <!doctype html>
    <html>
        <head>
            <title>НГТУ, ФБ, Лабораторные работы</title>
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        </head>
        <body>
            <header>
                НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных.
            </header>
            <h1>
                <a href="/lab1">Лабораторная работа 1</a>
            </h1>

            <h1>
                <a href="/lab2">Лабораторная работа 2</a>
            </h1>

            <footer>
                &copy; Сайфулина Алина, ФБИ-13, 3 курс, 2023
            </footer>
        </body>
    </html>
    '''

@app.route("/lab1")
def lab1():
    return '''
    <!doctype html>
    <html>
        <head>
            <title>Сайфулина Алина Витальевна, Лабораторная 1</title>
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        </head>
        <body>
            <header>
                НГТУ, ФБ, Лабораторная работа 1
            </header>
            <h1>
                Web-сервер на flask
            </h1>
            <p>
                    Flask — фреймворк для создания веб-приложений на языке программирования Python, использующий набор инструментов Werkzeug, 
                    а также шаблонизатор Jinja2. Относится к категории так называемых микрофреймворков — минималистичных каркасов веб-приложений, 
                    сознательно предоставляющих лишь самые базовые возможности.
            </p>
                <div><a href="/menu">Меню</a></div>
                <h2>Реализованные роуты</h2>
                <div><a href="/lab1/oak">/lab1/oak - Дуб</a></div>
                <div><a href="/lab1/student">/lab1/student - Студент</a></div>
                <div><a href="/lab1/python">/lab1/python - Python</a></div>
                <div><a href="/lab1/EQ">/lab1/EQ - Эмоциональный интеллект</a></div>
            <footer>
                &copy; Сайфулина Алина, ФБИ-13, 3 курс, 2023
            </footer>
        </body>
    </html>
    '''
@app.route('/lab1/oak')
def oak ():
    return '''
    <!doctype html>
    <html>
        <head> 
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        </head>
        <body>
            <h1> Дуб </h1>
            <img src="''' + url_for('static', filename='oak.jpg') + '''">
        </body>
    </html>
    '''
@app.route('/lab1/student')
def student ():
    return '''
    <!doctype html>
    <html>
        <head> 
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        </head>
        <body>
            <h1> Сайфулина Алина Витальевна </h1>
            <img src="''' + url_for('static', filename='nstu.jpg') + '''">
        </body>
    </html>
    '''

@app.route('/lab1/python')
def python ():
    return '''
    <!doctype html>
    <html>
        <head> 
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        </head>
        <body>
            <div>Python — это язык программирования, который широко используется в интернет-приложениях, разработке программного обеспечения,<br> 
            науке о данных и машинном обучении (ML). Разработчики используют Python, потому что он эффективен, прост в изучении и работает<br>
            на разных платформах.</div>
            <div>Программы на языке Python можно скачать бесплатно, они совместимы со всеми типами систем и повышают скорость разработки. </div>
            <img src="''' + url_for('static', filename='python.jpg') + '''">
        </body>
    </html>
    '''
@app.route ('/lab1/EQ')
def EQ ():
    return '''
    <!doctype html>
    <html>
        <head> 
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        </head>
        <body>
        <div> Эмоциональный интеллект (EQ) — это способность личности осознавать и понимать свои эмоции и чувства других людей<br>
        и использовать эти навыки во взаимодействии с окружающими.</div>
        <div> В практическом смысле это совокупность навыков, благодаря которым человек понимает, что его эмоции могут управлять<br>
        его поведением и влиять на окружающих — причем не только позитивно, но и негативно. В английском языке для обозначения<br> 
        эмоционального интеллекта по аналогии с IQ используется аббревиатура EQ — «emotional quotient», или «эмоциональный коэффициент»,<br>
        а также сокращение EI — «emotional intelligence». </div>
        <img src="''' + url_for('static', filename='eq.png') + '''">
        </body>
    </html>
    '''
@app.route('/lab2/')
def lab():
    return render_template('lab2.html') 
    
@app.route('/lab2/example')
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


@app.route('/lab2/cars/')
def puppys():
    return render_template('cars.html') 
    