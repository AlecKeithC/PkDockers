FROM postgres:latest

ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=detectaudec
ENV POSTGRES_DB=parkingdb

COPY init_db.sql /docker-entrypoint-initdb.d/

