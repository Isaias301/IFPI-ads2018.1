def main():
	lista = input().split()
	lista_int = transforma_itens_int(lista)
	resultado = middle(lista_int)
	print(resultado)

# transforma todos os iten do vetor em inteiros. Ou seja isso e um mapeamento.
def transforma_itens_int(lista):
	for i in range(len(lista)):
		lista[i] = int(lista[i])
	return lista


def middle(lista):
	new_lista = []
	# verifica se o tamanho da lista e menor igual a dois. Caso a atenda a condição return False(vetor invalido).
	if len(lista) <= 2:
		return False
	# verifica se o tamanho do vetor e igual a tres. Caso atenda a condição ele tem um tratamento diferente.
	elif len(lista) == 3:
		del(lista[0])
		del(lista[len(lista)-1])
		return lista
	# caso contrario o processamento e normal
	else:
		for i in range(len(lista)):
			if len(lista) > 2:
				del(lista[0])
				if len(lista) > 2:
					del(lista[len(lista)-1])
				else:
					break
		return lista


if __name__ == '__main__':
    main()
