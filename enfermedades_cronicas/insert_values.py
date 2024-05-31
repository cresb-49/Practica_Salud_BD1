import pandas as pd

# Paths de entrada y salida
path_entrada = "E:\PROYECTOS\Practica_Salud_BD1\enfermedades_cronicas\genero_datos.csv"
path_salida = "E:\PROYECTOS\Practica_Salud_BD1\enfermedades_cronicas\genero_datos_54384.sql"

# Cargamos el archivo CSV
df = pd.read_csv(path_entrada)

# Aseguramos que las columnas sean del tipo correcto
df['id_linea'] = df['id_linea'].astype(int)
df['id_genero'] = df['id_genero'].astype(int)
df['id_rango_edad'] = df['id_rango_edad'].astype(int)

# Creamos una lista para almacenar los inserts
inserts = []

# Iteramos por cada fila del DataFrame y creamos los inserts
for index, row in df.iterrows():
    id_linea = row['id_linea']
    if int(id_linea) >= 54384:
        id_genero = row['id_genero']
        id_rango_edad = row['id_rango_edad']
        valor = row['valor']
        insert = f"INSERT INTO valor_enfermedades_cronicas (id_enfermedades_cronicas, id_genero, id_rango_edad, valor) VALUES ({id_linea}, {id_genero}, {id_rango_edad}, {valor});"
        inserts.append(insert)

# Escribimos los inserts en el archivo de salida
with open(path_salida, 'w') as file:
    file.write('\n'.join(inserts))

print(f"Inserts guardados en {path_salida}")
