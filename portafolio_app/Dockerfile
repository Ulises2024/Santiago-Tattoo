FROM alpine:3.19
ENV APP_DIRECTORY portafolio_app
# INSTALL TZDATA
RUN apk add --update --no-cache tzdata
# INSTALL PYTHON 3
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
# INSTALL PIP
RUN apk add --update --no-cache py3-pip
# INSTALL PIP
RUN apk add --update --no-cache mariadb-dev 
RUN apk add --update --no-cache gcc
#RUN apk add --update --no-cache build-deps 
RUN apk add --update --no-cache python3-dev 
RUN apk add --update --no-cache musl-dev
RUN apk add --update --no-cache netcat-openbsd
# CREATE DIRECTORY TRANSBANK
RUN mkdir -p /opt/app/$APP_DIRECTORY
# CHANGE DIRECTORY
WORKDIR /opt/app/
# COPY  DB SHELL SCRIPT
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh
# COPY DEPENDENCIES
# COPY requirements.txt .
# CHANGE DIRECTORY
WORKDIR /opt/app/$APP_DIRECTORY
# INSTALL DEPENDENCIES
#RUN python3 -m venv env
#RUN source env/bin/activate && python -m pip install -r ../requirements.txt
# CHANGE DIRECTORY
#WORKDIR /opt/app/$APP_DIRECTORY