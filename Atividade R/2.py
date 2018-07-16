def main():
    a = input().split()
    print(elementos_iguais(a))


def elementos_iguais(lista):
    # tamanho da lista
    tamanho_lista = len(lista)
    # contador
    cont = 0
    # map em cada elemento da lista
    for i in range(tamanho_lista):
        # compara cada elemento do map anterior com cada elemento do map atual
        for j in range(tamanho_lista):
            # verifica se os elementos são iguais
            if lista[i] == lista[j]:
                # acumulua no contador
                cont += 1
    # resultado logico
    return cont > tamanho_lista


if __name__ == '__main__':
    main()
