FROM python:3.9.7



COPY ./src/requirements.txt /code/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

WORKDIR /code

COPY src /code

EXPOSE 8000

CMD ["uvicorn", "main:app","--host=0.0.0.0","--reload"]