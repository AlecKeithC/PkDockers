# PkDockers

[Breve descripción de tu proyecto, qué hace y cualquier otra información relevante que los usuarios o desarrolladores deban saber.]

## Requisitos Previos

Para ejecutar esta aplicación, necesitarás tener Docker y Docker Compose instalados en tu máquina. Sigue las instrucciones en la [Página oficial de instalación de Docker](https://docs.docker.com/get-docker/) para instalar Docker. (Recomendado Docker Desktop)

## Configuración con Docker Compose

Este proyecto utiliza Docker Compose para facilitar la ejecución de servicios multi-contenedor. La configuración de todos los servicios requeridos se encuentra en el archivo `docker-compose.yml`.

## Clonar repositorio

Antes de iniciar los servicios con Docker Compose, debes configurar los puertos y las credenciales:

- En postgre-db/Dockerfile, encuentra las instrucciones para las variables de entorno USER y PASSWORD y sustitúyelas con el nombre de usuario y la contraseña que desees configurar para la base de datos.
- En api/main.py, busca la línea que define el puerto y reemplaza "PUERTO" con el puerto que desees utilizar para el servicio de la API. También actualiza los campos con los datos de la DB, seleccionados en postgre-db/Dockerfile.
- En docker-compose.yml, actualiza todas las instancias de "PUERTO" bajo los servicios para que coincidan con los puertos que has decidido exponer. Asegúrate de que estos puertos estén disponibles y no estén siendo utilizados por otro servicio en tu sistema. También actualiza los campos con los datos de la DB, seleccionados en postgre-db/Dockerfile.
  
### Iniciar los Servicios

Para construir e iniciar los servicios, ejecuta el siguiente comando en el directorio raíz del proyecto:

  ```bash
  docker-compose up --build


  
