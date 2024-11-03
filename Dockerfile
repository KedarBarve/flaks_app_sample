# pull the official docker image
#FROM python:3.8.6-slim
FROM ubuntu:22.04

RUN apt-get update 

RUN apt-get  -y install wget 
RUN apt-get update
RUN  apt-get -y  install gcc
RUN  apt-get -y  install zlib1g-dev
RUN  apt-get -y  install make

RUN  apt-get -y install software-properties-common
#RUN add-apt-repository ppa:fkrull/deadsnakes
RUN  apt-get update
RUN  apt-get -y install python3.9

RUN  apt-get -y install python3-pip 
RUN  apt-get -y install libpq-dev python3-dev
RUN  apt-get -y install libgl1

RUN  apt-get -y install libtool pkg-config build-essential autoconf automake


#RUN  apt-get -y install git 
RUN apt-get install -y vim
RUN apt-get install -y libreadline-dev
RUN apt-get install -y libsm6 libxext6 libxrender-dev


# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHON python3
#USER root 

# Install development tools and Python development headers
#RUN apt-get update && apt-get install -y build-essential python3-dev

# Install gcc
#RUN apt-get install -y gcc

# install dependencies
COPY requirements/requirements.txt /app
RUN pip3 install -r requirements.txt

RUN mkdir -p /app/tmp
RUN mkdir -p /app/bin
RUN mkdir -p /app/config
RUN mkdir -p /app/logs
RUN mkdir -p /app/input
RUN mkdir -p /app/src/main/entities

# copy project
COPY bin/run_gunicorn.sh /app/bin/
COPY ./*.py /app/
COPY ./src/main/*.py /app/src/main
COPY ./src/main/entities/*.py  /app/src/main/entities/
COPY config/config*.dat /app/config
COPY config/*.dat /app/config

RUN chmod +x /app/bin/run_gunicorn.sh

EXPOSE 5005
ENTRYPOINT ["/app/bin/run_gunicorn.sh"]
