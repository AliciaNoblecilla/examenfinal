""" 3. Escribir un programa para gestionar los errores en Python (3 ptos):
Reglas:
- El programa deberá tener una función para ingresar dos datos los
cuáles serán ingresado por consola.
- Deberá tener una función en el caso haya una división entre cero y
mencionar el error.
- Deberá tener una función la cuál evaluará la suma de datos
incorrectos.
- Todas las funciones creadas tendrán la facultad de volver a pedir el
número hasta que se ingrese correctamente."""

def division(a, b):
    try:
        resultado = a/b
        print(resultado)
    except ZeroDivisionError:
        print("no es posible realizar esta division")
    else:
        print(resultado)

division(48, 0)

def operacion(x, y):
    try:
        resultado = x + y

    except TypeError:
        print("no es posible realizar esta suma")
    else:
        print(resultado)

operacion(4, "hola")



