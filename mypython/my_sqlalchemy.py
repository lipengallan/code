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



engine = create_engine('mysql+mysqldb://root:root@localhost:3306/mytest')
try:
    engine.connect()
except exc.OperationalError:
    engine = create_engine('mysql+mysqldb://root:root@localhost:3306')
    engine.execute('create database mytest').close()
    engine = create_engine('mysql+mysqldb://root:root@localhost:3306/mytest')



Base.metadata.create_all(engine)
DBsession = sessionmaker(bind=engine)
session = DBsession()

new_user = User(id='5',name='Bob')
session.add(new_user)
session.commit()
session.close()