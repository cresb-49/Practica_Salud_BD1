import pandas as pd

# Ruta donde se guardarán los archivos
ruta_entrada = "/home/benjamin/PROYECTOS/Practica_Salud_BD1/conversion_vacunacion/"
ruta_salida = "/home/benjamin/PROYECTOS/Practica_Salud_BD1/conversion_vacunacion/"

# Leer el archivo que puede tener valores vacíos
df = pd.read_csv(ruta_entrada + 'datos_vacunacion_v3.csv')

# Eliminar filas que contengan cualquier valor vacío
df_cleaned = df.dropna()

# Re-aplicar el formato de ceros a la izquierda para las columnas 'departamento' y 'municipio'
if 'departamento' in df_cleaned.columns:
    df_cleaned['departamento'] = df_cleaned['departamento'].apply(lambda x: f"{int(x):02d}" if pd.notnull(x) else x)
if 'municipio' in df_cleaned.columns:
    df_cleaned['municipio'] = df_cleaned['municipio'].apply(lambda x: f"{int(float(x)):04d}" if pd.notnull(x) else x)

# Guardar el DataFrame limpio en un nuevo archivo CSV
df_cleaned.to_csv(ruta_salida + 'datos_vacunacion_v4.csv', index=False)
