from asyncio import events
from click import launch
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "postgresql+psycopg2://zyhfesfxpfxvbz:6318d82135697351e26637859cc30126bd6937367c892daad9fc008ac6af06ba@ec2-34-205-46-149.compute-1.amazonaws.com:5432/d7b7etm394h0d"
)

Session = sessionmaker(bind=engine)
session = Session()

url = "https://api.spaceflightnewsapi.net/v3/articles?_limit=50"

payload = {}
headers = {}
response = requests.get(url, headers=headers, data=payload).json()


def queryExecute(response):
    for post in response:
        id = post["id"]
        featured = post["featured"]
        title = post["title"]
        url = post["url"]
        imageUrl = post["imageUrl"]
        newsSite = post["newsSite"]
        summary = post["summary"]
        publishedAt = post["summary"]
        events = post["events"]
        launches = post["launches"]

        query = f"select * from articles where id = {id}"
        result = session.execute(query)

        if result.first() is None:
            query = f"insert into articles values ({id}, {featured}, '{title}', '{url}', '{imageUrl}', '{newsSite}', '{summary}', '{publishedAt}')"
            session.execute(query)

        for event in events:
            query = f'select * from events where id = \'{event["id"]}\''
            result = session.execute(query)

            if result.first() is None:
                query = f'insert into events values (\'{event["id"]}\', \'{event["provider"]}\', {id})'
                session.execute(query)

        for launch in launches:
            query = f'select * from launches where id = \'{launch["id"]}\''
            result = session.execute(query)

            if result.first() is None:
                query = f'insert into launches values (\'{launch["id"]}\', \'{launch["provider"]}\', {id})'
                session.execute(query)

    session.commit()


queryExecute(response)
