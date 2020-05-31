FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

RUN pip install -r wsgi


COPY . /code/

CMD gunicorn --bind 0.0.0.0:$PORT wsgi 
