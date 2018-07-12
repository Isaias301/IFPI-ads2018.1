def main():
	tamanho = input("Tamanho do vetor: ")
	lista = criar_vetor(int(tamanho))
	lista_int = tranformar_item_int(lista)
	soma_itens = somar_itens(lista_int)
	print(soma_itens)


# Criar um novo vetor
def criar_vetor(tamanho):
	lista = [0] * tamanho
	for i in range(len(lista)):
		lista[i] = input().split()
	return lista


# Transforma todos os elementos do array em inteiros
def tranformar_item_int(lista):
	for i in range(len(lista)):
		for j in range(len(lista[i])):
			lista[i][j] = int(lista[i][j])
	return lista

def somar_itens(lista):
	soma = 0
	for i in range(len(lista)):
		for j in range(len(lista[i])):
			soma += lista[i][j]
	return soma


if __name__ == '__main__':
    main()
