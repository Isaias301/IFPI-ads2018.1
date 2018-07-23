def main():
    matriz = [[1,2,3], [4,5,6], [7,8,9]]
    matriz_quadrada(matriz)
    print("-"*30, end='\n\n')
    transposta(matriz)


def matriz_quadrada(matriz):

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=' ')
        print("\n")


def transposta(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[j][i], end=' ')
        print("\n")


if __name__ == '__main__':
    main()
