FROM python:3.11

WORKDIR /singlestore
COPY ./requirements.txt /api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt
COPY . /singlestore

