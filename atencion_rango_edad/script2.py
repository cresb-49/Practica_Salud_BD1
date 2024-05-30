import pandas as pd
import os

# Paths de entrada y salida
path_entrada = "E:/PROYECTOS/Practica_Salud_BD1/atencion_rango_edad"
path_salida = "E:/PROYECTOS/Practica_Salud_BD1/atencion_rango_edad"

# Cargamos el archivo CSV base
df = pd.read_csv(os.path.join(path_entrada, "atencion_por_rango_edad_v1.csv"))

# Creamos un nuevo DataFrame para los datos de género
genero_data = []

# ID inicial para las nuevas filas
new_id = 1

# Iteramos por cada fila del DataFrame original y creamos nuevas filas para cada género
for index, row in df.iterrows():
    genero_data.append([new_id, 1, row['hombres']])
    new_id += 1
    genero_data.append([new_id, 2, row['mujeres']])
    new_id += 1
    genero_data.append([new_id, 3, row['ignorado']])
    new_id += 1

# Convertimos la lista a un DataFrame
genero_df = pd.DataFrame(genero_data, columns=['id', 'id_genero', 'valor'])

# Guardamos el nuevo CSV con los datos de género
genero_df.to_csv(os.path.join(path_salida, "genero_datos.csv"), index=False)

# Eliminamos las columnas de género del DataFrame original
df = df.drop(columns=['hombres', 'mujeres', 'ignorado'])

# agregmos la columna 'id' al DataFrame original y empezamos desde 1
df['id'] = range(1, len(df) + 1)

# Guardamos el CSV base actualizado
df.to_csv(os.path.join(path_salida, "atencion_por_rango_edad_v2.csv"), index=False)



