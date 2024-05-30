import pandas as pd

# Paths de entrada y salida
path_entrada = "E:/PROYECTOS/Practica_Salud_BD1/atencion_rango_edad/rango_claves.csv"
path_salida = "E:/PROYECTOS/Practica_Salud_BD1/atencion_rango_edad/inserts_rangos_edad.sql"

# Cargamos el archivo CSV
df = pd.read_csv(path_entrada)

# Creamos una lista para almacenar los inserts
inserts = []

# Iteramos por cada fila del DataFrame y creamos los inserts
for index, row in df.iterrows():
    id_rango_edad = row['id']
    lim_inf_rango = row['lim_inf_rango']
    lim_sup_rango = row['lim_sup_rango']
    insert = f"INSERT INTO rangos_edad (id_rango_edad, lim_inf_rango, lim_sup_rango) VALUES ({id_rango_edad}, {lim_inf_rango}, {lim_sup_rango});"
    inserts.append(insert)

# Escribimos los inserts en el archivo de salida
with open(path_salida, 'w') as file:
    file.write('\n'.join(inserts))

print(f"Inserts guardados en {path_salida}")
