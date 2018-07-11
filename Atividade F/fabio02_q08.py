"""	Questão: Lista E 02
	Descrição: Leia data atual (dia, mês e ano) e data de nascimento (dia, mês e ano) 
	de uma pessoa, calcule e escreva sua idade exata (em anos).
"""

def main():
	# entrada
	data_atual = input("Digite a data atual Ex: 06/07/2018: ")
	data_nascimento = input("Digite sua data de nascimento Ex: 06/07/2018: ")

	# calculos, operacoes, processamento
	idade = int(data_atual[6:]) - int(data_nascimento[6:])

	# saida
	print("Você possue: {} anos".format(idade))

if __name__ == '__main__':
	main()