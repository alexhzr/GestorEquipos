# Herramientas usadas
## Núcleo de la aplicación: lenguaje y framework
Voy a desarrollar el proyecto usando **Python 3.6 y Flask**. Necesito montar un servicio rápido y ligero, por lo que Flask me da justamente eso que pido. El paso de datos cliente-servidor y viceversa será en JSON. Django lo veo demasiado completo para hacer un microservicio. No voy a usar plantillas ni voy a tener un sistema complejo de clases, así que con Flask me basta y me sobra.

## Base de datos
Para la base de datos voy a usar **MongoDB**. Ya la he usado varias veces y me parece un sistema de DB bastante útil y potente. Dado que voy a emplearlo, voy a hacer uso de las colecciones y los documentos embebidos. No tiene sentido elegir un proyecto en MongoDB y hacerlo siguiendo la estructura de las bases de datos SQL, con relaciones y demás.

### Tratando las datos de la BD como objetos
De todas formas, he diseñado modelos para que mi aplicación use ORM. Para ello he usado **[Mongoengine](http://mongoengine.org/)**. Mongoengine es una "capa" por encima de PyMongo. Utiliza sus modelos y funciones, pero de manera más simple para el usuario final.

He incluido una librería externa, **[mongoengine_goodjson](https://github.com/hiroaki-yamamoto/mongoengine-goodjson)**. Básicamente lo que hace es poner el JSON que exportan los modelos de Mongoengine de una forma más _human readable_. ¿Esto qué quiere decir? Mongoengine, por defecto, al pasar un objeto a JSON, lo hace así:
```json
"partidas": [
	{
		"equipo_local": {"$oid": "5c3cb0396c4e1411ffa332ea"},
		"equipo_visitante": {"$oid": "5c3cb03a6c4e1411ffa332eb"},
		"fecha": { "$date": 1547121600000 },
		"lugar": "Estadio Santa Juana"
	},
```
Se puede observar que el el ``_id`` del campo está metido dentro del objeto ``equipo_local`` con la clave ``$oid``, cuando no debería de estar metido, sino aparecer a continuación, algo así:
```json
"partidas": [
	{
		"equipo_local" : "5c3cb0396c4e1411ffa332ea",
	},
]
```
En este caso aparece ``equipo_local``, pero si en vez de eso tuviésemos un campo ``_id`` ya estaría dando problemas, porque no podríamos acceder a la key ``_id`` por problemas del linter de JSON.

Ahora bien, al usar Mongoengine-Goodjson, el JSON generado es el siguiente:

```json
"partidas": [
	{
		"equipo_local": "5c3cb0396c4e1411ffa332ea",
		"equipo_visitante": "5c3cb03a6c4e1411ffa332eb",
		"fecha": "2019-01-10T12:00:00",
		"lugar": "Estadio Santa Juana"
	},
```

Nos quitamos el problema de los subcampos generados de un plumazo. Esto se puede hacer también sin necesidad de instalar una librería externa, pero hay que tocar los modelos y se quedan con un código engorroso, que ensucia lo que nos interesa del modelo que es su implementación.
