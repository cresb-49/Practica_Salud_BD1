import pandas as pd
import os

# Paths de entrada y salida
path_entrada = "E:\PROYECTOS\Practica_Salud_BD1\enfermedades_cronicas"
path_salida = "E:\PROYECTOS\Practica_Salud_BD1\enfermedades_cronicas"

# Cargamos el archivo CSV base
df = pd.read_csv(os.path.join(path_entrada, "data2.csv"))

# Creamos un nuevo DataFrame para los datos de género
genero_data = []

# ID inicial para las nuevas filas
new_id = 1

# Iteramos por cada fila del DataFrame original y creamos nuevas filas para cada género
for index, row in df.iterrows():
    genero_data.append([new_id, 1, row['hombres']])
    genero_data.append([new_id, 2, row['mujeres']])
    genero_data.append([new_id, 3, row['ignorado']])
    new_id += 1

# Convertimos la lista a un DataFrame
genero_df = pd.DataFrame(genero_data, columns=['id', 'id_genero', 'valor'])

# Guardamos el nuevo CSV con los datos de género
genero_df.to_csv(os.path.join(path_salida, "genero_datos.csv"), index=False)

# Eliminamos las columnas de género del DataFrame original
df = df.drop(columns=['hombres', 'mujeres', 'ignorado'])
if 'id_departamento' in df.columns:
    df['id_departamento'] = df['id_departamento'].apply(lambda x: f"{int(x):02d}" if pd.notnull(x) else x)

# Guardamos el CSV base actualizado
df.to_csv(os.path.join(path_salida, "atencion_por_departamento_v2.csv"), index=False)
