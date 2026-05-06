# Declarar lista de 10 elementos enteros
lista = [5, 8, 12, 3, 7, 9, 15, 2, 6, 10]

# Recorrer e imprimir todos los elementos con un for
print("Elementos de la lista:")
for i in lista:
    print(i)

# Modificar el tercer elemento
nuevo_valor = int(input("Ingrese un nuevo valor para el tercer elemento: "))
lista[2] = nuevo_valor

print("\nLista actualizada:")
for i in lista:
    print(i)

# Buscar un número en la lista
buscar = int(input("\nIngrese un número a buscar: "))

if buscar in lista:
    print("El número sí existe en la lista.")
else:
    print("El número no existe en la lista.")
