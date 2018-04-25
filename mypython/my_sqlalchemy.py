#!/usr/bin/env python
# coding:utf-8

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, create_engine, exc
from sqlalchemy.orm import sessionmaker
from random import randint


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    age = Column(Integer)

    def __str__(self):
        return '%s %s %s' %(self.id, self.name, self.age)


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    pages = Column(Integer)

    def __str__(self):
        return '%s %s %s' %(self.id, self.name, self.pages)


engine = create_engine('mysql+mysqldb://root:lipeng#opzoon@localhost/mytest?unix_socket'
                       '=/usr/local/mariadb/mysql.sock')

# create table mytest.users and mytest.article
Base.metadata.create_all(engine)
sessionDB = sessionmaker(bind=engine)


def add_user(id, name, age):
    user = User(id=id, name=name, age=age)
    session = sessionDB()
    session.add(user)
    session.commit()
    session.close()


def add_article(id, name, pages):
    article = Article(id=id, name=name, pages=pages)
    session = sessionDB()
    session.add(article)
    session.commit()
    session.close()


def query_user_byId(id):
    session = sessionDB()
    user = session.query(User).filter(User.id == id).first()
    session.close()
    print user


def query_user_byIdAndAge(id,age):
    session = sessionDB()
    for each in session.query(User).filter(User.id > id).filter(User.age > age):
        print each
    session.close()


def query_user_byIdRange(id):
    import pdb
    # pdb.set_trace()
    session = sessionDB()
    for each in session.query(User).filter(User.id > id):
        print each
    session.close()


def query_user_all():
    session = sessionDB()
    for each in session.query(User).order_by(User.age):
        print each
    session.close()


for i in range(0):
    try:
        article_id = randint(1, 100)
        article_pages = randint(30, 500)
        add_article(article_id, "book_%s"%i, article_pages)

        user_id = randint(1, 100)
        user_age = randint(90, 200)
        add_user(user_id, "lipeng_%s" %i, user_age)
    except exc.IntegrityError as e:
        if 'Duplicate entry' in e[0]:
            continue

query_user_byIdRange(30)
print '---------------------------'
query_user_byIdAndAge(30,120)
#query_user_all()