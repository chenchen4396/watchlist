from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)
# 配置数据库的地址
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@127.0.0.1:3306/flask" # 这里根据自己的数据库地址，数据库名字配置
# 跟踪数据库的修改，不建议开启
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key="123456"
db = SQLAlchemy(app)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    from .database import User
    user = User.query.get(int(user_id))
    return user


login_manager.login_view = 'login'
# login_manager.login_message = 'Your custom message'


@app.context_processor
def inject_user():
    from .database  import User
    user = User.query.first()
    return dict(user=user)
from watchlist import views, errors, commands,database,upload
app.run()