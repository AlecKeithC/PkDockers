FROM postgres:latest

ENV POSTGRES_USER=USER
ENV POSTGRES_PASSWORD=PASSWORD
ENV POSTGRES_DB=parkingdb

COPY init_db.sql /docker-entrypoint-initdb.d/

#docker build -t postgres .  
#docker run -dp PUERTO:5432 postgres
