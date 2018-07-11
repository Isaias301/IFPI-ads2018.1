"""	Questão: Lista E 17
	Descrição: Leia o valor da base e altura de um retangulo, calcule e escreva sua area.  
"""

def main():
	# entrada
	base_do_retangulo = int(input("Digite o valor do lado do retangulo: "))
	altura_do_retangulo = int(input("Digite o valor da altura do retangulo: "))

	
	# calculos, operacoes, processamento
	area_do_retangulo = (base_do_retangulo * altura_do_retangulo)


	# saida
	print('Área do retângulo: %i' % area_do_retangulo)

	
if __name__ == '__main__':
	main()