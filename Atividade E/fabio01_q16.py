"""	Questão: Lista E 16
	Descrição: Leia o valor do lado de uma quadrado, calcule e escreva sua área  
"""

def main():
	# entrada
	lado_do_quadrado = int(input("Digite o valor do lado do quadrado: "))

	
	# calculos, operacoes, processamento
	area_do_quadrado = ( lado_do_quadrado ** 2)


	# saida
	print('Área do quadrado: %i' % area_do_quadrado)

	
if __name__ == '__main__':
	main()