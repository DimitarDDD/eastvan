from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


Base  = declarative_base()


class Book(Base):
    __tablename__ = 'book'
    id  = Column(Integer, primary_key=True, index=True)
    title = Column(String) 
    description = Column(String)
    rating = Column(Float)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    author_id = Column(Integer, ForeignKey('author.id', ondelete='CASCADE'))
    author = relationship('Author', back_populates="books")


class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now()) 
    books = relationship("Book",    cascade="all,delete-orphan",
        back_populates="author",
        uselist=True,)