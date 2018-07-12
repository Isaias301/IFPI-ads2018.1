def main():
	lista = input().split()
	lista_int = transforma_numeros_int(lista)
	print(has_duplicates(lista_int))


def transforma_numeros_int(lista):
	for i in range(len(lista)):
		lista[i] = int(lista[i])
	return lista


def has_duplicates(lista):
	elemento = 0
	cont = 0
	for i in range(len(lista)):
		if lista[i] == elemento:
			cont += 1
		elemento = lista[i]
	if cont > 0:
		return True
	else:
		return False


if __name__ == '__main__':
    main()
