FROM postgres:lastest

ENV POSTGRES_USER admin
ENV POSTGERS_PASSWORD detectaudec
ENV POSTGERS_DB parkingdb

COPY init_db.sql /docker-entrypoint-initdb.d/


# Path: /docker-entrypoint-initdb.d/init.sql
