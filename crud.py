from sqlalchemy.orm import Session

import models, schemas


def get_article_by_id(db: Session, article_id: int):
    return db.query(models.Article).filter(models.Article.id == article_id).first()


def get_articles(db: Session, skip: int = 0, limit: int = 3):
    return db.query(models.Article).offset(skip).limit(limit).all()


def create_article(db: Session, article: schemas.ArticleCreate):
    db_article = models.Article(
        featured=article.featured,
        title=article.title,
        url=article.url,
        urlImage=article.urlImage,
        newsSite=article.newsSite,
        summmary=article.summary,
        publishedAt=article.publishedAt,
    )
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article
