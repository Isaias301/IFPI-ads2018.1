"""	Questão: Lista E 11
	Descrição: Leia um número inteiro(3 digitos) e escreva o inverso do número.
	Ex: numero = 532; inverso = 235.
"""

def main():
	# entrada
	numero = input("Digite um número: ")
	
	
	# calculos, operacoes, processamento
	inverso = numero[::-1]

	# saida
	print('Inverso: %s' % inverso)

	
if __name__ == '__main__':
	main()