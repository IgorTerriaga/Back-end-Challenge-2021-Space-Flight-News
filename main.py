from fastapi import FastAPI, Depends, HTTPException
from fastapi_pagination import Page, add_pagination, paginate
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal, engine
import models, schemas
from crud import get_article_by_id, get_articles, create_article, update_article, delete_article


models.Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def welcome():
    """title = Column(String)
    retorna uma mensagem de boas vindass -> Back-end Challenge 2021 🏅 - Space Flight News
    """
    return {"menssagem": "Back-end Challenge 2021 🏅 - Space Flight News"}


@app.get("/articles/",)
def get_Articles(skip: int = 0, limit: int = 3, db: Session = Depends(get_db)):
    """
    Obtém todos os artigos
    """
    articles = get_articles(db, skip=skip, limit=limit)
    return articles


@app.get("/articles/{id}")
def get_ArticlesById(id: int, db: Session = Depends(get_db)):
    """
    Obtém um artigo passando o id
    """
    db_article = get_article_by_id(db, id=id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Artigo não  encontrado")
    return db_article


@app.post("/articles/", response_model=schemas.Article)
def create_Articles(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    """Cria um artigo"""
    # db_article = CRUD.get_article_by_id(db, article=article_id)
    return create_article(db=db, article=article)


@app.put("/articles/{id}")
def update_Article(id:int, article:schemas.ArticleCreate, db: Session = Depends(get_db)):
    db_article =  get_article_by_id(db, id=id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Artigo não  encontrado")
    return update_article(db, db_article, article)


@app.delete("/articles/{id}")
def delete_Article(id: int, db: Session = Depends(get_db)):
    db_article = get_article_by_id(db, id=id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Artigo não  encontrado")
    return delete_article(db, id=id)
