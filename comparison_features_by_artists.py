import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

__all__ = [ 'artists_features_compara',
            'similarities_features',
          ]

def artists_features_compara(df,artists_names, feature): 

    """
    Compara un audio feature seleccionado entre dos artistas en particular

    Args:
        df: Dataframe con la información de la puntuación con cada feature y los nombres de los artistas.
        artists_names: Nombre de los dos artistas a analizar.
        feature: Audio feature de interés

    Returns:
        histograma: Histogramas de densidad de probabilidad (superpuestos) del feature para los dos artistas.
    """
    
    audio_features = df[['artists_name','danceability', 'energy', 'key',
           'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness',
           'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature' ]]

    audio_features = audio_features.melt(id_vars=['artists_name'], 
            var_name="audio_features", 
            value_name="feature_value")
    plt.rcParams["figure.figsize"]=(20,5)

    heights,bins1 = np.histogram(audio_features[(audio_features["artists_name"] == artists_names[0]) & (audio_features["audio_features"] == feature)]['feature_value'],bins=25)
    heights = heights/sum(heights)
    plt.bar(bins1[:-1],heights,width=(max(bins1) - min(bins1))/len(bins1), color="blue", alpha=0.5)
    
    heights,bins2 = np.histogram(audio_features[(audio_features["artists_name"] == artists_names[1]) & (audio_features["audio_features"] == feature)]['feature_value'],bins=25)
    heights = heights/sum(heights)
    plt.bar(bins2[:-1],heights,width=(max(bins2) - min(bins2))/len(bins2), color="red", alpha=0.5)

    plt.xticks(np.concatenate((bins1[:-1],bins2[:-1])),rotation = 90)
    plt.ylabel('Probabilidad')
    plt.xlabel("Valores de "+ feature)
    plt.title("Densidad de probabilidad para los valores del feature "+ feature +"\npara los artistas "+ artists_names[0] + " y " + artists_names[1])
    plt.show(block=False)
    plt.savefig('hist_proba_two_artists.png')
    plt.close("all")


def similarities_features(df,artists_names,metric):

    """
    Compara todos los audio features entre artistas especificados

    Args:
        df: Dataframe con la información de la puntuación con cada feature y los nombres de los artistas.
        artists_names: Nombre de los artistas a analizar (dos o más).
        metric: Métrica de comparación.

    Returns:
        heatmap: Heatmap que muestra las distancias (según la métrica escogida) entre los artistas especificados.
    """

    audio_features = df[['artists_name','danceability', 'energy', 'key',
               'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness',
               'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature' ]]
    
    audio_features = audio_features[audio_features["artists_name"].isin(artists_names)]

    medias = audio_features.groupby("artists_name").mean().reset_index()

    distances = pdist(medias.iloc[:,1:].values, metric = metric)
    matrix_distances = squareform(distances)
    matrix_distances = pd.DataFrame(matrix_distances, columns = medias["artists_name"], index = medias["artists_name"])

    fig,ax=plt.subplots(figsize=(10,7))
    sns.heatmap(matrix_distances, cmap = "YlGnBu")
    ax.set_title("Matriz de similaridad con métrica "+ metric)
    fig.savefig('similaridad.png')   # save the figure to file
    plt.close(fig)    

