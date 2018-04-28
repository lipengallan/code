#!/usr/bin/env python
# coding:utf-8

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, create_engine,ForeignKey,exc
from sqlalchemy.orm import sessionmaker,relationship
from random import randint


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    age = Column(Integer)
#    article = relationship("Article", order_by=Article.id, back_populates="user")   # error because of Article.id
 #   article = relationship("Article",backref='user')   # corrrect
     article = relationship("Article",back_populates="user")   # correct
#    article = relationship("Article", order_by=article.id, back_populates="user") # error because of article.id 
    def __str__(self):
        return '%s %s %s' %(self.id, self.name, self.age)


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    pages = Column(Integer)
    
    user_id = Column(Integer,ForeignKey('user.id')) # user is __tablename__ in User
    user = relationship('User',back_populates='article')


    def __str__(self):
        return '%s %s %s' %(self.id, self.name, self.pages)


engine = create_engine('mysql+mysqldb://root:lipeng#opzoon@localhost/relation?unix_socket'
                       '=/usr/local/mariadb/mysql.sock')

# create table mytest.users and mytest.article
Base.metadata.create_all(engine)

'''
sessionDB = sessionmaker(bind=engine)

#User.article = relationship("Article", order_by=Article.id, back_populates="user")
Tom=User(id=9,name="Tom",age=20)
Tom.article=[Article(name='newbook')]

print Tom.article[0].user.name

session=sessionDB()
session.add(Tom)
session.commit()

'''
