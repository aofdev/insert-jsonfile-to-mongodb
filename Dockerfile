FROM python:3.9.1-slim-buster
WORKDIR  /insert-jsonfile-to-mongodb
COPY requirements.txt /insert-jsonfile-to-mongodb/requirements.txt
RUN pip install -r requirements.txt
COPY main.py /insert-jsonfile-to-mongodb/main.py
