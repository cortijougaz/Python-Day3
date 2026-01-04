def separar_letras(letras: str) -> list[str]:
    limpio = "".join(letras.split()).lower()
    return list(limpio)

def ultima_letras(texto: str) -> str:
    if texto[-1] != ".":
        return texto[-1]
    else:
        return texto[-2]

def invertir_palabras(texto: str) -> str:
    nuevo_texto = texto.split()
    nuevo_texto.reverse()
    return " ".join(nuevo_texto)

texto = input("Ingrese un texto: ").lower()
letras = input("Ingrese 3 letras a su elección: ")
print("-------------------------------------")
let = separar_letras(letras)
primera_letra = texto.count(let[0])
segunda_letra = texto.count(let[1])
tercera_letra = texto.count(let[2])
print("En el texto: " + texto)
print(f"La primera letra {let[0]} se repite {primera_letra} veces")
print(f"La segunda letra {let[1]} se repite {segunda_letra} veces")
print(f"La tercera letra {let[2]} se repite {tercera_letra} veces")
palabras = texto.split()
print(f"El texto está conformado por {len(palabras)} palabras")
first = texto[0]
last = ultima_letras(texto)
print(f"La primera letra del texto es: {first}")
print(f"La última letra del texto es: {last}")
print(invertir_palabras(texto))
diccionario = {True: "La palabra Python sí se encuentra en el texto.",
               False: "La palabra Python no se encuentra en el texto."}
print(diccionario["python".lower() in texto.lower()])
