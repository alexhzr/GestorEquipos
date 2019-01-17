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
