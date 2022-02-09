from fastapi import FastAPI
from typing import Generator
from sqlalchemy.orm import Session
from pydantic import BaseModel

# from models import Articles
from models import articles
from database import conn
from schemas import Article

app = FastAPI()


@app.get("/")
def welcome():
    """title = Column(String)
    retorna uma mensagem de boas vindass -> Back-end Challenge 2021 🏅 - Space Flight News
    """
    return {"menssagem": "Back-end Challenge 2021 🏅 - Space Flight News"}


@app.get("/articles")
async def get_Articles():
    """
    Obtém todos os artigos
    """
    return conn.execute(articles.select()).fetchall()


@app.get("/articles/{id}")
def get_ArticlesById(id: int):
    """
    Obtém um artigo passando o id
    """
    return conn.execute(articles.select().where(articles.id == id)).fetchall()


@app.post("/articles")
def create_Articles(article: Article):
    """Cria um artigo"""
    return conn.execute(
        articles.insert().values(
            title=articles.title,
            url=articles.url,
            urlImage=articles.urlImage,
            newsSite=articles.newsSite,
            summmary=articles.summmary,
            publishedAt=articles.publishedAt,
        )
    ).fetchall()


@app.put("/articles/{id}")
def update_articles(id: int, article: Article):
    """atualiza um artigo passando o id"""

    conn.execute(
        articles.update()
        .values(
            title=articles.title,
            url=articles.url,
            urlImage=articles.urlImage,
            newsSite=articles.newsSite,
            summmary=articles.summmary,
            publishedAt=articles.publishedAt,
        )
        .where(articles.id == id)
    )
    return conn.execute(articles.select()).fetchall()


@app.delete("/articles/{id}")
def delete_articles(id):
    """Delete um artigo passando o id"""
    return conn.execute(articles.delete().where(articles.id == id)).fetchall()
