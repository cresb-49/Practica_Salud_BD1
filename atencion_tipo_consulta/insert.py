import pandas as pd

# Paths de entrada y salida
path_entrada = "E:/PROYECTOS/Practica_Salud_BD1/atencion_tipo_consulta/atencion_por_tipo_consulta_v1.csv"
path_salida = "E:/PROYECTOS/Practica_Salud_BD1/atencion_tipo_consulta/inserts_atencion_por_tipo_consulta.sql"

# Cargamos el archivo CSV
df = pd.read_csv(path_entrada)

# Aseguramos que las columnas sean del tipo correcto
df['id_atencion_por_tipo_consulta'] = df['id_atencion_por_tipo_consulta'].astype(int)
df['id_clave_rango'] = df['id_clave_rango'].astype(int)
df['id_genero'] = df['id_genero'].astype(int)
df['id_tipo_consulta'] = df['id_tipo_consulta'].astype(int)
df['total'] = df['total'].astype(int)

# Creamos una lista para almacenar los inserts
inserts = []

# Iteramos por cada fila del DataFrame y creamos los inserts
for index, row in df.iterrows():
    id_row = row['id_atencion_por_tipo_consulta']
    id_rango_edad = row['id_clave_rango']
    id_genero = row['id_genero']
    id_tipo_consulta = row['id_tipo_consulta']
    total_atenciones = row['total']
    insert = f"INSERT INTO atencion_por_tipo_consulta (id_atencion_por_tipo_consulta, id_rango_edad, id_genero, id_tipo_consulta, total_atenciones) VALUES ({id_row}, {id_rango_edad}, {id_genero}, {id_tipo_consulta}, {total_atenciones});"
    inserts.append(insert)

# Escribimos los inserts en el archivo de salida
with open(path_salida, 'w') as file:
    file.write('\n'.join(inserts))

print(f"Inserts guardados en {path_salida}")
