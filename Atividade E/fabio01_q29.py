"""	Questão: Lista E 29
	Descrição: Leia um número inteiro de meses, calcule e escreva 
	quantos anos e quantos meses ele corresponde.
"""

def main():
	# entrada
	numero_em_meses = int(input("Digite um número em meses: "))
	

	# calculos, operacoes, processamento
	anos = numero_em_meses / 12
	meses = numero_em_meses % 12
	

	# saida
	print('Anos: %i ' % anos)
	print('Meses: %i ' % meses)


	
if __name__ == '__main__':
	main()