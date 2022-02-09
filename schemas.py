from pydantic import BaseModel


class ArticleBase(BaseModel):
    """
    Define a estrura de dados que armazena as informações dos artigos.
    """

    featured: bool = None
    title= ""
    url= ""
    imageUrl= ""
    newsSite= ""
    summary= ""
    publishedAt= ""


class ArticleCreate(ArticleBase):
    pass


class Article(ArticleBase):
    id: int

    class Config:
        orm_mode = True
