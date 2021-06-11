# encoding: utf-8

from flask import Flask, render_template, request, redirect, url_for, session, g
from exts import db
from models import User,Movie
from functools import wraps
import config
from sqlalchemy import or_

app = Flask(__name__)
app.config['SECRET_KEY'] = 'malizhi123.'
app.config.from_object(config)
app.static_folder = 'static'
db.init_app(app)



@app.route('/')
def index():
    context = {
        'movies': Movie.query.all()
    }
    return render_template('index.html', **context)


@app.route('/sign_up', methods={'GET', 'POST'})
def sign_up():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        username = request.form['username']
        email = request.form['email']
        password1 = request.form['password1']
        password2 = request.form['password2']

        # an email can only register an account
        user = User.query.filter(User.email == email).first()
        if user:
            return u'The email account has been registered'
        else:

            if password1 != password2:
                return u'The passwords entered are not the same, please fill in after checking'
            else:
                current_user = User(username=username, email=email, password=password1)
                db.session.add(current_user)
                db.session.commit()
                # current_user = User.query.filter_by(email=email).first()
                # login_user(current_user)
                return redirect(url_for('sign_in'))


@app.route('/sign_in', methods={'GET', 'POST'})
def sign_in():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        context = {
            'movies': Movie.query.all()
        }
        email = request.form['email']
        password = request.form['password']
        # remember = request.form['remember']
        user = User.query.filter(User.email == email).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            # if re:
            #     session.permanent = True
            # else:

            session.permanent = False
            if email == "123456@qq.com":


                return render_template('administrator.html', **context)
            else:
                return redirect(url_for('index'))
        else:
            return u'Email or password is wrong, please confirm and login again'

@app.route('/add_movie', methods={'GET', 'POST'})
def add_movie():
    if request.method == 'GET':
        context = {
            'movies': Movie.query.all()
        }
        return render_template('administrator.html',**context)
    else:
        moviename = request.form['moviename']
        genre = request.form['genre']
        country = request.form['country']
        year=request.form['year']
        # an email can only register an account
        a = User.query.filter(Movie.moviename == moviename).first()
        if a:
            return u'The email account has been registered'
        else:


            b = Movie(moviename=moviename,genre=genre,country=country,year=year)
            db.session.add(b)
            db.session.commit()
            return redirect(url_for('add_movie'))

@app.route('/delete/<int:movie_id>')
def delete(movie_id):
    task_to_delete = Movie.query.get_or_404(movie_id)

    db.session.delete(task_to_delete)
    db.session.commit()
    context = {
        'movies': Movie.query.all()
    }
    return render_template('administrator.html', **context)

@app.route('/genre/<genre>')
def genre(genre):
    # ms = Blog.query.filter(Movie.genre == genre)
    if genre == 'horror':
        return render_template('genre.html')

@app.route('/single')
def single():
    # ms = Blog.query.filter(Movie.genre == genre)

    return render_template('singlepage.html')
@app.route('/book')
def book():
    # ms = Blog.query.filter(Movie.genre == genre)

    return render_template('booking.html')

@app.route('/succeed')
def succeed():
    # ms = Blog.query.filter(Movie.genre == genre)

    return render_template('succeed.html')



@app.route('/country/<country>')
def country(country):
    # ms = Blog.query.filter(Movie.genre == genre)
    if country == 'US':
        return render_template('country.html')

@app.route('/a_zlist')
def a_zlist():
    # ms = Blog.query.filter(Movie.genre == genre)

    return render_template('a-zlist.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('sign_in'))


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user_id'):  # 如果用户登录了
            return func(*args, **kwargs)  # 返回的是某个页面 记得func前面要加return 不然会产生return render_template('center.html')这样类似的功能
        else:
            return redirect(url_for('sign_in'))

    return wrapper


@app.before_request
def my_before_request():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            g.user = user


@app.context_processor
def my_context_processor():
    if hasattr(g,'user'):
        return {'user': g.user}
    return {}


if __name__ == '__main__':
    app.run()
