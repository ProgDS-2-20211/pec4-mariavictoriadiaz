# Paquete **pec4-mariavictoriadiaz**

El paquete **pec4-mariavictoriadiaz** está creado para apoyar el proceso de selección de los artistas musicales más influyentes hasta el momento. 

Brinda un resumen de: las canciones de un artista en particular; artistas que no paran de lanzar canciones décadas tras décadas; canciones que se lanzaron en cierta época; comparación de audio features entre artistas; descripción de audio features por artista, etc.


## Instalación

$ pip install pec4-mariavictoriadiaz


## Ejemplo:

```
from pec4-mariavictoriadiaz.preprocessing import unzip_data, normalize_data, join_datasets
from pec4-mariavictoriadiaz.exploratory_analysis import count_tracks_artist, count_track_contain, count_tracks_years,track_popularity,artists_every_decade
from pec4-mariavictoriadiaz.one_artist_one_feature import summary_audio_feature
from pec4-mariavictoriadiaz.comparison_features_by_artists import artists_features_compara, similarities_features
from pec4-mariavictoriadiaz.one_artist_one_feature import summary_audio_feature, histogram_audio_feature_album, histogram_artist_feature, 

```

1. ¿Cuál es la canción con más popularidad de los últimos 10 años?

```
track_popularity(df,year = 10)
```

2. ¿Cuántas canciones contienen la palabra ‘police’en el título?

```
count_track_contain(df,track_name = "police")
```

3. Mostrar por pantalla  la similitud euclidiana comparando los artistas Metallica,Extremoduro,AC/DCyHans Zimmer.

```
similarities_features(df,artists_name = ["Metallica","Extremoduro","Ac/Dc","Hans Zimmer"],metric = "euclidean")
```

## Test  y coverage

Desde la carpeta del proyecto, ejecutar: 

```
$ coverage run -m unittest tests/test.py 
```

Y para ver el reporte de coverage:

```
$ coverage report
```

## Licencia

Paquete amparado bajo la licencia de 3 cláusulas BSD 

Copyright (c) 2022, Maria Victoria Díaz
Todos los derechos reservados.
