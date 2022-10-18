from flask import request, url_for, redirect
from flask_login import current_user
from watchlist import db,app


@app.route('/')
def index():
    return 'hello'
@app.route('/user')
def user():
    # abort(401)  # Unauthorized 未授权
    return 'Welcome to user!'
# # from watchlist.models import User, Movie
#
# @app.route('/')
# def hello():
#     return login

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#
#         if not username or not password:
#             flash('Invalid input.')
#             return redirect(url_for('login'))
#
#         user = User.query.first()
#
#         if username == user.username and user.validate_password(password):
#             login_user(user)
#             flash('Login success.')
#             return redirect(url_for('index'))
#
#         flash('Invalid username or password.')
#         return redirect(url_for('login'))
#
#     return render_template('login.html')
#
# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     flash('Goodbye.')
#     return redirect(url_for('index'))