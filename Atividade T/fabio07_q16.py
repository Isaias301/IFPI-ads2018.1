def main():
    new_matriz = nova_matriz(5,5)
    matriz = alimenta_matriz(new_matriz)
    for i in range(len(matriz)):
        print(matriz[i])

    print(determinante(matriz))


def determinante(matriz):
    # soma dos elementos da diagonal primaria
    diag_primaria = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j:
                diag_primaria += matriz[i][j]
    return diag_primaria


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
