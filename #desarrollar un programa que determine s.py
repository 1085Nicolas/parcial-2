#desarrollar un programa que determine si en una lista se encuestra una cadena de caracteres con dos o mas vocales,
# si la cadena existe debe inprimirla y si  no existe debe imprimir "no existe"


lista = ["hola", "sol", "python",]

# se define una función que cuenta las vocales en una cadena
def vocales(cadena):
    return sum(1 for c in cadena if c in "aeiouAEIOU")

# Verificar si alguna cadena tiene dos o más vocales
print(next((cadena for cadena in lista if vocales(cadena) >= 2), "no existe"))
