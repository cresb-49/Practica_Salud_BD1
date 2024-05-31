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
    # ------------------------------
    genero_data.append([new_id, 2, 1, row['F4']])
    genero_data.append([new_id, 1, 1, row['M4']])
    # ------------------------------
    genero_data.append([new_id, 2, 2, row['F5']])
    genero_data.append([new_id, 1, 2, row['M5']])
    # ------------------------------
    genero_data.append([new_id, 2, 3, row['F6']])
    genero_data.append([new_id, 1, 3, row['M6']])
    # ------------------------------
    genero_data.append([new_id, 2, 4, row['F7']])
    genero_data.append([new_id, 1, 4, row['M7']])
    # ------------------------------
    genero_data.append([new_id, 2, 5, row['F9']])
    genero_data.append([new_id, 1, 5, row['M9']])
    # ------------------------------
    genero_data.append([new_id, 2, 6, row['F10']])
    genero_data.append([new_id, 1, 6, row['M10']])
    # ------------------------------
    genero_data.append([new_id, 2, 7, row['F11']])
    genero_data.append([new_id, 1, 7, row['M11']])
    # ------------------------------
    genero_data.append([new_id, 2, 8, row['F12']])
    genero_data.append([new_id, 1, 8, row['M12']])
    # ------------------------------
    genero_data.append([new_id, 2, 9, row['F13']])
    genero_data.append([new_id, 1, 9, row['M13']])
    # ------------------------------
    genero_data.append([new_id, 2, 10, row['F14']])
    genero_data.append([new_id, 1, 10, row['M14']])
    # ------------------------------
    genero_data.append([new_id, 2, 11, row['F15']])
    genero_data.append([new_id, 1, 11, row['M15']])
    # ------------------------------
    genero_data.append([new_id, 2, 12, row['F16']])
    genero_data.append([new_id, 1, 12, row['M16']])
    # ------------------------------
    genero_data.append([new_id, 2, 13, row['F17']])
    genero_data.append([new_id, 1, 13, row['M17']])
    # ------------------------------
    genero_data.append([new_id, 2, 14, row['F18']])
    genero_data.append([new_id, 1, 14, row['M18']])
    # ------------------------------
    genero_data.append([new_id, 2, 15, row['F18']])
    genero_data.append([new_id, 1, 15, row['M18']])
    new_id += 1

# Convertimos la lista a un DataFrame
genero_df = pd.DataFrame(genero_data, columns=['id_linea', 'id_genero', 'id_rango_edad', 'valor'])

# Guardamos el nuevo CSV con los datos de género
genero_df.to_csv(os.path.join(path_salida, "genero_datos.csv"), index=False)


if 'id_departamento' in df.columns:
    df['id_departamento'] = df['id_departamento'].apply(
        lambda x: f"{int(x):02d}" if pd.notnull(x) else x)
if 'id_municipio' in df.columns:
    df['id_municipio'] = df['id_municipio'].apply(
        lambda x: f"{int(x):02d}" if pd.notnull(x) else x)

df.index = df.index + 1
# Guardamos el CSV base actualizado
df.to_csv(os.path.join(
    path_salida, "data3.csv"), index=True)
