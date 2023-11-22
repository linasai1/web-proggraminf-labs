from flask import Blueprint, render_template,request, redirect
lab4 = Blueprint('lab4', __name__)

@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')


@lab4.route('/lab4/login/', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
         return render_template('login.html')   
    error = ''   
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    if not username:        
            error = 'Введите логин'
            return render_template('login.html', error=error, username=username, password=password)
    else: 
        if username != 'alex' and password != '123':
            error = 'Неверный логин и/или пароль' 
            return render_template('login.html', error=error, username=username, password=password)
        elif username != 'alex' and password == '123':
            error = 'Неверный логин'
            return render_template('login.html', error=error, username=username, password=password)
        elif password != '123' and username == 'alex':
            error = 'Неверный пароль'
            return render_template('login.html', error=error, username=username, password=password)
        elif not password:
            error = 'Введите пароль'
            return render_template('login.html', error=error, username=username, password=password)
        elif not username and not password:
            error = 'Введите пароль и логин'
            return render_template('login.html', error=error, username=username, password=password)
        else:
            return render_template ('password_success.html', error=error, 
                                        username=username, password=password)    
    return render_template('login.html', error=error)