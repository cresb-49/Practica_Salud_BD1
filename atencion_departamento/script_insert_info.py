import pandas as pd

# Paths de entrada y salida
path_entrada = "E:/PROYECTOS/Practica_Salud_BD1/atencion_departamento/atencion_por_departamento_v2.csv"
path_salida = "E:/PROYECTOS/Practica_Salud_BD1/atencion_departamento/inserts_atencion_por_departamento.sql"

# Cargamos el archivo CSV
df = pd.read_csv(path_entrada)

# Aseguramos que las columnas sean del tipo correcto
df['id_atencion_por_departamento'] = df['id_atencion_por_departamento'].astype(int)
df['id_tipo_servicio'] = df['id_tipo_servicio'].astype(int)

if 'id_departamento' in df.columns:
    df['id_departamento'] = df['id_departamento'].apply(lambda x: f"{int(x):02d}" if pd.notnull(x) else x)


# Creamos una lista para almacenar los inserts
inserts = []

# Iteramos por cada fila del DataFrame y creamos los inserts
for index, row in df.iterrows():
    id_row = row['id_atencion_por_departamento']
    id_departamento = row['id_departamento']
    id_codigo_cie = row['codigo_cie']
    id_tipo_servicio = row['id_tipo_servicio']
    insert = f"INSERT INTO atencion_por_departamento (id_atencion_por_departamento, id_departamento, codigo_cie, id_tipo_servicio) VALUES ({id_row}, '{id_departamento}', '{id_codigo_cie}', {id_tipo_servicio});"
    inserts.append(insert)

# Escribimos los inserts en el archivo de salida
with open(path_salida, 'w') as file:
    file.write('\n'.join(inserts))

print(f"Inserts guardados en {path_salida}")
