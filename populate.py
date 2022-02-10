import smtplib
import requests
from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


connect = config("STRING_CONNECTION")
engine = create_engine(connect)
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("igsantos1996@gmail.com", "tggkxdrauhvcguvp")
Session = sessionmaker(bind=engine)
session = Session()

url = "https://api.spaceflightnewsapi.net/v3/articles?_limit=50"
msg = 'Ocorreu um erro ao sincronizar os dados dos articles.'
payload = {}
headers = {}

try:
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
except Exception as e:
    print(e)
    server.sendmail("igsantos1996@gmail.com", "wedsonteixeira14081998@gmail.com", "Subject: Sincronizacao do servidor\n{}".format(msg))
    server.quit()
