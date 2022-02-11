import models, schemas
from cmath import log
from sqlalchemy.orm import Session


def get_article_by_id(db: Session, id: int):
    articles = db.query(models.Article).filter(models.Article.id == id).first()
    if articles is None:
        print(articles)
        return None
    articles.events
    articles.launches
    for e in articles.events:
        del e.article_id
    for e in articles.launches:
        del e.article_id
    return articles


def get_articles(db: Session, skip: int = 0, limit: int = 3):
    articles = db.query(models.Article).offset(skip).limit(limit).all()
    for e in articles:
        e.events
        e.launches

    return articles


def create_article(db: Session, article: schemas.ArticleCreate):
    db_article = models.Article(
        featured=article.featured,
        title=article.title,
        url=article.url,
        imageUrl=article.imageUrl,
        newsSite=article.newsSite,
        summary=article.summary,
        publishedAt=article.publishedAt,
    )
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article


def update_article(db: Session, db_article, article):
    db_article.title = article.title
    db_article.featured = article.featured
    db_article.url = article.url
    db_article.imageUrl = article.imageUrl
    db_article.newsSite = article.newsSite
    db_article.summary = article.summary
    db_article.publishedAt = article.publishedAt

    db.commit()
    db.refresh(db_article)
    return db_article


def delete_article(db: Session, id: int):
    db_article = db.query(models.Article).filter(models.Article.id == id).first()
    db.delete(db_article)
    db.commit()
    return {"detail": "Ok"}
