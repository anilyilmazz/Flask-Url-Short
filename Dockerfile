FROM python:3.8.3-slim-buster

WORKDIR /url_short

COPY requirements.txt requirements.txt

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python", "manage.py"]