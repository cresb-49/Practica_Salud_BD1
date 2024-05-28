import pandas as pd

# Ruta donde se guardarán los archivos
ruta_entrada = "/home/benjamin/PROYECTOS/Practica_Salud_BD1/conversion_vacunacion_vph/"
ruta_salida = "/home/benjamin/PROYECTOS/Practica_Salud_BD1/conversion_vacunacion_vph/"

# Leer el archivo que puede tener valores vacíos
df = pd.read_csv(ruta_entrada + 'datos_vacunacion_vph_v6.csv')

# Eliminar filas que contengan cualquier valor vacío
df_cleaned = df.dropna()

# Re-aplicar el formato de ceros a la izquierda para las columnas 'departamento' y 'municipio'
if 'id_departamento' in df_cleaned.columns:
    df_cleaned['id_departamento'] = df_cleaned['id_departamento'].apply(lambda x: f"{int(x):02d}" if pd.notnull(x) else x)
if 'id_municipio' in df_cleaned.columns:
    df_cleaned['id_municipio'] = df_cleaned['id_municipio'].apply(lambda x: f"{int(float(x)):04d}" if pd.notnull(x) else x)

# Guardar el DataFrame limpio en un nuevo archivo CSV
df_cleaned.to_csv(ruta_salida + 'datos_vacunacion_vph_v7.csv', index=False)
