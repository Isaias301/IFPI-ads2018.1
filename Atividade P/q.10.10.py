def main():
	lista = [1,2,3,4,5]
	print(in_bisect(lista, 7))


def in_bisect(lista, valor_alvo):

	try:
		if lista.index(valor_alvo) != None:
			return lista.index(valor_alvo)
	except:
		return None


if __name__ == '__main__':
    main()
