def main():
	file = open('words.txt')
	print(use_append(file))


def use_append(file):
	lista = []
	for i in file:
	    word = i.strip()
	    lista.append(word)
	return lista


def outra_forma(file):
	t = ''
	for line in file:
	    word = line.strip()
	    t = t + word
	return t



if __name__ == '__main__':
    main()
