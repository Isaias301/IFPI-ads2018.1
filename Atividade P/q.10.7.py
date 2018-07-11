def main():
	lista = [1,2,3,4]
	print(has_duplicates(lista))


def has_duplicates(lista):
	elemento = 0
	cont = 0
	for i in lista:
		if i == elemento:
			cont += 1
		elemento = i		
	if cont > 0:
		return True
	else:
		return False


if __name__ == '__main__':
    main()