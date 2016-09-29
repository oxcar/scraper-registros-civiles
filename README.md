# Scraper de Registros Civiles

Scripts para [scrapear](https://es.wikipedia.org/wiki/Web_scraping) la ubicación de los Registros Civiles (RRCC) de la web [http://www.registro-civil.com.mx/](http://www.registro-civil.com.mx/).

## Requerimientos

* Python 3
* Librería BeautifulSoup 4

## Como funciona

El fichero `urls.txt` contiene las URLs donde están los listados de los RRCC de las entidades.

### Scrapeo de ubicaciones

El script `scrape_rcs.py` lee las urls del fichero `urls.txt` y extrae la información de las **oficialias**, contenidas en una tabla, y las guarda en ficheros [CSV](https://es.wikipedia.org/wiki/CSV), uno por cada URL en la carpeta `data/not-geocoded`.

Estos ficheros CSV contienen la información de los RRCC, con los campos:

* entidad
* nombre
* direccion
* latitud (vacío)
* longitud (vacío)
* contacto

### Geocodificación de las ubicaciones

Los ficheros CSV en la carpeta `data/not-geocoded` no contienen ubicación (latitud, longitud), solo la dirección.

## Notas
La web scrapeada no contiene información referente a los Registros Civiles de la entidad de Colima.

A su vez tiene dos listados diferentes para Guadalajara y Jalisco, y para Monterrey y Nuevo León.