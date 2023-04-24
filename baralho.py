cartas = input()

copas = [1]
espadas = [1]
ouros = [1]
paus = [1]

for i in range(13):
    copas.append(0)
    espadas.append(0)
    ouros.append(0)
    paus.append(0)

for i in range(0, len(cartas),+3):
    valor = cartas[i] + cartas[i+1]
    valor = int(valor)
    if cartas[i+2] == "P":
        if paus[valor] == 1:
            paus[0] = 2
        else:
            paus[valor] = 1
    elif cartas[i+2] == "C":
        if copas[valor] == 1:
            copas[0] = 2
        else:
            copas[valor] = 1
    elif cartas[i+2] == "E":
        if espadas[valor] == 1:
            espadas[0] = 2
        else:
            espadas[valor] = 1
    elif cartas[i+2] == "U":
        if ouros[valor] == 1:
            ouros[0] = 2
        else:
            ouros[valor] = 1
if copas[0] == 2:
    print("erro")
else:
    print(copas.count(0))
if espadas[0] == 2:
    print("erro")
else:
    print(espadas.count(0))
if ouros[0] == 2:
    print("erro")
else:
    print(ouros.count(0))
if paus[0] == 2:
    print("erro")
else:
    print(paus.count(0))


