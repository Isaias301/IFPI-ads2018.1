"""	Questão: Lista E 18
	Descrição: Leia o valor do raio de uma circunferência, calcule e escreva seu comprimento.  
"""

def main():
	# entrada
	raio_circunferencia = float(input("Digite o valor do raio da circunferência: "))
	

	# calculos, operacoes, processamento
	comprimento = 2 * 3.14 * raio_circunferencia


	# saida
	print('Comprimento: %.2f' % comprimento)

	
if __name__ == '__main__':
	main()