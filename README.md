# RDF-path-parser

## Ejecución

### Con Wikidata

1. Ejecutar `python wikidata_test.py`.
2. Escribir primera entidad en el formato **wd:{entidad}**, luego apretar **ENTER**.
3. Escribir segunda entidad en el formato **wd:{entidad}**, luego apretar **ENTER**.
4. Escribir largo del camino buscado con un número entero, luego apretar **ENTER**.
5. Esperar, el resultado se entregará en el archivo `output.nt`.

### Con grafo Propio

Para esto se necesita descargar la última version de blazegraph. La puede conseguir del siguiente link: [https://github.com/blazegraph/database/wiki/Main_Page]

1. Iniciar el servidor de blazegraoh con el comando `java -server -Xmx4g -jar blazegraph.jar`.
2. Cargar un grafo desde la interfaz de blazegraph en la pestaña Update.
3. Escribir primera entidad en el formato **wd:{entidad}**, luego apretar **ENTER**.
4. Escribir segunda entidad en el formato **wd:{entidad}**, luego apretar **ENTER**.
5. Escribir largo del camino buscado con un número entero, luego apretar **ENTER**.
6. Esperar, el resultado se entregará en el archivo `output.nt`.