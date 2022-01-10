from timeit import default_timer as timer
import csv
import pandas as pd
from read_columns import get_column_pandas, get_column_csv_method



if __name__ == "__main__":
    
    time1 = list()
    rows = list()
    time2 = list()
    
    random.seed(10)

    for i in range(len(files)):
        start = timer()
        x = get_column_pandas(files[i], col)
        end = timer()
        time1.append(end - start)
        rows.append(len(x))


    for i in range(len(files)):
        start = timer()
        get_column_csv_method(files[i], col)
        end = timer()
        time2.append(end - start)


    plt.plot(rows, time1, label = "Time pandas")
    plt.plot(rows, time2, label = "Time csv method")
    plt.legend()
    plt.xlabel("Número de filas del dataset")
    plt.ylabel("Tiempo de ejecución (seg)")
    plt.show()

