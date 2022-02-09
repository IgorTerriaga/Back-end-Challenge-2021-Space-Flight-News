from fastapi import FastAPI
from sqlalchemy.orm import Session
from pydantic import BaseModel

from database import SessionLocal, engine
import models, schemas
from crud import get_article_by_id, get_articles, create_article


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


@app.get("/articles/", response_model=list[schemas.Article])
def get_Articles(skip: int = 0, limit: int = 3, db: Session = Depends(get_db)):
    """
    Obtém todos os artigos
    """
    articles = get_articles(db, skip=skip, limit=limit)


@app.get("/articles/{id}", response_model=schemas.Article)
def get_ArticlesById(id: int, db: Session = Depends(get_db)):
    """
    Obtém um artigo passando o id
    """
    db_article = get_article_by_id(db, id=article_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Artigo não  encontrado")
    return db_article


@app.post("/articles/", response_model=list[schemas.Article])
def create_Articles(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    """Cria um artigo"""
    # db_article = CRUD.get_article_by_id(db, article=article_id)
    return create_article(db=db, article=article)
