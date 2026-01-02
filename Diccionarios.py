diccionario = {
    "c1": "valor1",
    "c2": "valor2"
}
print(diccionario)
resultado = diccionario["c1"]
print(resultado)

cliente = {
    "nombre": "Juan",
    "apellido": "Fuentes",
    "peso": 88,
    "talla": 1.76
}
consulta = cliente["apellido"]
print(consulta)

dic = {
    "c1": 55,
    "c2": [10, 20, 30],
    "c3": {
        "s1": 100,
        "s2": "e",
    },
}
print(dic["c2"][1])
print(dic["c3"]["s2"].upper())
dic[3] = "c"
print(dic)
dic[3] = "C"
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())