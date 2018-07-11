"""	Questão: Lista E 06
	Descrição: Leia uma velocidade em km/h, calcule e escreva esta velocidade em m/s.
"""

def main():
	# entrada
	velocidade_em_km = float(input("Digite uma uma velocidade em Km/h: "))
	
	# calculos, operacoes, processamento
	velocidade_em_ms = velocidade_em_km * 3.6

	# saida
	print('Resultado: %.2f m/s' % velocidade_em_ms)

if __name__ == '__main__':
	main()