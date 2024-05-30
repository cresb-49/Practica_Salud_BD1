import pandas as pd
import os

# Paths de entrada y salida
path_entrada = "E:/PROYECTOS/Practica_Salud_BD1/atencion_rango_edad"
path_salida = "E:/PROYECTOS/Practica_Salud_BD1/atencion_rango_edad"

# Cargamos el archivo CSV
df = pd.read_csv(os.path.join(path_entrada, "atencion_por_rango_edad.csv"))

# Creamos el diccionario para almacenar las combinaciones únicas y sus IDs
rango_dict = {}
current_id = 1

# Función para generar clave única y asignar ID
def generar_clave(row):
    global current_id
    clave = f"{row['lim_inf_rango']}-{row['lim_sup_rango']}"
    if clave not in rango_dict:
        rango_dict[clave] = current_id
        current_id += 1
    return rango_dict[clave]

# Aplicamos la función para cada fila y generamos una columna con el ID
df['id_clave_rango'] = df.apply(generar_clave, axis=1)

# Seleccionamos solo las columnas necesarias para el nuevo CSV
nuevo_df = df[['id_clave_rango', 'id_codigo_cie', 'hombres', 'mujeres', 'ignorado', 'id_tipo_servicio']]

# Guardamos el nuevo CSV
nuevo_df.to_csv(os.path.join(path_salida, "nuevo_atencion_por_rango_edad.csv"), index=False)

# Convertimos el diccionario a un DataFrame
rango_df = pd.DataFrame(list(rango_dict.items()), columns=['clave_rango', 'id'])

# Dividimos la columna 'clave_rango' en 'lim_inf_rango' y 'lim_sup_rango'
rango_df[['lim_inf_rango', 'lim_sup_rango']] = rango_df['clave_rango'].str.split('-', expand=True)

# Seleccionamos y reordenamos las columnas
rango_df = rango_df[['id', 'lim_inf_rango', 'lim_sup_rango']]

# Guardamos el diccionario en un nuevo CSV
rango_df.to_csv(os.path.join(path_salida, "rango_claves.csv"), index=False)
