def crear_diccionario():
    entrada = input("Introduce las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas: ")
    pares = entrada.split(',')
    diccionario = {}
    for par in pares:
        palabra, traduccion = par.split(':')
        diccionario[palabra.strip()] = traduccion.strip()
    return diccionario

def traducir_frase(diccionario):
    frase = input("Introduce una frase en español: ")
    palabras = frase.split()
    frase_traducida = []
    for palabra in palabras:
        if palabra in diccionario:
            frase_traducida.append(diccionario[palabra])
        else:
            frase_traducida.append(palabra)
    return ' '.join(frase_traducida)

diccionario = crear_diccionario()
frase_traducida = traducir_frase(diccionario)
print(frase_traducida)
