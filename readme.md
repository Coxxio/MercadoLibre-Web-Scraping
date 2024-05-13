# Proyecto de Web Scraping


Proyecto de Web Scaping para MercadoLibre obteniendo el titulo, precio, si cuenta con envio gratis, link del articulo y link de la imagen,
guarda los datos en un archivo csv para su posterior analisis.

</br>

---
## Requisitos

Debe usarse con Python 3.x y las siguientes librerias

* Requests
* BeautifulSoup4
* Pandas

Para instalar use el siguiente comando:

```console
pip install -r requirements.txt
```

</br>

---

## Uso

Para ejecutar el scraper, en la raiz del proyecto ejecute el siguiente comando:

```console
py main.py
```
O
```console
python3 main.py
```

Esto iniciará el proceso de scraping y creará un archivo "mercadolibre_scraped_data_<span>nombre del articulo<span>.csv" en el directorio "data" con todos los datos extraídos.

---

### Tecnologías utilizadas

* Python
* Requests
* Beautiful Soup
* Pandas