import pandas as pd

# Paths de entrada y salida
path_entrada = "E:/PROYECTOS/Practica_Salud_BD1/atencion_rango_edad/atencion_por_rango_edad_v2.csv"
path_salida = "E:/PROYECTOS/Practica_Salud_BD1/atencion_rango_edad/inserts_atencion_por_rango_edad.sql"

# Cargamos el archivo CSV
df = pd.read_csv(path_entrada)

# Aseguramos que las columnas sean del tipo correcto
df['id'] = df['id'].astype(int)
df['id_clave_rango'] = df['id_clave_rango'].astype(int)
df['id_tipo_servicio'] = df['id_tipo_servicio'].astype(int)

# Creamos una lista para almacenar los inserts
inserts = []

# Iteramos por cada fila del DataFrame y creamos los inserts
for index, row in df.iterrows():
    id_row = row['id']
    id_rango_edad = row['id_clave_rango']
    id_codigo_cie = row['id_codigo_cie']
    id_tipo_servicio = row['id_tipo_servicio']
    insert = f"INSERT INTO atencion_por_rango_edad (id, id_rango_edad, id_codigo_cie, id_tipo_servicio) VALUES ({id_row}, {id_rango_edad}, '{id_codigo_cie}', {id_tipo_servicio});"
    inserts.append(insert)

# Escribimos los inserts en el archivo de salida
with open(path_salida, 'w') as file:
    file.write('\n'.join(inserts))

print(f"Inserts guardados en {path_salida}")
