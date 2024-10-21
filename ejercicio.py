# Escribir un programa que almacene en una lista los siguientes 
# precios: 50, 75, 46, 22, 80, 65, 8 y muestre por pantalla el menor y el mayor de los precios.

# Ejercicio hecho por Nicolás Ruiz

def mayor(lista):
    numero=0
    for i in lista:
        if i > numero:
            numero=i
    print(numero)

def menor(lista):
    numero=99999999999999999
    for i in lista:
        if i < numero:
            numero=i
    print(numero)

precios = [50, 75, 46, 22, 80, 65, 8]

mayor(precios)
menor(precios)
