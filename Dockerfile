# Uso una imagen oficial de Python
FROM python:3.6.8-slim

# Se pone el directorio de trabajo bajo /gestor-equipos
WORKDIR /gestor-equipos

# Instalar dependencias. He movido esta línea más arriba para que se guarden en caché las dependencias.
COPY requirements.txt /gestor-equipos
RUN pip3 install --upgrade pip
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Copiar la aplicación al contenedor en la ruta /gestor-equipos. Ahora no uso .dockerignore, sino que sólo copio los ficheros necesarios.
COPY app.py /gestor-equipos
COPY modelos/* /gestor-equipos/modelos/

# Abrir puerto 80
EXPOSE 80

# Ejecutar la app al inicio del contenedor
CMD ["gunicorn", "-b :5000", "app:create_app()"]
