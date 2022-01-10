import statistics
import matplotlib.pyplot as plt
import numpy as np

def summary_audio_feature(df, feature, artist_name):
    """
    Brinda un resumen estadístico (mínimo, máximo, media) de los audio features de un artista en específico.

    Args:
        df: Dataframe con la información de la puntuación con cada feature y los nombres de los artistas.
        artist_name: Nombre del artista a analizar.
        feature: Audio feature de interés

    Returns:
        Mínimo, máximo y promedio del feature del artista.
    """
    mini = min(df[df["artists_name"]== artist_name][feature])
    maxi = max(df[df["artists_name"]== artist_name][feature])
    medi = round(statistics.mean(df[df["artists_name"]== artist_name][feature]),4)

    print("Para las tracks de {}, el mìnimo de la feature {} es: {}, el máximo es: {}, y el promedio es: {}".format(artist_name,feature, mini, maxi, medi))
    return mini, maxi, medi


def histogram_audio_feature_album(df, feature, artist_name):
    """
    Muestra los promedios de cierto audio feature para cada album del artista.

    Args:
        df: Dataframe con la información de la puntuación con cada feature, los nombres de los artistas y sus álbumes.
        artist_name: Nombre del artista a analizar.
        feature: Audio feature de interés

    Returns:
        Histograma 
    """

    resumen = df[(df["artists_name"]==artist_name)].groupby("album_name")[feature].mean().reset_index()
    
    plt.rcParams["figure.figsize"]=(18,5)
    plt.bar(resumen["album_name"], resumen[feature], align='center', alpha=0.5)
    plt.ylabel('Promedio '+feature)
    plt.xticks(rotation = 90)
    plt.title("Promedios del feature "+ feature +" para cada album de "+ artist_name)
    plt.show(block=False)
    plt.savefig('feature_prom_by_album.png')
    plt.close("all")


def histogram_artist_feature(df,artist_name, feature): 
    """
    Muestra la distribución de probabilidad de los valores de cierto audio feature para un artista

    Args:
        df: Dataframe con la información de la puntuación con cada feature y los nombres de los artistas.
        artist_name: Nombre del artista a analizar.
        feature: Audio feature de interés

    Returns:
        Histograma de probabilidad
    """
    
    audio_features = df[['artists_name','danceability', 'energy', 'key',
           'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness',
           'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature' ]]

    audio_features = audio_features.melt(id_vars=['artists_name'], 
            var_name="audio_features", 
            value_name="feature_value")

    heights,bins = np.histogram(audio_features[(audio_features["artists_name"] == artist_name) & (audio_features["audio_features"] == feature)]['feature_value'],bins=25)
    heights = heights/sum(heights)
    plt.bar(bins[:-1],heights,width=(max(bins) - min(bins))/len(bins), color="blue", alpha=0.5)
    plt.xticks(bins[:-1], rotation = 90)
    plt.ylabel('Probabilidad')
    plt.xlabel("Valores de "+ feature)
    plt.title("Densidad de probabilidad para los valores del feature "+ feature +"\npara el artista "+ artist_name)
    plt.show(block=False)
    plt.savefig('feature_hist_proba.png')
    plt.close("all") 



