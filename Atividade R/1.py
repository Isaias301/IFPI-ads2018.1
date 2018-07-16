def main():
    a = input().split()
    print(inverte_vetor(a))


# inverte o vetor
def inverte_vetor(lista):
    # tamanho do vetor vindo no parametro
    tamanho_vetor = len(lista)
    # cria um novo vetor para armazenar os elementos ao inverso.
    c = ""
    # percore o vetor ao contrario
    while tamanho_vetor > 0:
        # soma string
        c += str(lista[tamanho_vetor-1])
        tamanho_vetor -= 1
        # cria uma lista com cada parte da string
    return list(c)


if __name__ == '__main__':
    main()
