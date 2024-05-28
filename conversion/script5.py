import pandas as pd

# Ruta donde se guardarán los archivos
ruta_entrada = "/home/benjamin/PROYECTOS/Practica_Salud_BD1/conversion/"
ruta_salida = "/home/benjamin/PROYECTOS/Practica_Salud_BD1/conversion/"

# Leer el archivo original de vacunación que puede tener valores vacíos
df = pd.read_csv(ruta_entrada + 'datos_vacunacion_v3.csv')

# Eliminar filas que contengan cualquier valor vacío
df_cleaned = df.dropna()

# Guardar el DataFrame limpio en un nuevo archivo CSV
df_cleaned.to_csv(ruta_salida + 'datos_vacunacion_v4.csv', index=False)
