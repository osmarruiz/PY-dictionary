#- Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
#pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de
#ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje
#informando de ello.

frutas_precio = {"Platano":1.35, "Manzana":0.80, "Pera":0.85, "Naranja":0.70}\

fruta =input("Que fruta? ")
kilos =int(input("cuentos kilos? "))

try:
    if frutas_precio[fruta] != None:
        precio_final = frutas_precio[fruta] * kilos
        print(f"{fruta} a {precio_final} los {kilos} kilos")
except:
    print("No se encontro esta fruta")