#desarrollar un algoritmo que calcule el promedio de un areglo de reales


#se define la funcion promedio
def promedio():
#se crea una lista vacía y un ciclo while que genera un float input que le solicita al usuario que ingrese un valor 
    valores = [] 
    while True:
        valor = float(input("valor: "))
#si el usuario ingresa un valor 0 el ciclo se detiene
        if valor ==  0:
            break 
 #si el usuario ingresa un valor diferente de 0 el valor es agregado a la lista
        else:
            valores.append(valor)        
#se declara la variable "prom" con el valor de 0 y mediante un ciclo for se le suman los valores ingresados por el usuario y almacenados en la lista
    prom = 0
    for i in valores:
        prom+=i
#se declara la varianle "promfin" que se le asignará el valor de la suma de los datos dividido entre la camtidad de los mismos 
    promfin = prom / len(valores)     
    print("el promedio es de :",promfin)   
#se imprimen los valores ingresados por el usuario y el valor de la funcion "promedio"
    print(valores) 

promedio()