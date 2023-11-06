FROM postgres:latest

ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=detectaudec
ENV POSTGRES_DB=parkingdb

COPY init_db.sql /docker-entrypoint-initdb.d/

#docker build -t postgres .  
#docker run -dp 32783:5432 postgres