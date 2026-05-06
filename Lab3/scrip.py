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

#PARTE DIEGO 

lista = []

while True:

    print("\n--- MENÚ ---")
    print("1. Insertar elemento al final")
    print("2. Eliminar elemento por posición")
    print("3. Buscar valor y mostrar posición")
    print("4. Mostrar lista")
    print("5. Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        num = int(input("Ingrese un número: "))
        lista.append(num)

    elif opcion == 2:
        pos = int(input("Ingrese la posición a eliminar: "))
        if pos >= 0 and pos < len(lista):
            lista.pop(pos)
        else:
            print("Posición inválida")

    elif opcion == 3:
        valor = int(input("Ingrese el valor a buscar: "))
        if valor in lista:
            print("Se encuentra en la posición:", lista.index(valor))
        else:
            print("No se encontró en la lista")

    elif opcion == 4:
        print("Lista actual:", lista)

    elif opcion == 5:
        break

    else:
        print("Opción inválida")
        
        # Parte Haziel
lista = [5, 2, 9, 1, 7, 3]

print("Lista original:", lista)

# ----------- MÉTODO BURBUJA -----------
burbuja = lista.copy()

for i in range(len(burbuja) - 1):
    for j in range(len(burbuja) - i - 1):
        if burbuja[j] > burbuja[j + 1]:
            # Intercambio
            temp = burbuja[j]
            burbuja[j] = burbuja[j + 1]
            burbuja[j + 1] = temp

print("Ordenado con Burbuja:", burbuja)
