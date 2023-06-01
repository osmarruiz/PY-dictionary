def obtener_conjunto():
    entrada = input("Introduce los elementos del conjunto separados por comas: ")
    elementos = entrada.split(',')
    conjunto = set(elementos)
    return conjunto

# Obtener los conjuntos
print("Introduce los elementos del primer conjunto:")
conjunto1 = obtener_conjunto()

print("Introduce los elementos del segundo conjunto:")
conjunto2 = obtener_conjunto()

# Operaciones con los conjuntos
union = conjunto1.union(conjunto2)
interseccion = conjunto1.intersection(conjunto2)
diferencia1 = conjunto1.difference(conjunto2)
diferencia2 = conjunto2.difference(conjunto1)
diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)

# Mostrar los resultados
print("Unión:", union)
print("Intersección:", interseccion)
print("Diferencia del primero con respecto al segundo:", diferencia1)
print("Diferencia del segundo con respecto al primero:", diferencia2)
print("Diferencia simétrica:", diferencia_simetrica)
