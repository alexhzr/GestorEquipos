# Docker
Docker nos da la posibilidad de _enfrascar_ el entorno en el que vamos a trabajar. Virtualiza aplicaciones en un mismo sistema operativo, sin máquinas virtuales.

## Configuración de Docker

Hay que instalar Docker, registrarse en DockerHub y tener el entorno preparado para construir las imágenes. Si se quiere trabajar sin tener que usar ``sudo``, hay que añadir el usuario al grupo de Docker.

Si diese algún error relacionado con la red, editar el fichero ``/etc/default/docker`` como superusuario y descomentar la línea ``DOCKER_OPTS="--dns 8.8.8.8 --dns 8.8.4.4"``. Esto hará que los contenedores obtengan las DNS indicadas; en este caso, son las de Google.

### Dockerfile

Se podría decir que el Dockerfile es el corazón de la imagen. Con él logramos que la creación de la imagen de nuestra app siga unas pautas para que pueda ejecutarse sin problemas.

```dockerfile
# Uso una imagen oficial de Python
FROM python:3.6.8-slim

# Se pone el directorio de trabajo bajo /gestor-equipos
WORKDIR /gestor-equipos

# Copiar al contenedor en la ruta /gestor-equipos
COPY . /gestor-equipos

# Instalar dependencias
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Abrir puerto 80
EXPOSE 80

# Ejecutar la app al inicio del contenedor
CMD ["python", "app.py"]
```

Adicionalmente, es recomendable tener también el fichero ``.dockerignore``, que funciona de forma análoga al ``.gitignore``: marca una serie de ficheros o especifica wildcards para que estos archivos no se copien a la imagen. En mi caso, es el contenido del ``.gitignore`` además de otras reglas que he creído conveniente añadir.

```
*.md
runtime.txt
LICENSE
docs/
.travis.yml
```

### Construir la imagen

Para construir la imagen, dentro del directorio donde esté la aplicación, se hace:

``$ docker build --tag=<nombre> .``

Para ejecutarla y ver que funciona,

``$ docker run -p 5000:80 <nombre>``

La opción ``-p 5000:80`` mapea el puerto 5000 externo al 80 interno del contenedor.

### Subir imagen a DockerHub

Primero hay que loguearse si no se ha hecho ya.

``$ docker login``

Con la imagen que hemos construido previamente, la etiquetamos:

``$ docker tag <nombre> alexhzr/gestor-equipos:<tag>``

Finalmente, la subimos con

``$ docker push alexhzr/gestor-equipos:<tag>``

Para probar la mi imagen, ejecutar:

``$ docker run -p 5000:80 alexhzr/gestor-equipos:latest``

Mi repositorio de DockerHub está en esta URL: https://hub.docker.com/r/alexhzr/gestor-equipos

## Despliegue con Docker en Heroku
He montado otra app de Heroku: https://gestorequipos-docker.herokuapp.com/

### heroku.yml
Este fichero contiene información para que Heroku sepa cómo tratar la aplicación (al tratarse de un contenedor). Básicamente le dice que para construir, use Docker con el fichero Dockerfile, y la parte de run ya la conocemos.

```ỳaml
build:
  docker:
    web: Dockerfile
run:
web: gunicorn app:app
```

### Realizando el despliegue del contenedor

Para desplegar por contenedores, primero hay que hacer

``$ heroku container:login``

Ahora, para construir el Dockerfile y subir la imagen de Docker:

``$ heroku container:push web -a gestorequipos-docker``

Finalmente, desplegamos los cambios:

``$ heroku container:release web -a gestorequipos-docker``
