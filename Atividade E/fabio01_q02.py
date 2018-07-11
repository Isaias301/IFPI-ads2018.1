"""	Questão: Lista E 02
	Descrição: Leia um valor em horas e um valor em minutos, calcule e escreva o equivalente a minutos
"""

def main():
	# entrada
	horas = float(input("Digite um valor em Horas: "))
	minutos = float(input("Digite um valor em Minutos: "))

	# calculos, operacoes, processamento
	resultado_em_minutos = (horas * 60) + minutos

	# saida
	print('Resultado: %2.f minutos' % resultado_em_minutos)

if __name__ == '__main__':
	main()