# Configuración para desplegar en Heroku

Enlace a la app: https://gestor-equipos.herokuapp.com/

### ¿Por qué Heroku?
Heroku me ha parecido de lejos el más sencillo y rápido para desplegar rápidamente una aplicación. Hace años probé OpenShift y la verdad es que iba muy bien, pero ahora han cambiado mucho la manera de hacer las cosas, empezando por el registro. Desde que apliqué hasta que me concedieron la posibilidad de usar la plataforma, pasaron más de dos semanas, por lo que los rechacé totalmente.

## Crear la aplicación
A la hora de crear la aplicación en el PaaS se puede hacer de dos formas:
1.  Mediante web
2. Mediante Heroku CLI

Yo personalmente, para esta aplicación, lo he hecho vía web y es muy sencillo. Basta simplemente con crearla, asignarle un nombre y una región y ya estaría lista. Ahora bien, en este punto no tenemos nada. Hay que configurar cómo queremos que se despliegue. Yo he optado por integrar con GitHub, lo cual voy a explicar a continuación.

## Integrado con GitHub

Con cada commit, se despliega la última versión. Basta con entrar al _dashboard_ de Heroku, acceder a la aplicación, y bajo _Deployment method_, escoger GitHub. Pasará por un proceso de autenticación en el que seleccionaremos el repositorio que pertenece a la aplicación y posteriormente elegiremos la rama. Normalmente será la rama ``master``.

![](https://imgur.com/WOtjYDp.png)

## Despliegue con Heroku CLI

Como se comenta en el temario, hay que inicializar un repositorio con ``git init`` bajo el directorio de trabajo en el que esté la aplicación, añadir un ``origin`` con ``heroku git:remote -a nombre-aplicación`` y trabajar con git normalmente. A la hora de subir los ficheros, se hace con ``git push heroku master`` o la rama que se tenga configurada.

### Ficheros de configuración

#### Procfile
El procfile indica qué lanzar. En este caso, al ser una webapp de Python, usará gunicorn:

```
web: gunicorn app:app
```

#### runtime.txt
Indica qué necesita para lanzar. Como es Python 3.6.7, tendrá:

```
python-3.6.7
```

#### requeriments.txt
    pytest==3.8.1
    flask
    pymongo>=2.7.1
    six>=1.10.0
    mongoengine
    mongoengine_goodjson
    gunicorn
Indica qué módulos adicionales necesita nuestra aplicación para funcionar. Es **muy importante** añadir ```gunicorn``` al fichero ```requeriments.txt```, sino, Heroku no instalará Gunicorn y por tanto no lanzará la aplicación.
