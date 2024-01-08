from flask import Blueprint, render_template,request, redirect, session, Flask, abort
from werkzeug.security import check_password_hash, generate_password_hash 
import psycopg2


lab5 = Blueprint('lab5', __name__)

 
@lab5.route('/lab5/')
def lab():
    return render_template('lab5.html')


def dbConnect():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database = 'knowledge_base',
        user = 'panchuk_anastasia_knowledge_base',
        password='123'
    )

    return conn; 
def dbClose(cursor, connection):
    cursor.close()
    connection.close()

@lab5.route('/lab5/users/')
def main():
    conn = dbConnect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")

    result = cur.fetchall()

    cur.close()
    conn.close()

    user_names = [user[1] for user in result]

    return render_template('users_names.html', user_names=user_names)


@lab5.route('/lab5/general/')
def gen():
    visibleUser = session.get ('username','Anon')
    return render_template ('general.html', username = visibleUser)


@lab5.route('/lab5/registration/', methods=['GET', 'POST'])
def registerPage():
    
    errors = []
   

    if request.method == 'GET':
        return render_template('registration.html', errors=errors)

    username = request.form.get('username')
    password = request.form.get('password')

    if not (username or password):  
        errors.append('Заполните все поля')
        print(errors)
        return render_template('registration.html', errors=errors)
    
    hashPassword = generate_password_hash(password)

    conn = dbConnect()
    cur = conn.cursor()
    
    #проверка
    cur.execute("SELECT username FROM users WHERE username = %s;", (username,))
    
    if cur.fetchone() is not None:
        errors.append('Пользователь с данным именем уже существует')
       
        conn.close()
        cur.close()

        return render_template('registration.html', errors=errors)

    #вставка нового пользователя
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s);", (username, hashPassword))
    conn.commit()  
    conn.close()
    cur.close()

    return redirect ('/lab5/login5/')

#Вход
@lab5.route('/lab5/login5/', methods = ['GET', 'POST'])
def loginPage():
    errors = [];
    
    if request.method == 'GET':
        return render_template('login5.html', errors=errors)
    
    username = request.form.get('username')
    password = request.form.get('password')

    if not (username or password):
        errors.append('Заполните все поля')
        return render_template('login5.html', errors=errors)
    
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT id, password FROM users WHERE username = %s;", (username,))

    result = cur.fetchone()

    if result is None:
        errors.append('Неправильный логин')
        dbClose(cur, conn)
        return render_template('login5.html', errors = errors)
    
    userID, hashPassword = result

    if check_password_hash(hashPassword, password) or hashPassword == password:
        session['id'] = userID
        session['username'] = username
        dbClose(cur, conn)
        return redirect ('/lab5/general/')
    else: 
        errors.append('Неправильный логин или пароль')
        return render_template('login5.html', errors=errors)
    


#создание новой статьи
@lab5.route('/lab5/new_article/', methods=['GET', 'POST'])
def createArticle():
    errors = [] 
    userID = session.get('id')

    if userID is not None:
        if request.method == 'GET':
            return render_template('new_article.html')

        if request.method == 'POST':
            arcticle_text = request.form.get('arcticle_text')  
            title = request.form.get('title_article')

            if len(arcticle_text) == 0:
                errors.append('Заполните поле')
                return render_template('new_article.html', errors=errors)

            conn = dbConnect()
            cur = conn.cursor()

            cur.execute("INSERT INTO articles(user_id, title, arcticle_text) VALUES (%s, %s, %s) RETURNING id;", (userID, title, arcticle_text))
            new_article_id = cur.fetchone()[0]
            conn.commit()

            dbClose(cur, conn)
            return redirect(f'/lab5/articles/{new_article_id}')
    abort (403)         
    
#просмотр статей
@lab5.route('/lab5/articles/<int:article_id>')  
def state(article_id):
    userID = session.get('id')  
        
    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()
            
        cur.execute("SELECT title, arcticle_text FROM articles WHERE id = %s and user_id = %s", (article_id, userID))
        articleBody = cur.fetchone()

        dbClose(cur, conn)

        if articleBody is None:
            return 'Not found!'
                
            
        text = articleBody[1].splitlines()

        return render_template('articleN.html', arcticle_text=text, article_title=articleBody[0],
                            username=session.get('username'))
    
    abort (403)
       
    

@lab5.route('/lab5/user_articles/')
def user_articles():
    userID = session.get('id')

    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()

        cur.execute(f"SELECT id, title, arcticle_text FROM articles WHERE user_id = {userID}")
        articles = cur.fetchall()

        dbClose(cur, conn)

        return render_template('user_articles.html', articles=articles)

    abort (403)    

@lab5.route('/lab5/logout/')
def logout():
    # Clear the entire session
    session.clear()
    return redirect('/lab5/login5/')