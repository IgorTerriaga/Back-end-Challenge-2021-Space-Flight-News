
from pydantic import BaseModel, validator

class Article(BaseModel):
    """
    Define a estrura de dados que armazena as informações dos artigos.
    """
    featured = bool
    title = ""
    url = ""
    imageUrl = ""
    newsSite = ""
    summary = ""
    publishedAt = ""

