import pandas as pd

# Paths de entrada y salida
path_entrada = "E:/PROYECTOS/Practica_Salud_BD1/atencion_departamento/genero_datos.csv"
path_salida = "E:/PROYECTOS/Practica_Salud_BD1/atencion_departamento/valor_atencion_por_departamento.sql"

# Cargamos el archivo CSV
df = pd.read_csv(path_entrada)

# Creamos una lista para almacenar los inserts
inserts = []

# Iteramos por cada fila del DataFrame y creamos los inserts
for index, row in df.iterrows():
    id_atencion_por_departamento = row['id']
    id_genero = row['id_genero']
    valor = row['valor']
    insert = f"INSERT INTO valor_atencion_por_departamento (id_atencion_por_departamento, id_genero, valor) VALUES ({id_atencion_por_departamento}, {id_genero}, {valor});"
    inserts.append(insert)

# Escribimos los inserts en el archivo de salida
with open(path_salida, 'w') as file:
    file.write('\n'.join(inserts))

print(f"Inserts guardados en {path_salida}")
