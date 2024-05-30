import pandas as pd
import re

# Path del archivo SQL de entrada y el archivo CSV de salida
path_sql = "E:/PROYECTOS/Practica_Salud_BD1/atencion_tipo_consulta/modelo.sql"
output_path = "E:/PROYECTOS/Practica_Salud_BD1/atencion_tipo_consulta/atencion_por_tipo_consulta.csv"

# Leer el archivo SQL
with open(path_sql, 'r') as file:
    sql_content = file.read()

# Expresión regular para extraer los valores
regex = re.compile(r'VALUES \((\d+), (\d+), (\d+), (\d+), (\d+), (\d+)\);')

# Lista para almacenar los datos
data = []

# Buscar todas las coincidencias de la expresión regular en el contenido del archivo SQL
matches = regex.findall(sql_content)
for match in matches:
    data.append(match)

# Crear un DataFrame de pandas con los valores extraídos
df = pd.DataFrame(data, columns=[
    'id_atencion_por_tipo_consulta', 'lim_inf_rango', 'lim_sup_rango', 'id_sexo', 'id_tipo_consulta', 'total'
])

# Asegurar que las columnas sean de tipo entero
df = df.astype(int)

# Guardar el DataFrame como un archivo CSV
df.to_csv(output_path, index=False)

print(f"CSV guardado en {output_path}")
