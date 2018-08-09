def main():
    matriz = [[1,2,3], [7,5,4], [9,0,1]]
    matriz_ordem = ordenar(matriz)
    mostrar_matriz(matriz_ordem)


def importar(arquivo='enem2014_nota_por_escola.csv'):

    fin = open(arquivo, encoding="ISO-8859-1")

    escolas = []
    for linha in fin.readlines():
        linha_limpa = linha.strip()
        dados_escola = linha_limpa.split(';')
        escolas.append(dados_escola[1:])

    return escolas


def tratar_dados(escolas):

    for i in range(len(escolas)):
        for j in range(len(escolas[i])):
            # se eh para transformar para float
            if j >= 6 and j <= 11:
                escolas[i][j] = float(escolas[i][j].replace(',', '.'))


def orde(matriz):
    return matriz[2]


def ordenar(matriz):
    matriz_ordem = sorted(matriz, key=orde, reverse=False)
    return matriz_ordem


def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])


if __name__ == '__main__':
    main()
