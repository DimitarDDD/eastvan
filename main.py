import uvicorn
import models
import schemas
from sqlalchemy.orm import Session , Query
from fastapi import FastAPI
from schemas import Book as SchemaBook
from schemas import Author as SchemaAuthor
#from router import router
from schemas import Book
from schemas import Author
from fastapi_sqlalchemy import DBSessionMiddleware, db
from models import Book as ModelBook
from models import Author as ModelAuthor
from db_conf import engine


models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url="postgresql://postgres:pass123pass@localhost:5432/bookdb")



@app.post('/book/', response_model=SchemaBook, name='Add new book', description= 'Adding a new book to the database')
async def book(book: SchemaBook):
    db_book = ModelBook(title=book.title, rating=book.rating, author_id = book.author_id)
    db.session.add(db_book)
    db.session.commit()
    return db_book


@app.get('/book/',  name='Get all books', description= 'Get all the books from the database')
async def book():
    book = db.session.query(ModelBook).all()
    return book


@app.get("/book/{id}",  name='Get one book', description= 'Get specific book from the database')
async def getSpecificBook(id:int): 
    book = db.session.query(models.Book).get(id)  
    return book


@app.put("/book/{id}",  response_model=SchemaBook,  name='Update a book', description= 'Update specific book from the database')
async def updateBook(id:int, book: SchemaBook): 
    book1 = db.session.query(models.Book).get(id)   
    book1.title = book.title 
    book1.description = book.description
    db.session.commit() 
    return book


@app.delete("/book/{id}", name='Delete a book', description= 'Delete specific book from the database')
async def getSpecificBook(id:int): 
    book = db.session.query(models.Book).get(id) 
    db.session.delete(book) 
    db.session.commit()  
    db.session.close()
    return 'Book was deleted'


@app.post('/author/', response_model=SchemaAuthor, name='Add new author', description= 'Add new author to the database')
async def author(author:SchemaAuthor):
    db_author = ModelAuthor(name=author.name, age=author.age)
    db.session.add(db_author)
    db.session.commit()
    return db_author


@app.get('/author/', name='Get all authors', description= 'Get all the authors from the database')
async def author():
    author = db.session.query(ModelAuthor).all()
    return author 