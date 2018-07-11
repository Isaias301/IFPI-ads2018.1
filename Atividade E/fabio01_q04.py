"""	Questão: Lista E 04
	Descrição: Leia o valor em dolar e um valor em dolar, calcule e escreva o equivalente em real(R$)
"""

def main():
	# entrada
	valor_do_dolar = float(input("Digite o valor do Dolar: "))
	valor_em_dolar = float(input("Digite um valor em Dolar: "))

	# calculos, operacoes, processamento
	valor_em_real = valor_em_dolar * valor_do_dolar

	# saida
	print('Resultado: R$ %.2f' % valor_em_real)

if __name__ == '__main__':
	main()