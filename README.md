# Mountais Are Calling

## ¿De que se trata?
_'Mountains are calling'_ es una aplicación que se encarga de recoger los datos de vías y lugares de escalada a través de la página **Mountain Project**, y usa la *API* de **Mapbox** para mostrarlos en un mapa interactivo. En principio también daré la posibilidad de ver los precios de **blablacar**, aunque más adelante si consigo los permisos necesarios también mostrará los lugares de hospedaje más cercanos además de poder reservarlos. 

## ¿Cómo va a funcionar?
Haré uso de las *API* como **MountainProject** para recopilar las ubicaciones y las fechas de subida de las mismas, y después las usaré en la *API* de **Mapbox** además de **blablacar**.

### APIs
- [MapBox](https://docs.mapbox.com/api/)
- [MountainProject](https://www.mountainproject.com/data)
- [Blablacar](https://dev.blablacar.com/docs/versions/1.0)
- [NewsApi](https://newsapi.org/)
- [Youtube Data API](https://developers.google.com/youtube/v3/)
- [Yandex Translate](https://tech.yandex.com/translate/doc/dg/concepts/About-docpage/)

**Todas estas APIs ofrecen una respuesta en formato _JSON_ y su modo de autenticación es por key**
#### Pequeño programa en la [terminal](ConsultasTerminal.py)

### Estructura de la página

Constará de las siguientes rutas:
- "**/**" o raiz, será la página de inicio y tendrá los distintos botones y enlaces a las distintas rutas.
- "**/busqueda**": esta página tendrá un formulario en el cual introduciremos una ciudad, un país y un número de kilómetros a la redonda, y nos mostrará (en la ruta "**/blablacar**")en un mapa qué vías/bloques de escalada se encuentran en ese radio. Así como un botón que nos abrirá un formulario para introducir un origen y enseñarnos las opciones que tenemos de ir allí con **blablacar** ordenadas por precio.
- "**/blablacar**": se trata de una página producto de un formulario que contiene un mapa con diversas localizaciones así como otro posible formulario para calcular los costes de transportes (si hay) desde un origen a través de la *API de blablacar*.
- "**/noticias**": Muestra las noticias más recientes relacionadas con la Federación Internacional de la Escalada Deportiva (_ifsc_), así como sus competiciones y competidores.
- "**/youtube**": Muestra los 3 videos más recientes de una lista de 5 canales relacionados con la escalada que recomiendo personalmente.

### Aplicación web en heroku
Algunas capturas de la página desplegada en heroku.

<a href="https://imgur.com/ymPVKkX"><img src="https://i.imgur.com/ymPVKkX.png" title="source: imgur.com" /></a>

<a href="https://imgur.com/8LKOqj5"><img src="https://i.imgur.com/8LKOqj5.png" title="source: imgur.com" /></a>

<a href="https://imgur.com/qE5ACK1"><img src="https://i.imgur.com/qE5ACK1.png" title="source: imgur.com" /></a>

<a href="https://imgur.com/3sqFjec"><img src="https://i.imgur.com/3sqFjec.png" title="source: imgur.com" /></a>

<a href="https://imgur.com/CMzsDyF"><img src="https://i.imgur.com/CMzsDyF.png" title="source: imgur.com" /></a>

<a href="https://imgur.com/psGAAkG"><img src="https://i.imgur.com/psGAAkG.png" title="source: imgur.com" /></a>

<a href="https://imgur.com/ropEiSE"><img src="https://i.imgur.com/ropEiSE.png" title="source: imgur.com" /></a>

