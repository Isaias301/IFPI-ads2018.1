def main():
    new_matriz = nova_matriz(5,5)
    matriz = alimenta_matriz(new_matriz)
    for i in range(len(matriz)):
        print(matriz[i])

    maior_menor(matriz)


def maior_menor(matriz):
    soma = 0
    vetor_soma = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma += matriz[i][j]

        vetor_soma += [soma]
    print(vetor_soma)

    maior = 0
    menor = vetor_soma[0]
    linha_manior = 0
    linha_menor = 0
    for l in range(len(vetor_soma)):
        if vetor_soma[i] > maior:
            maior = vetor_soma[i]
            linha_manior = vetor_soma.index(vetor_soma[i])
        elif vetor_soma[i] < maior:
            menor = vetor_soma[i]
            linha_menor = vetor_soma.index(vetor_soma[i])
    print("Maior numero: {} linha: {}\nMenor numero: {} linha: {}".format(maior, linha_manior, menor, linha_menor))


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
