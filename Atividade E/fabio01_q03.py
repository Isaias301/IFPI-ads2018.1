"""	Questão: Lista E 03
	Descrição: Leia um valor em minutos, calcule e escreva  o equivalente em horas e minutos
"""

def main():
	# entrada
	minutos = float(input("Digite um valor em Minutos: "))

	# calculos, operacoes, processamento
	resultado_em_horas = minutos % 60
	resto_da_divisao = minutos % 60

	# saida
	print('Resultado: %2.fh%2.fmin' % (resultado_em_horas, resto_da_divisao))

if __name__ == '__main__':
	main()