import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.getcwd() + '/database/main.db'
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    userID = Column(Integer, primary_key=True, default=100)
    email = Column(String(120), nullable=False)
    password = Column(String(120), nullable=False)
    coins = Column(Integer, nullable=False, default=10)
    avatar = Column(Text, nullable=False, default="default")
    pincode = Column(Text, nullable=False, default="123")

    def __repr__(self):
        return '[ID:{},email:{},coins:{},avatar:{},pincode:{}]'.format(self.id,self.email,self.coins,self.avatar,self.pincode)

class Community(db.Model):
    __tablename__ = 'community'
    id = Column(Text, primary_key=True)
    title = Column(String(120), nullable=False)
    userID = Column(Integer, ForeignKey('User.id'))

    def __repr__(self):
        return '[ID:{},title:{},userID:{}]'.format(self.id,self.title,self.userID)

class Thread(db.Model):
    __tablename__ = 'threads'
    id = Column(Text, primary_key=True)
    userID = Column(Integer, ForeignKey('User.id'))
    contents = Column(Text, nullable=False, default="No Content")

    def __repr__(self):
        return '[ID:{},userID:{},contents:{}]'.format(self.id,self.userID,self.contents)

class Request(db.Model):
    __tablename__ = 'requests'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(120), nullable=False)
    content = Column(Text, nullable=False)
    rewards = Column(String(120))
    timelimit = Column(String(120))
    userID = Column(Integer, ForeignKey('User.id'))
    status = Column(Text, nullable=False, default="Available")
    answer = Column(Text)

    def __repr__(self):
        return '[ID:{},title:{},content:{},rewards:{},timelimit:{},userid:{},status:{},answer:{}]'.format(self.id,
        self.title,self.content,self.rewards,self.timelimit,self.userID,self.status,self.answer)

class Shop(db.Model):
    __tablename__ = 'shop'
    id = Column(Integer, primary_key=True)
    detail = Column(Text, nullable=False)
    price = Column(Integer, default=0)

    def __repr__(self):
        return '[ID:{},detail:{},price:{}]'.format(self.id,self.detail,self.price)

class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    userID = Column(Integer, ForeignKey('User.id'))
    itemID = Column(Integer, ForeignKey('Shop.id'))

    def __repr__(self):
        return '[ID:{},userID:{},itemID:{}]'.format(self.id,self.userID,self.itemID)

class Todo(db.Model):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True, autoincrement=True)
    userID = Column(Integer, ForeignKey('User.id'))
    requireID = Column(Integer, ForeignKey('Request.id'))
    status = Column(Text, default="Undo")

    def __repr__(self):
        return '[ID:{},userID:{},requireID:{},status:{}]'.format(self.id,self.userID,self.requireID,self.status)
    
class Chats(db.Model):
    __tablename__ = 'chats'
    chatID = Column(Text, primary_key=True)
    srcUserID = Column(Integer, ForeignKey('User.id'))
    dstUserID = Column(Integer, ForeignKey('User.id'))
    content = Column(Text, nullable=False, default="No Content")

    def __repr__(self):
        return '[ID:{},srcUserID:{},dstUserID:{},content:{}]'.format(self.chatID,self.srcUserID,self.dstUserID,self.content)
