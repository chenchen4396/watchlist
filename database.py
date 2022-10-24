from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from watchlist import db,app
class User(db.Model, UserMixin):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(20))
    username = db.Column(db.String(20))
    password = db.Column(db.String(128))
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
    def __init__(self):
        self.id=None
        self.uid=None
        self.url=None
# with app.app_context():
#     # db.init_app(app)
#     db.drop_all()
#     db.create_all()