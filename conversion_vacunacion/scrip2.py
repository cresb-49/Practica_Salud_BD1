import pandas as pd


# Ruta donde se guardarán los archivos
ruta_entrada = "/home/benjamin/PROYECTOS/Practica_Salud_BD1/conversion_vacunacion/"
ruta_salida = "/home/benjamin/PROYECTOS/Practica_Salud_BD1/conversion_vacunacion/"

# Leer el archivo CSV modificado
df = pd.read_csv(ruta_entrada+'datos_vacunacion_v1.csv')

# Función para crear un archivo CSV con valores únicos y un ID incremental


def crear_csv_unico(columna, nombre_archivo, ruta_archivos):
    # Extraer los valores únicos y resetear el índice para obtener un ID incremental desde 1
    df_unico = pd.DataFrame(df[columna].unique(), columns=[columna])
    df_unico.reset_index(inplace=True, drop=False)
    df_unico.index += 1  # Hacer que los índices empiecen en 1
    df_unico.rename(columns={'index': 'id'}, inplace=True)
    # Guardar en un archivo CSV en la ruta especificada
    df_unico.to_csv(f'{ruta_archivos}{nombre_archivo}.csv', index=False)


# Crear archivos CSV para 'area_salud', 'vacuna', y 'num_dosis'
crear_csv_unico('area_salud', 'area_salud', ruta_salida)
crear_csv_unico('vacuna', 'vacuna', ruta_salida)
crear_csv_unico('num_dosis', 'numero_dosis', ruta_salida)
