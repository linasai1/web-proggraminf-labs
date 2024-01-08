from flask import  Blueprint, redirect, url_for, render_template
lab1 = Blueprint('lab1', __name__)


@lab1.route("/")
@lab1.route("/index")
def start():
    return redirect("/menu", code=302)


@lab1.route("/menu")
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

            <h1>
                <a href="/lab3">Лабораторная работа 3</a>
            </h1>

            <h1>
                <a href="/lab4">Лабораторная работа 4</a>
            </h1>

            <h1>
                <a href="/lab5">Лабораторная работа 5</a>
            </h1>

            <footer>
                &copy; Сайфулина Алина, ФБИ-13, 3 курс, 2023
            </footer>
        </body>
    </html>
    '''

@lab1.route("/lab1")
def lab():
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


@lab1.route('/lab1/oak')
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


@lab1.route('/lab1/student')
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

@lab1.route('/lab1/python')
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


@lab1.route ('/lab1/EQ')
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
