import zipfile as zf
import pandas as pd
import os


def unzip_data(root):
    """
    Descomprimir los datos

    Args:
       root: Ruta del archivo zip
    """

    zip_with_multiple_files = root
    with zf.ZipFile(zip_with_multiple_files, 'r') as zip_f:
        zip_f.extractall()



def normalize_data(artists_norm, tracks_norm, albums_norm):
    
    """
    Estandariza las bases de datos de artistas, tracks y albums. (Corrige nombres, identifica y completa datos faltantes, estandariza el nombre de los artistas)

    Args:
        artists_norm: Base de datos con la información de los artistas.
        tracks_norm: Base de datos con la información de las canciones.
        albums_norm: Base de datos con la información de los álbumes.
        
    Returns:
        Bases de datos normalizadas 
    """
    
    artists_norm['name'] = artists_norm['name'].str.title()
    
    artists_norm.rename(columns={'name': 'artist_name'}, inplace=True)
    albums_norm.rename(columns={'name': 'album_name'}, inplace=True)
    tracks_norm.rename(columns={'name': 'track_name'}, inplace=True)

    artists_norm.rename(columns={'popularity': 'artist_popularity'}, inplace=True)
    albums_norm.rename(columns={'popularity': 'album_popularity'}, inplace=True)
    tracks_norm.rename(columns={'popularity': 'track_popularity'}, inplace=True)

    print ("Existen {} tracks".format(len(tracks_norm['track_id'].unique())))
    if tracks_norm['popularity'].isnull().values.any():
        print ("De los cuales, hay {} sin valor de popularidad".format(tracks_norm['popularity'].isnull().sum()))
        tracks_norm['popularity'].fillna(value =  tracks_norm['popularity'].mean(), inplace = True)
    else:
        tracks_norm['popularity'] = tracks_norm['popularity']
 
    return artists_norm, tracks_norm, albums_norm
  


def join_datasets(artists_norm, tracks_norm, albums_norm):
    """
    Une las bases de datos de artistas, tracks y albumes e  imprime el nro. de columnas de la base final.
    Args:
        artists_norm: Base de datos con la información de los artistas.
        tracks_norm: Base de datos con la información de las canciones.
        albums_norm: Base de datos con la información de los álbumes.
        
    Returns:
        Base de datos final 
    """
    tracks = pd.merge(artists_norm,pd.merge(albums_norm,tracks_norm, on = ["artist_id", "album_id"]), on = "artist_id")
    tracks.to_csv("data/tracks.csv", sep=';', encoding='utf-8')
    print ("Hay {} columnas en el dataset final".format(len(tracks.columns)))
    return tracks








