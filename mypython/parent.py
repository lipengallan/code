from sqlalchemy import Table, Column, Integer,String,DATE, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    children = relationship("Child", back_populates="parent")

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    parent_id = Column(Integer, ForeignKey('parent.id'))
    parent = relationship("Parent", back_populates="children")



engine = create_engine('mysql+mysqldb://root:lipeng#opzoon@localhost/relation?unix_socket'
                       '=/usr/local/mariadb/mysql.sock')
Base.metadata.create_all(engine) 


sessionDB = sessionmaker(bind=engine)
session = sessionDB()

'''
# create parent and child tables;

parent = Parent(id=1,name='aaaaa')
child_1  = Child(id=1,name='child_1')
child_2  = Child(id=2,name='child_2')

parent.children = [child_1,child_2]

session.add(parent)
session.commit()
session.close()
'''

# query tables;

for each in session.query(Parent,Child).filter(Parent.id==1).filter(Child.id==2).all():
    parent,child = each
    print parent.id,parent.name
    print child.id,child.name





 
