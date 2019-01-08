# Configuración para desplegar en Heroku

Enlace a la app: [](https://gestor-equipos.herokuapp.com/)

Yo he configurado Heroku para que despliegue automáticamente vía GitHub. Es decir, con cada commit, se despliega la última versión.

![](https://imgur.com/WOtjYDp.png)

### Ficheros

#### Procfile
El procfile indica qué lanzar. En este caso, al ser una webapp de Python, usará gunicorn:

```
web: gunicorn app:app
```

#### runtime.txt
Indica qué necesita para lanzar. Como es Python 3.6, tendrá:

```
python-3.6.6
```

Es **muy importante** añadir ```gunicorn``` al fichero ```requeriments.txt```, sino, Heroku no instalará Gunicorn y por tanto no lanzará la aplicación.
