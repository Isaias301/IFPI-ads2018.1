"""	Questão: Lista E 20
	Descrição: Leia uma temperatura em °C, calcule e escreva a equivalente em °F.
"""

def main():
	# entrada
	celcios = int(input("Digite a temperatura em °C: "))
	

	# calculos, operacoes, processamento
	fareiraite = ((9 * celcios + 160) / 5)


	# saida
	print('Remperatura em °F: %i' % fareiraite)

	
if __name__ == '__main__':
	main()