mi_set = set([1,2,3,4,5])
print(mi_set)
print(type(mi_set))

otro_set = {1,2,3,4,5}
print(otro_set)
print(type(otro_set))
sett = mi_set.union(otro_set)
print(1 in sett)
sett.add(6)
sett.remove(1) # Elimina elemento que existe
sett.discard(143) # Elimina elemento que puede no existir
sett.pop() # Eliminación aleatoria
sett.clear() # Vacía el Set
print(sett)
