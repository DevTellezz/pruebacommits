import re

def limpiar_archivo(ruta_archivo):
    # Definir las palabras o números a omitir
    omitir_palabras = ['2024', 'Base64', 'Output', 'tescha', 'pruebas', '17645']
    
    # Abrir el archivo y leer el contenido
    with open(ruta_archivo, 'r') as archivo:
        contenido = archivo.read()

    # Buscar y extraer todos los textos que estén en formato Base64
    b64_texto = re.findall(r'[A-Za-z0-9+/=]{4,}', contenido)
    
    # Filtrar los elementos que no sean números o palabras no deseadas
    b64_filtrado = [texto for texto in b64_texto if not any(palabra in texto for palabra in omitir_palabras)]
    
    # Unir los textos en b64 en una sola cadena
    texto_b64 = '\n'.join(b64_filtrado)
    
    # Sobrescribir el archivo con el texto limpio
    with open(ruta_archivo, 'w') as archivo:
        archivo.write(texto_b64)


# Ejemplo de uso
ruta = '/home/tellez/Documentos/pruebaCommits/textoBasura.txt'
resultado = limpiar_archivo(ruta)
print(resultado)
    