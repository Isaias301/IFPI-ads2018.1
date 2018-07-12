def main():
	lista = input().split()
	lista_int = transforma_itens_int(lista)
	resultado = chop(lista_int)
	print(resultado)


# transforma todos os iten do vetor em inteiros. Ou seja isso e um mapeamento.
def transforma_itens_int(lista):
	for i in range(len(lista)):
		lista[i] = int(lista[i])
	return lista


def chop(lista):
	del(lista[0])
	del(lista[len(lista)-1])
	return lista


if __name__ == '__main__':
    main()
