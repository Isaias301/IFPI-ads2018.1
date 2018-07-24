def main():
    matriz = [[1,2,3], [4,5,6], [7,8,9]]
    matriz_quadrada(matriz)
    soma_diagonal_principal(matriz)


def matriz_quadrada(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=' ')
        print("\n")


def soma_diagonal_principal(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j:
                print(matriz[i][j], end=' ')
            else:
                print(" ", end=" ")
        print("\n")


def soma_diagonal_secundaria(matriz):
    pass


def soma_elementos_resto(matriz):
    pass


if __name__ == '__main__':
    main()
