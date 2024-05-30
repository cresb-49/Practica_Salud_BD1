import pandas as pd
import os

# Paths de entrada y salida
path_entrada = "E:/PROYECTOS/Practica_Salud_BD1/atencion_tipo_consulta"
path_salida = "E:/PROYECTOS/Practica_Salud_BD1/atencion_tipo_consulta"

# Cargamos el archivo CSV
df = pd.read_csv(os.path.join(path_entrada, "atencion_por_tipo_consulta.csv"))

# Creamos el diccionario para almacenar las combinaciones únicas y sus IDs
rango_dict = {}
rango_dict['0.0-4.0'] = 1
rango_dict['5.0-9.0'] = 2
rango_dict['10.0-14.0'] = 3
rango_dict['15.0-19.0'] = 4
rango_dict['20.0-24.0'] = 5
rango_dict['25.0-29.0'] = 6
rango_dict['30.0-34.0'] = 7
rango_dict['35.0-39.0'] = 8
rango_dict['40.0-44.0'] = 9
rango_dict['45.0-49.0'] = 10
rango_dict['50.0-54.0'] = 11
rango_dict['55.0-59.0'] = 12
rango_dict['60.0-64.0'] = 13
rango_dict['65.0-69.0'] = 14
rango_dict['70.0-74.0'] = 15
rango_dict['75.0-79.0'] = 16
rango_dict['80.0-120.0'] = 17
rango_dict['nan-nan'] = 18
current_id = 19

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
nuevo_df = df[['id_atencion_por_tipo_consulta', 'id_clave_rango', 'id_sexo', 'id_tipo_consulta', 'total']]

# Guardamos el nuevo CSV
nuevo_df.to_csv(os.path.join(
    path_salida, "atencion_por_tipo_consulta_v1.csv"), index=False)

# Convertimos el diccionario a un DataFrame
rango_df = pd.DataFrame(list(rango_dict.items()),
                        columns=['clave_rango', 'id'])

# Dividimos la columna 'clave_rango' en 'lim_inf_rango' y 'lim_sup_rango'
rango_df[['lim_inf_rango', 'lim_sup_rango']
         ] = rango_df['clave_rango'].str.split('-', expand=True)

# Seleccionamos y reordenamos las columnas
rango_df = rango_df[['id', 'lim_inf_rango', 'lim_sup_rango']]

# Guardamos el diccionario en un nuevo CSV
rango_df.to_csv(os.path.join(path_salida, "rango_claves.csv"), index=False)
