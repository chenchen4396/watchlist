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
from sqlalchemy import func

@app.route('/register/',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        phone_number = request.form.get('phone_number')
        if not all([username,name,password,password2]):
            flash ('参数不完整')
        elif password != password2:
            flash ('两次密码不一致，请重新输入')
        else:
            new_user=User()
            new_user.username =username
            new_user.name = name
            new_user.password = password
            new_user.phone_number = phone_number
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
    return render_template('register.html')

