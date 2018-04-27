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


def add_user_all(User_list):
    session = sessionDB()
    session.add_all(User_list)
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


def modify_name_byid(id):
    session = sessionDB()
    user = session.query(User).filter(User.id == id).first()
    user.name = 'hehehehe'
    session.commit()
    session.close()



def delete_user_byId(id):
    session = sessionDB()
    session.query(User).filter(User.id == id).delete()
    session.commit()
    session.close()


def delete_user_byIdRange(id):
    session = sessionDB()
    session.query(User).filter(User.id < id).delete()
    session.commit()
    session.close()


for i in range(0):
    try:
        article_id = randint(10, 100)
        article_pages = randint(30, 500)
        add_article(article_id, "book_%s"%i, article_pages)

        user_id = randint(10, 100)
        user_age = randint(90, 200)
        add_user(user_id, "lipeng_%s" %i, user_age)
    except exc.IntegrityError as e:
        if 'Duplicate entry' in e[0]:
            continue

user_one = User(id=9,name='9',age=9)
user_two = User(id=8,name='8',age='8')


#add_user_all([user_one,user_two])




query_user_byIdRange(30)
print '---------------------------'
query_user_byIdAndAge(30,120)


#modify_name_byid(99)
#query_user_byId(99)

#delete_user_byId(99)


delete_user_byIdRange(1000)


#rollback
#infomation of fake_user is in session,
#but the session has not been commit,
#so fake_user can be seen in session,but not in mysql
fake_user = User(id=100,name='fake_user',age=10)
session=sessionDB()
session.add(fake_user)
print session.query(User).all()

