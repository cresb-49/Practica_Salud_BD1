import pandas as pd

# Ruta donde se guardará el archivo
ruta_entrada = "/home/benjamin/PROYECTOS/Practica_Salud_BD1/conversion_vacunacion/"
ruta_salida = "/home/benjamin/PROYECTOS/Practica_Salud_BD1/conversion_vacunacion/"

# Leer el archivo de vacunación que ya tiene las columnas de ID
df = pd.read_csv(ruta_entrada + 'datos_vacunacion_v2.csv')

# Ajustar el formato de las columnas 'departamento' y 'municipio' para que tengan ceros a la izquierda
df['departamento'] = df['departamento'].apply(lambda x: f"{int(x):02d}" if pd.notnull(x) else x)
df['municipio'] = df['municipio'].apply(lambda x: f"{int(float(x)):04d}" if pd.notnull(x) else x)

# Guardar el DataFrame modificado de nuevo en un archivo CSV
df.to_csv(ruta_salida + 'datos_vacunacion_v3.csv', index=False)
