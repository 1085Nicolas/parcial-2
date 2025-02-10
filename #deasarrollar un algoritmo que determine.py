#deasarrollar un algoritmo que determine la mediana de un arreglo de enteros, la mediana es el numero que queda en la mitad del arreglo despues de ser ordenado en python y sin definir funciones


# Arreglo de enteros
arreglo = [12, 3, 5, 7, 19, 1, 4]

# Ordenamos el arreglo
arreglo.sort()

print(arreglo)

# Determinamos el tamaño del arreglo
n = len(arreglo)

# Si el número de elementos es impar, la mediana es el valor en la posición central
if n % 2 == 1:
    mediana = arreglo[n // 2]
else:
    # Si el número de elementos es par, la mediana es el promedio de los dos valores centrales
    mediana = (arreglo[n // 2 - 1] + arreglo[n // 2]) / 2

# Imprimimos la mediana
print("La mediana es:", mediana)
