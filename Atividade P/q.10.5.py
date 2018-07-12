def main():
	lista = input().split()
	lista_int = transforma_numeros_int(lista)
	print(is_sorted(lista_int))


def transforma_numeros_int(lista):
	for i in range(len(lista)):
		lista[i] = int(lista[i])
	return lista


def is_sorted(lista):
	for i in range(len(lista)):
		try:
			if lista[i] > lista[i+1]:
				return False
		except:
			return True


# Forma pythonica
# def is_sorted(lista):
# 	b = lista.copy()
# 	lista.sort()
# 	return lista == b


if __name__ == '__main__':
    main()
