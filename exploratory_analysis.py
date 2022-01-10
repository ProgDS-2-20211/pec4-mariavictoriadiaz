import pandas as pd

__all__ = [ 'count_tracks_artist',
            'count_track_contain',
           'count_tracks_years',
           'track_popularity',
           'artists_every_decade',
           ]

def count_tracks_artist(df,artist_name):
    """
    Calcula la cantidad de tracks de cierto artista

    Args:
        df: Dataframe con la información de los tracks y los artistas.
        artist_name: Nombre del artista a analizar.
        
    Returns:
        Cantidad de tracks de un artista. 
    """
    print("Hay {} tracks de {}".format(len(df[df["artists_name"] == artist_name]), artist_name))
    return len(df[df["artists_name"] == artist_name])



def count_track_contain(df,track_name):
    """
    Calcula la cantidad de tracks que contienen cierta palabra en su nombre.

    Args:
        df: Dataframe con la información de los tracks.
        track_name: Palabra a buscar entre los nombres de los tracks.
        
    Returns:
        Cantidad de tracks cuyo nombre contiene la palabra especificada. 
    """
    print("Hay {} tracks que contienen la palabra {} en su nombre".format(len(df[df['track_name'].str.contains(track_name,  case=False)]), track_name))
    return len(df[df['track_name'].str.contains(track_name,  case=False)])



def count_tracks_years(df,year):
    """
    Calcula la cantidad de tracks que se lanzaron en cierto año

    Args:
        df: Dataframe con la información de los tracks y el año de lanzamiento.
        year: año del cual se quiere tener información.
        
    Returns:
        Cantidad de tracks que salieron en el año especificado. 
    """
    print("Hay {} tracks que salieron en el año {}".format(len(df[df['release_year'] == year]), year))
    return len(df[df['release_year'] == year])




def track_popularity(df,year):
    """
    Busca y muestra el track más popular en los últimos años 

    Args:
        df: Dataframe con la información de los tracks y el año de lanzamiento.
        year: cantidad de años hacia atrás que se quiere averiguar.
        
    Returns:
        Nombre del track más popular de los últimos años. 
    """
    ultimos_diez = df[df["release_year"] >= year]
    print("El track más popular en los últimos {} años fue: {}".format(year, ultimos_diez.iloc[ultimos_diez['track_popularity'].idxmax()]["track_name"]))
    return  ultimos_diez.iloc[ultimos_diez['track_popularity'].idxmax()]["track_name"]



def artists_every_decade(df, year, n_decades):

    """
    Muestra los artistas que han sacado canciones en cada una de las últimas décadas

    Args:
        df: Dataframe con la información de los tracks, los artistas, y la fecha de lanzamiento.
        year: Año desde el cual se quiere averiguar.
        n_decades: Número de décadas que han pasado desde el año especificado.
        
    Returns:
        Lista con los artistas que sacaron tracks en cada década 
    """
    
    df["decade"]= 0
    año=year
    
    for i in range(1,n_decades+1):
        df.loc[(df["release_year"]>=year) & (df["release_year"] <year+10), "decade"]= i
        year = year+10

    artists = list(df["artists_name"].unique())
    count = list()
    for i in range(len(artists)):
        tracksj = df[df["artists_name"]== artists[i]]["decade"].unique()
        if ((len(tracksj) == len(df["decade"].unique())-1) & (min(tracksj) == 1) & (max(tracksj) == max(df["decade"]))):
            count.append(artists[i])  
            
    print("Los artistas que sacaron tracks en cada década desde {}, son {}".format(año,count))
    return count





