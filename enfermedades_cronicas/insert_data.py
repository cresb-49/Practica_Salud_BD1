import pandas as pd

# Paths de entrada y salida
path_entrada = "E:\PROYECTOS\Practica_Salud_BD1\enfermedades_cronicas\data4.csv"
path_salida = "E:\PROYECTOS\Practica_Salud_BD1\enfermedades_cronicas\insert_enfermedades_cronicas.sql"

# Cargamos el archivo CSV
df = pd.read_csv(path_entrada)

# Aseguramos que las columnas sean del tipo correcto
df['id'] = df['id'].astype(int)
df['anio'] = df['anio'].astype(int)

if 'id_departamento' in df.columns:
    df['id_departamento'] = df['id_departamento'].apply(lambda x: f"{int(x):02d}" if pd.notnull(x) else x)
if 'id_municipio' in df.columns:
    df['id_municipio'] = df['id_municipio'].apply(lambda x: f"{int(x):04d}" if pd.notnull(x) else x)


# Creamos una lista para almacenar los inserts
inserts = []

# Iteramos por cada fila del DataFrame y creamos los inserts
for index, row in df.iterrows():
    id_row = row['id']
    anio = row['anio']
    id_departamento = row['id_departamento']
    id_municipio = row['id_municipio']
    codigo_cie = row['CIE']
    insert = f"INSERT INTO enfermedades_cronicas (id_enfermedades_cronicas, anio, id_departamento, id_municipio, codigo_cie) VALUES ({id_row}, '{id_departamento}', '{id_municipio}', '{codigo_cie}');"
    inserts.append(insert)

# Escribimos los inserts en el archivo de salida
with open(path_salida, 'w') as file:
    file.write('\n'.join(inserts))

print(f"Inserts guardados en {path_salida}")
