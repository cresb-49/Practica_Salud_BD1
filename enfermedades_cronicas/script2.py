import pandas as pd
from unidecode import unidecode
import re

# Función para limpiar el texto
def limpiar_texto(texto):
    if pd.isnull(texto):
        return texto
    texto = str(texto).lower()
    texto = unidecode(texto)
    texto = re.sub(r'[^a-z0-9\s]', '', texto)
    return texto

# Ruta donde se guardarán los archivos
ruta_entrada = "E:\PROYECTOS\Practica_Salud_BD1\enfermedades_cronicas\\"
ruta_salida = "E:\PROYECTOS\Practica_Salud_BD1\enfermedades_cronicas\\"

def cargar_en_diccionario(nombre_archivo, limpiar=False):
    df_temp = pd.read_csv(ruta_entrada + nombre_archivo)
    if limpiar:
        df_temp.iloc[:, 1] = df_temp.iloc[:, 1].apply(lambda x: limpiar_texto(str(x)))
    return dict(zip(df_temp.iloc[:, 1], df_temp.id))

# Cargar los CSV en diccionarios con limpieza para 'departamento' y 'municipio'
dic_departamento = cargar_en_diccionario('departamento.csv', limpiar=True)
dic_municipio = cargar_en_diccionario('municipio.csv', limpiar=True)

df = pd.read_csv(ruta_entrada + 'data1.csv')
# Aplicar limpieza de texto a las columnas antes de hacer el mapeo
df['id_departamento'] = df['id_departamento'].apply(lambda x: limpiar_texto(str(x))).map(dic_departamento)
df['id_municipio'] = df['id_municipio'].apply(lambda x: limpiar_texto(str(x))).map(dic_municipio)


# Guardar el DataFrame modificado en un nuevo archivo CSV
df.to_csv(ruta_salida + 'data2.csv', index=False)
