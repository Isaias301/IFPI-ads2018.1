"""	Questão: Lista E 21
	Descrição: Leia uma temperatura em °F, 
	calcule e escreva a equivalente em °C. (t°C = (5 * t°F - 160) / 9).
"""

def main():
	# entrada
	fareiraite = int(input("Digite a temperatura em °F: "))
	

	# calculos, operacoes, processamento
	celcius = (5 * fareiraite - 160) / 9


	# saida
	print('Remperatura em °C: %i' % celcius)

	
if __name__ == '__main__':
	main()