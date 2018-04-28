from sqlalchemy import Table, Column, Integer,String,DATE, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    pub_date = Column(DATE)
    authors = relationship('Author',backref='books')
    def __repr__(self):
        return self.name

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    def __repr__(self):
        return self.name


engine = create_engine('mysql+mysqldb://root:lipeng#opzoon@localhost/relation?unix_socket'
                       '=/usr/local/mariadb/mysql.sock')
Base.metadata.create_all(engine) 


