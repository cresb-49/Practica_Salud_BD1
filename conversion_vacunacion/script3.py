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
ruta_entrada = "/home/benjamin/PROYECTOS/Practica_Salud_BD1/conversion_vacunacion/"
ruta_salida = "/home/benjamin/PROYECTOS/Practica_Salud_BD1/conversion_vacunacion/"

def cargar_en_diccionario(nombre_archivo, limpiar=False):
    df_temp = pd.read_csv(ruta_entrada + nombre_archivo)
    if limpiar:
        df_temp.iloc[:, 1] = df_temp.iloc[:, 1].apply(lambda x: limpiar_texto(str(x)))
    return dict(zip(df_temp.iloc[:, 1], df_temp.id))

# Cargar los CSV en diccionarios con limpieza para 'departamento' y 'municipio'
dic_departamento = cargar_en_diccionario('departamento.csv', limpiar=True)
dic_municipio = cargar_en_diccionario('municipio.csv', limpiar=True)
dic_area_salud = cargar_en_diccionario('area_salud.csv')
dic_numero_dosis = cargar_en_diccionario('numero_dosis.csv')
dic_vacuna = cargar_en_diccionario('vacuna.csv')

# Leer el archivo original de vacunación
df = pd.read_csv(ruta_entrada + 'datos_vacunacion_v1.csv')
# Aplicar limpieza de texto a las columnas antes de hacer el mapeo
df['departamento'] = df['departamento'].apply(lambda x: limpiar_texto(str(x))).map(dic_departamento)
df['municipio'] = df['municipio'].apply(lambda x: limpiar_texto(str(x))).map(dic_municipio)
df['area_salud'] = df['area_salud'].map(dic_area_salud)
df['vacuna'] = df['vacuna'].map(dic_vacuna)
df['num_dosis'] = df['num_dosis'].map(dic_numero_dosis)


# Guardar el DataFrame modificado en un nuevo archivo CSV
df.to_csv(ruta_salida + 'datos_vacunacion_v2.csv', index=False)
