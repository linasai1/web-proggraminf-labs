from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return """
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

            <main>
                <ol>
                    <li>
                        <a href="/lab1" target="_blank">Лабораторная работа 1</a>
                    </li>
                </ol>
            </main>

            <footer>
                &copy; Сайфулина Алина, ФБИ-13, 3 курс, 2023
            </footer>
        </body>
    </html>
    """

@app.route("/lab1")
def lab1():
    return """
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

            <main>
                <div>
                    Flask — фреймворк для создания веб-приложений на языке программирования Python, использующий набор инструментов Werkzeug, 
                    а также шаблонизатор Jinja2. Относится к категории так называемых микрофреймворков — минималистичных каркасов веб-приложений, 
                    сознательно предоставляющих лишь самые базовые возможности.
                </div>
            </main>

            <footer>
                &copy; Сайфулина Алина, ФБИ-13, 3 курс, 2023
            </footer>
        </body>
    </html>
    """
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

