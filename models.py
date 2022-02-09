from sqlalchemy import  Boolean, Column, ForeignKey, Integer, String
from database import Base
from sqlalchemy.orm import relationship


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    featured = Column(Boolean, default=False)
    title = Column(String)
    url = Column(String)
    imageUrl = Column(String)
    newsSite = Column(String)
    summary = Column(String)
    publishedAt = Column(String)

    launches = relationship("Launche", back_populates="article")
    events = relationship("Event", back_populates="article")


class Launche(Base):
    __tablename__ = "launches"
    id = Column(String, primary_key=True, index=True)
    provider = Column(String)
    article_id = Column(Integer, ForeignKey("articles.id"))

    article = relationship("Article", back_populates="launches")


class Event(Base):
    __tablename__ = "events"
    id = Column(String, primary_key=True, index=True)
    provider = Column(String)
    article_id = Column(Integer, ForeignKey("articles.id"))

    article = relationship("Article", back_populates="events")
