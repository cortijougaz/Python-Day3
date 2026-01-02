mi_lista = ["a", "b", "c"]
print(type(mi_lista))
print(mi_lista)
print(len(mi_lista))
print(mi_lista[0])
mi_lista2 = ["d", "e", "f"]
mi_lista3 = mi_lista + mi_lista2
mi_lista3[0] = "alfa"
mi_lista3.append("beta")
print(mi_lista3)
print(len(mi_lista3))
mi_lista3.pop()
print(mi_lista3)
eliminado = mi_lista3.pop(1)
print(mi_lista3)
print(eliminado)

lista = ['g', 'o', 'b', 'm', 'c']
print(lista)
lista.sort()
print(lista)