from sqlalchemy import Table, Boolean, Column, ForeignKey, Integer, String
from database import Base


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    featured = Column(Boolean, default=False)
    title = Column(String)
    url = Column(String)
    urlImage = Column(String)
    newsSite = Column(String)
    summmary = Column(String)
    publishedAt = Column(String)