def main():
    new_matriz = nova_matriz(5,5)
    matriz = alimenta_matriz(new_matriz)
    for i in range(len(matriz)):
        print(matriz[i])

    soma_positivos_negativos(matriz)


def soma_positivos_negativos(matriz):
    soma_positivos = 0
    soma_negativos = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > 0:
                soma_positivos += matriz[i][j]
            else:
                soma_negativos += matriz[i][j]
    print("Soma dos números positivos: {}\nSoma dos números negativos: {}".format(soma_positivos, soma_negativos))


def alimenta_matriz(matriz):
    from random import randint
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = randint(-50, 80)
    return matriz


def nova_matriz(colunas, linhas, valor_padrao=None):
    matriz = [None] * colunas
    for i in range(len(matriz)):
        matriz[i] = [valor_padrao] * linhas
    return matriz


if __name__ == '__main__':
    main()
