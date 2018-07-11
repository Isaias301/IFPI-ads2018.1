def main():
	lista = [1,2,3]
	print(cumsum(lista))
	

def cumsum(lista):
	cont = 0
	new_lista = []
	for i in range(len(lista)):
		cont += lista[i]
		new_lista.append(cont)
	return new_lista


if __name__ == '__main__':
    main()