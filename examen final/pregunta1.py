import random
def listaAleatoria():
    lista = []
    for _ in range(10):
        lista.append(random.randint(1, 25))
    return lista
def SinRepetir(lista):
    listaSinRepetir = list(set(lista))
    return listaSinRepetir
def ordenar(lista):
    listaMm = sorted(lista, reverse=True)
    listamM = sorted(lista)
    return listaMm, listamM
def maximo(lista):
    maximo = max(lista)
    return maximo
listaAleatoria = listaAleatoria()
print("Aleatoria:", listaAleatoria)

listaSinRepetir = SinRepetir(listaAleatoria)
print("sin repetir", listaSinRepetir)

# Ordenar listas
listaMm, listamM = ordenar(listaSinRepetir)
print("De mayor a menor:", listaMm)
print("De menor a mayor:", listamM)

# Encontrar el mayor número
maximo = maximo(listaSinRepetir)
print("El mayor número es:", maximo)