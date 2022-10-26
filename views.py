from flask import request, url_for, redirect
from flask import flash
from flask import render_template
from flask_login import login_required, logout_user
from flask_login import login_user
from flask_login import current_user
from flask_login import LoginManager
from watchlist import db,app
from watchlist.database import  User,Photos
from watchlist.__init__ import  load_user
@app.route('/')
def hello():
    return 'hello'

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/grxx')
def grxx():
    return render_template('grxx.html')

@app.route('/xgmm')
def xgmm():
    return render_template('xgmm.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash('Invalid input.')
            return redirect(url_for('login'))

        user = User.query.first()
        # 验证用户名和密码是否一致
        # if username == user.username and user.validate_password(password):
        if username == user.username and password == user.password:
            login_user(user)  # 登入用户
            flash('Login success.')
            return redirect(url_for('home'))  # 重定向到主页

        else:
            flash('Invalid username or password.')  # 如果验证失败，显示错误消息
            return redirect(url_for('login'))  # 重定向回登录页面

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Goodbye.')
    return redirect(url_for('index'))

@app.route('/home')
@login_required
def home():
    photos=Photos.query.filter(Photos.uid == current_user.id)
    return render_template('home.html',user=current_user, photos=photos)



