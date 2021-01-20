FROM python:3
ENV PYTHONUNBUFFERD 1
RUN apt-get update
RUN apt-get install -y default-mysql-client
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/
