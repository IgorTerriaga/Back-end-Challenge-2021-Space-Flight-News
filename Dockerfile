FROM python:3.9.7

COPY ./BackEndChallengeSpaceFlight /app/src
COPY ./requirements.txt /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "BackEndChallengeSpaceFlight.main:app","--host=0.0.0.0","--reload"]

