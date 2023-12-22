FROM postgres:latest

ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_DB=parkingdb

COPY init_db.sql /docker-entrypoint-initdb.d/

#docker build -t postgres .  
#docker run -dp PUERTO:5432 postgres
