def main():
	lista = [[1, 2], [3], [4, 5, 6]]
	print(nested_sum(lista))
	

def nested_sum(lista):
	soma = 0
	for i in range(len(lista)):
		for j in lista[i]:
			soma += j
	return soma


if __name__ == '__main__':
    main()