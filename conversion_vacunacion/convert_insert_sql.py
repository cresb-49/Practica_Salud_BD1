import pandas as pd

# Ruta donde se guardarán los archivos
ruta_entrada = "/home/benjamin/PROYECTOS/Practica_Salud_BD1/conversion_vacunacion/"
ruta_salida = "/home/benjamin/PROYECTOS/Practica_Salud_BD1/conversion_vacunacion/"

# Leer el archivo CSV
df = pd.read_csv(ruta_entrada + 'datos_vacunacion_v8.csv')

df_cleaned = df

# Nombre de la tabla a la que se insertarán los datos
tabla = 'atencion_por_vacuna'

if 'id_departamento' in df_cleaned.columns:
    df_cleaned['id_departamento'] = df_cleaned['id_departamento'].apply(
        lambda x: f"{int(x):02d}" if pd.notnull(x) else x)
if 'id_municipio' in df_cleaned.columns:
    df_cleaned['id_municipio'] = df_cleaned['id_municipio'].apply(
        lambda x: f"{int(float(x)):04d}" if pd.notnull(x) else x)

# Abrir un archivo para escribir los comandos SQL
with open(ruta_salida + 'inserts_vacunacion.sql', 'w') as file:
    for index, row in df_cleaned.iterrows():
        # Crear la sentencia INSERT para cada fila
        insert_statement = f"INSERT INTO {tabla} (anio, id_area_salud, id_departamento, id_municipio, edad, id_vacuna, id_numero_dosis, n_vacunados, poblacion) VALUES "
        insert_statement += f"({int(row['anio'])}, {int(row['id_area_salud'])}, \'{row['id_departamento']}\', \'{row['id_municipio']}\', {int(row['edad'])}, {int(row['id_vacuna'])}, {int(row['id_num_dosis'])}, {int(row['n_vacunados'])}, {int(row['poblacion'])});\n"
        # Escribir la sentencia en el archivo SQL
        file.write(insert_statement)

print("Archivo SQL generado exitosamente.")
