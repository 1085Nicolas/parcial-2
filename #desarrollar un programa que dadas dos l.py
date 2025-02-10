#desarrollar un programa simple que dadas dos listas determine que elementos tiene la primera lista que no tenga la segunda lista 

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7]

# Imprimir los elementos de la primera lista que no están en la segunda
print([elemento for elemento in lista1 if elemento not in lista2])
