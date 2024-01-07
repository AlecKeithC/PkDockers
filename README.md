# PkDockers

¡Bienvenido a PkDockers! Aquí se encuentra las instrucciones para instalar e iniciar el servidor para la aplicación de ParkingUdec.

## Requisitos Previos

- Instala git para poder clonar el repositorio más tarde. [Página oficial de instalación de Git](https://www.git-scm.com/downloads).
- Para ejecutar esta aplicación, necesitarás tener Docker y Docker Compose instalados en tu máquina. Sigue las instrucciones en la [Página oficial de instalación de Docker](https://docs.docker.com/get-docker/) para instalar Docker. (Recomendado Docker Desktop)

## Configuración con Docker Compose

Este proyecto utiliza Docker Compose para facilitar la ejecución de servicios multi-contenedor. La configuración de todos los servicios requeridos se encuentra en el archivo `docker-compose.yml`.

## Clonar repositorio

Antes de iniciar los servicios con Docker Compose, debes configurar los puertos y las credenciales:

- Ejecuta el comando git clone https://github.com/AlecKeithC/PkDockers.git en un nuevo directorio.
- En PkDockers, encuentra las instrucciones para las variables de entorno en ".env" USER y PASSWORD y sustitúyelas con el nombre de usuario y la contraseña que desees configurar para la base de datos.
- En api/main.py, busca la línea que define el puerto y reemplaza "PUERTO" con el puerto que desees utilizar para el servicio de la API. También actualiza los campos con los datos de la DB, seleccionados en postgre-db/Dockerfile.
- En docker-compose.yml, actualiza todas las instancias de "PUERTO" bajo los servicios para que coincidan con los puertos que has decidido exponer. Asegúrate de que estos puertos estén disponibles y no estén siendo utilizados por otro servicio en tu sistema. También actualiza los campos con los datos de la DB, seleccionados en postgre-db/Dockerfile.
  
### Iniciar los Servicios

Para construir e iniciar los servicios, ejecuta el siguiente comando en el directorio raíz del proyecto:

  ``bash
  docker-compose up --build

### Configurar NGINX Proxy Manager (NPM)

Iniciados los servicios, 
- ingresar a http://(ip_donde_se_ejecuta_el_contenedor):81 aquí se abrirá el "Login" de NPM, para iniciar sesión por primera vez usa el email: admin@example.com y la contraseña: changeme, modificar los datos que se pedirán.
- Añadir un Proxy host, recuerda tener un dominio listo, añádelo.
- Configurar la ip (ip_donde_se_ejecuta_el_contenedor), en "Forward Port" escribir el puerto donde se ejecuta la API (32784 en el Docker-compose.yml, es modificable a cualquier puerto).
- Configurar certificado SSL gratis, en el apartado "SSL". (Se requiere para funcionar con la aplicación móvil)

## ¡El servidor ya está configurado!
