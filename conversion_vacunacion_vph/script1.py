import pandas as pd
from unidecode import unidecode
import re

# Función para limpiar el texto
def limpiar_texto(texto):
    # Convertir a minúsculas
    texto = texto.lower()
    # Reemplazar caracteres especiales por sus equivalentes sin acentos
    texto = unidecode(texto)
    # Eliminar caracteres especiales y espacios adicionales
    texto = re.sub(r'[^a-z0-9\s]', '', texto)
    return texto

# Nombre del archivo CSV de entrada y salida
archivo_entrada = "/home/benjamin/PROYECTOS/Practica_Salud_BD1/conversion_vacunacion_vph/datos_vacunacion_vph.csv"
archivo_salida = "/home/benjamin/PROYECTOS/Practica_Salud_BD1/conversion_vacunacion_vph/datos_vacunacion_vph_v1.csv"

# Leer el archivo CSV
df = pd.read_csv(archivo_entrada)

# Aplicar la función de limpieza a las columnas 'Departamento' y 'Municipio'
df['departamento'] = df['departamento'].apply(limpiar_texto)
df['municipio'] = df['municipio'].apply(limpiar_texto)

# Eliminar la columna 'codigo_municipio'
df = df.drop(columns=['codigo_municipio'])

# Guardar el DataFrame modificado en un nuevo archivo CSV
df.to_csv(archivo_salida, index=False)
