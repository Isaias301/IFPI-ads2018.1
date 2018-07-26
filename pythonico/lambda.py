def main():
    print(nova_matriz(3,3,"*"))


def nova_matriz(linhas, colunas, valor_padrao):
    matriz = [None] * linhas
    [print(matriz) for linha in matriz linha = [valor_padrao] * colunas]


if __name__ == '__main__':
    main()
