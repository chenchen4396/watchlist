from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
HOSTNAME = '127.0.0.1'
DATABASE = 'flask'
PORT = 3306
USERNAME = 'root'
PASSWORD = 'Apromise202077+'
DB_URL = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
engine = create_engine(DB_URL)

Base = declarative_base(engine)

class Person(Base):
    # 创建表结构操作
    # 表名
    __tablename__ = 'user'
    #  字段
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    gender = Column(Integer, comment="1男，2女")
    birthday=Column(Integer(8))
    area =Column(String(30))
    pnumber =(Column(String(20), nullable=False))
    email = (Column(String(20)))

class Photos(Base):
    # 创建表结构操作
    # 表名
    __tablename__ = 'uphotos'
    #  字段
    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer,ForeignKey("user.id"))
    url = Column(String(50), nullable=False)
Base.metadata.create_all()
# 创建一个会话
session = sessionmaker(engine)()
p1 = Person(name='张三', gender='1',pnumber='1234')
session.add(p1)
session.commit()
