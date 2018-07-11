def main():
	file = open('words.txt')
	print(outra_forma(file))
	    

def use_append(file):
	lista = []
	for line in file:
	    word = line.strip()
	    lista.append(word)
	return lista


def outra_forma(file): # Terminar outra forma
	t = ''
	for line in file:
	    word = line.strip()
	    t = t + word
	return t



if __name__ == '__main__':
    main()