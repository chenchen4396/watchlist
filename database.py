from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from watchlist import db,app
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)
class Photos(db.Model):
    # 创建表结构操作
    # 表名
    __tablename__ = 'uphotos'
    #  字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer,db.ForeignKey("user.id"))
    url = db.Column(db.String(50), nullable=False)
with app.app_context():
    # db.init_app(app)
    db.drop_all()
    db.create_all()