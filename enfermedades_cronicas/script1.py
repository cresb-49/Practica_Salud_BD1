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
archivo_entrada = "E:\PROYECTOS\Practica_Salud_BD1\enfermedades_cronicas\data.csv"
archivo_salida = "E:\PROYECTOS\Practica_Salud_BD1\enfermedades_cronicas\data1.csv"

# Leer el archivo CSV
df = pd.read_csv(archivo_entrada)

# Aplicar la función de limpieza a las columnas 'Departamento' y 'Municipio'
df['id_departamento'] = df['id_departamento'].apply(limpiar_texto)
df['id_municipio'] = df['id_municipio'].apply(limpiar_texto)


# Guardar el DataFrame modificado en un nuevo archivo CSV
df.to_csv(archivo_salida, index=False)
