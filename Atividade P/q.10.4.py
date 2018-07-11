def main():
	lista = [1,2,3,4]
	print(chop(lista))
	

def chop(lista):
	lista.pop(0)
	lista.pop(len(lista)-1)
	return lista


if __name__ == '__main__':
    main()