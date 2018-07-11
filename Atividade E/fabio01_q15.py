"""	Questão: Lista E 15
	Descrição: Leia o valor da base e altura de um triangulo, calcule e escreva sua area. 
"""

def main():
	# entrada
	base_triangulo = float(input("Digite o valor da base do triangulo: "))
	altura_triangulo = float(input("Digite o valor da altura do triangulo: "))
	
	
	# calculos, operacoes, processamento
	area_triangulo = ((base_triangulo * altura_triangulo) / 2)


	# saida
	print('Área do triângulo:  %.2f' % area_triangulo)

	
if __name__ == '__main__':
	main()