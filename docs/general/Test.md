# Tests
Para pasar los test he usado **[Pytest 3](https://docs.pytest.org/en/latest/)**. Lo he preferido antes que otros porque, a grandes rasgos, es más simple que unittest. No es necesario crear una clase de test, simplemente puedes escribir las funciones de test en un fichero y ya está. [Aquí](https://github.com/renzon/pytest-vs-unittest) hay una comparación de funcionalidades entre unittest y Pytest en las que gana Pytest.

Para testear el programa, ejecutar:

`$ pytest-3 test.py`

Además, el proyecto está configurado para que integración continua con [Travis-CI](https://travis-ci.org/). Aparte de registrarse en Travis-CI, enlazar tu cuenta de GitHub y seleccionar el proyecto a integrar, hace falta crear un fichero: [.travis.yml](https://github.com/alexhzr/GestorEquipos/blob/master/.travis.yml)

```yaml
language: python
services:
  - mongodb
python:
  - "3.6.6"
cache: pip
install:
  - pip install -r requirements.txt
script:
  - pytest test.py
```

Este fichero le indica a Travis qué necesita para ejecutar correctamente los tests.

  - ``language``: El lenguaje en el que está escrito el proyecto.
  - ``services``: Si el proyecto tiene algún servicio específico, se indica aquí. En mi caso, MongoDB.
  - ``python``: Versión a ejecutar de Python.
  - ``cache``: Lo que se va a utilizar para meter en caché las dependencias.
  - ``install``: Qué se usa para instalar dependencias.
  - ``script``: El script que lanza los tests.
