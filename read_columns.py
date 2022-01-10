import pandas as pd
import csv

def get_column_pandas(file, col):
    """
    Lee una columna de una base de datos mediante la librería pandas

    Args:
        file: Ruta del archivo a leer.

    Returns:
        Lista con los valores de la columna de la base de datos 
    """
    df = pd.read_csv(file, sep = ";", usecols= [col])
    return list(df[col])

    


def get_column_csv_method(file, col):
    """
    Lee una columna de una base de datos mediante la librería csv

    Args:
        file: Ruta del archivo a leer.

    Returns:
        Lista con los valores de la columna de la base de datos 
    """
  
    with open(file, newline='') as csvfile:
        data = csv.DictReader(csvfile, delimiter=';')
        cols = []
        for row in data:
            cols.append(row[col])
    return cols


