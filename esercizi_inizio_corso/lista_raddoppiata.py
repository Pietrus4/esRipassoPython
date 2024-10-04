lista1 = [1, 2, 3, 4, 5]
lista2 = []

for i in range(len(lista1)):
    lista2.append(lista1[i] * 2)
    
print(f"{lista1} raddoppiata è: {lista2}")