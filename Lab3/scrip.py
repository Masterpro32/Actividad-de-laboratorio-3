# PARTE HAROL
lista = [5, 8, 12, 3, 7, 9, 15, 2, 6, 10]
print("Elementos de la lista:")
for i in lista:
    print(i)
nuevo_valor = int(input("Ingrese un nuevo valor para el tercer elemento: "))
lista[2] = nuevo_valor
print("\nLista actualizada:")
for i in lista:
    print(i)
buscar = int(input("\nIngrese un número a buscar: "))
if buscar in lista:
    print("El número sí existe en la lista.")
else:
    print("El número no existe en la lista.")
