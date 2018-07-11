def main():
	lista = [1,2,3,4]
	print(is_sorted(lista))
	

def is_sorted(lista):
	b = lista.copy()
	lista.sort()
	return lista == b


if __name__ == '__main__':
    main()