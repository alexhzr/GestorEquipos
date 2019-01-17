# Docker
Docker nos da la posibilidad de _enfrascar_ el entorno en el que vamos a trabajar. Virtualiza aplicaciones en un mismo sistema operativo, sin máquinas virtuales.

## Configuración de Docker

Hay que instalar Docker, registrarse en DockerHub y tener el entorno preparado para construir las imágenes. Si se quiere trabajar sin tener que usar ``sudo``, hay que añadir el usuario al grupo de Docker.

Si diese algún error relacionado con la red, editar el fichero ``/etc/default/docker`` como superusuario y descomentar la línea ``DOCKER_OPTS="--dns 8.8.8.8 --dns 8.8.4.4"``. Esto hará que los contenedores obtengan las DNS indicadas; en este caso, son las de Google.

### Dockerfile

Se podría decir que el Dockerfile es el corazón de la imagen. Con él logramos que la creación de la imagen de nuestra app siga unas pautas para que pueda ejecutarse sin problemas.

```
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
