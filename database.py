from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from watchlist import db,app
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date
class User(db.Model, UserMixin):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    #昵称
    name = db.Column(db.String(20),nullable=False)
    #用来登录的用户名
    username = db.Column(db.String(20),nullable=False)
    password = db.Column(db.String(14),nullable=False)
    head_url = db.Column(db.String(100))
    email=db.Column(db.String(30))
    create_time=db.Column(db.DateTime,nullable=False, default=datetime.now)
    phone_number=db.Column(db.Integer,nullable=False)
    brithday=db.Column(Date)
    def __init__(self):
        self.username=None
        self.id=None
        self.username=None
        self.password=None

    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return self.id
    # def set_password(self, password):
    #     self.password_hash = generate_password_hash(password)
    #
    # def validate_password(self, password):
    #     return check_password_hash(self.password_hash, password)
class Photos(db.Model):
    # 创建表结构操作
    # 表名
    __tablename__ = 'uphotos'
    __table_args__ = {'extend_existing': True}
    #  字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer,db.ForeignKey("user.id"))
    url = db.Column(db.String(100), nullable=False)
    upload_time=db.Column(db.DateTime,nullable=False, default=datetime.now)
    delete_time=db.Column(db.DateTime,nullable=False, default=datetime.now)
    def __init__(self):
        self.id=None
        self.uid=None
        self.url=None
# with app.app_context():
#     # db.init_app(app)
#     db.drop_all()
#     db.create_all()
