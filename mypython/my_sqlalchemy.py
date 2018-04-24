#!/usr/bin/env python
# coding:utf-8


from sqlalchemy import Column, Integer, String, create_engine,exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'user';
    id = Column(Integer,primary_key=True)
    name = Column(String(10), primary_key=True)


    def __str__(self):
        return ''.join([login,userid,projid])


def test_create_insert():
    port = 30023
    engine = create_engine('mysql+mysqldb://root:root@localhost:30023/mytest?unix_socket=/usr/local/mariadb/mysql.sock')
    try:
        kwargs = {'unix_socket':'/usr/local/mariadb/mysql.sock'}
        engine.connect()
    except exc.OperationalError:
        engine = create_engine('mysql+mysqldb://root:lipeng#opzoon@localhost:30023/?unix_socket=/usr/local/mariadb/mysql.sock')
        engine.execute('create database mytest',**kwargs).close()
        engine = create_engine('mysql+mysqldb://root:lipeng#opzoon@localhost:30023/mytest?unix_socket=/usr/local/mariadb/mysql.sock')



    Base.metadata.create_all(engine)
    DBsession = sessionmaker(bind=engine)
    session = DBsession()

    new_user = User(id='5',name='Bob')
    session.add(new_user)
    session.commit()
    session.close()


if __name__ == '__main__':
    test_create_insert()



