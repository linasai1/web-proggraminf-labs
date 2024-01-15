from flask import Blueprint, render_template,request, redirect, session, Flask, abort
from werkzeug.security import check_password_hash, generate_password_hash 
from Db.models import users, articles
from flask_login import login_user, login_required, current_user, logout_user
import psycopg2
from Db import db


lab6 = Blueprint('lab6', __name__)


@lab6.route('/lab6/')
def lab():
    visibleUser = session.get ('username','Anon')
    return render_template('general6.html', username=visibleUser)


@lab6.route('/lab6/check/')
def main():
    my_users = users.query.all()
    print (my_users)
    return 'result in console!'

@lab6.route('/lab6/checkarticles/')
def actickls():
    articles_check = articles.query.all()
    print(articles_check)
    return 'result in console!'

@lab6.route('/lab6/register/', methods = ['GET', 'POST'])
def register():
    error = []
    if request.method == 'GET':
        return render_template ('register.html')
    username_form = request.form.get('username')
    password_form = request.form.get('password')

    if not username_form:
        error.append('Заполните все поля') 
    elif len(password_form) <5:
        error.append('Длина пароля должна быть более 5 символов')
        return render_template('register.html', error=error)
   
    isUserExist = users.query.filter_by(username=username_form).first()
    
    if isUserExist is not None:
        error = 'Пользователь с таким именем уже существует'
        return render_template ('register.html', error=error)
    
    hashedPswd = generate_password_hash(password_form, method = 'pbkdf2')
    newUser = users(username=username_form, password=hashedPswd)

    db.session.add(newUser)
    db.session.commit()

    return redirect ('/lab6/login6/')


@lab6.route('/lab6/login6/', methods = ['GET', 'POST'])
def login():
    error = []

    if request.method == 'GET':
        return render_template('login6.html')
    username_form = request.form.get('username')
    password_form = request.form.get('password')
    
    my_user = users.query.filter_by(username=username_form).first()
    user_password = users.query.filter_by(password=password_form).first()

    if not (username_form and password_form):
        error.append('Заполните все поля')
        return render_template('login6.html', error=error)
    if my_user is not None:
        if check_password_hash(my_user.password, password_form):
            login_user(my_user, remember=False)
            return redirect('/lab6/articles/')
        return render_template('login6.html', error=error)
    if my_user is None:
        error.append("Пользователь не существует")
        return render_template("login6.html", my_user=my_user, error=error)
    
    if  user_password is None:
        error.append("Неправильный пароль")
        return render_template("login6.html", user_password=user_password, error=error)
    
    return render_template("login6.html")


@lab6.route('/lab6/articles/')
@login_required
def articles_list():
    username_form=request.form.get('username')
    my_articles = articles.query.filter_by(user_id=current_user.id).all()
    return render_template('user_articles.html', articles=my_articles, username_form=username_form)

@lab6.route("/lab6/new_article/", methods=["GET", "POST"])
@login_required
def createArticle():
    if request.method == "GET":
        return render_template("new_article.html")
    article_text = request.form.get("article_text")
    title = request.form.get("article_title")
    if len(article_text) == 0:
        errors = ["Введите текст"]
        return render_template("new_article.html", errors=errors)
    new_article = articles(user_id=current_user.id, title=title, article_text=article_text)

    db.session.add(new_article)
    db.session.commit()

    return redirect("/lab6/articles")

@lab6.route("/lab6/articles/<int:article_id>", methods=['GET', 'POST'])
def getArticle(article_id):
    if current_user.is_authenticated:
        if request.method == 'POST':
            article = articles.query.filter_by(id=article_id).first()
        article = articles.query.filter_by(id=article_id).first()
        if article:
            if article.user_id == current_user.id or article.is_public:
                text = article.article_text.splitlines()
                return render_template('articleN.html', arcticle_text=text, article_title=article.title,
                            username=current_user.username)
    
    abort (403)


@lab6.route('/lab6/logout/')
@login_required
def logout():
    logout_user()
    session.clear()
    return redirect('/lab6')