def main():
    new_matriz = nova_matriz(5,5)
    matriz = alimenta_matriz(new_matriz)
    print(matriz)
    if matriz_simetrica(matriz):
        print("Simetrica")
    else:
        print("Nãe e simetrica")


def matriz_simetrica(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == matriz[j][i]:
                return True
            else:
                return False


def alimenta_matriz(matriz):
    from random import randint
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = randint(1, 100)
    return matriz


def nova_matriz(colunas, linhas, valor_padrao=None):
    matriz = [None] * colunas
    for i in range(len(matriz)):
        matriz[i] = [valor_padrao] * linhas
    return matriz


if __name__ == '__main__':
    main()
