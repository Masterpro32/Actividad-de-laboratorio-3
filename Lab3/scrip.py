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
#Parte_Jeanpier
matriz = []

for i in range(3):
    fila = []
    for j in range(3):
        num = int(input(f"Ingrese número para la posición [{i}][{j}]: "))
        fila.append(num)
    matriz.append(fila)

print("\nMatriz ingresada:")
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()

suma = 0
for fila in matriz:
    for elemento in fila:
        suma += elemento

print("\nLa suma total es:", suma)
