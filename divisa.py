
divisa = {"Euro":"€", "Dollar":"$", "Yen":"¥"}

entrada = input("Que divisa? ");
r = None
for div in divisa:
    if div == entrada:
        r = divisa[div]
        break

if r != None:
    print(r)
else:
    print("No se encontro la divisa")

   
