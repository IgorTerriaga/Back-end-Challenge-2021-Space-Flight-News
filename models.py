from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from database import meta

articles = Table(
    "articles",
    meta,
    Column("id", Integer, primary_key=True),
    Column("featured", Boolean, default=False ),
    Column("title", String(255)),
    Column("url", String(255)),
    Column("urlImage", String(255)),
    Column("newsSite", String(255)),
    Column("summmary", String(255)),
    Column("publishedAt", String(255))
)
