# cartas = {"verde": 40, "rosa": 10, "azul": 0, "branco": 20, "amarelo": 30}

cartas = [20, 40, 0, 10, 30]

print(f"estado inicial: {cartas}")
for i in range(len(cartas)):
    print(f"iteração: {i}")
    for j in range(len(cartas)-1):
        print(f"comparando {cartas[j]} com {cartas[j+1]}")
        if cartas[j] > cartas[j+1]:
            print(f"\ttrocando {cartas[j]} com {cartas[j+1]}")
            aux = cartas[j]
            cartas[j] = cartas[j+1]
            cartas[j+1] = aux
            print(cartas)

    print(cartas)
