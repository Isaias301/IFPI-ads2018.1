def main():
    new_matriz = nova_matriz(5,5)
    matriz = alimenta_matriz(new_matriz)
    print(matriz)
    menor_elemento_da_matriz(matriz)
    maior_elemento_da_matriz(matriz)


def alimenta_matriz_numero(matriz):
    from random import randint
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = randint(1, 100)
    return matriz


def maior_elemento_da_matriz(matriz):
    menor = matriz[0][0]
    posicao = ""
    for l in range(len(matriz)):
        for m in range(len(matriz[l])):
            if matriz[l][m] > menor:
                menor = matriz[l][m]
                posicao = str(l)+"-"+str(m)
    a = posicao.split("-")
    print("Menor elemento: {}[{}][{}]".format(menor, a[0],a[1]))


def menor_elemento_da_matriz(matriz):
    menor = matriz[0][0]
    posicao = ""
    for l in range(len(matriz)):
        for m in range(len(matriz[l])):
            if matriz[l][m] < menor:
                menor = matriz[l][m]
                posicao = str(l)+"-"+str(m)
    a = posicao.split("-")
    print("Menor elemento: {}[{}][{}]".format(menor, a[0],a[1]))


def nova_matriz(colunas, linhas, valor_padrao=None):
    matriz = [None] * colunas
    for i in range(len(matriz)):
        matriz[i] = [valor_padrao] * linhas
    return matriz


if __name__ == '__main__':
    main()
