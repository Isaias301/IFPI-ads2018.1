def main():
	lista = input().split()
	lista = transforma_itens_int(lista)
	new_array = cumsum(lista)
	print(new_array)


# Transforma todos os elementos do array em inteiros
def transforma_itens_int(lista):
	tamanho_array = len(lista)
	for i in range(tamanho_array):
		lista[i] = int(lista[i])
	return lista


# Soma cada elemento do array com o anterior e criar um novo array com os somatorios
def cumsum(lista):
	soma = 0
	tamanho_array = len(lista)
	new_array = [0] * tamanho_array
	for i in range(tamanho_array):
		soma += lista[i]
		new_array[i] = soma
	return new_array


if __name__ == '__main__':
    main()
