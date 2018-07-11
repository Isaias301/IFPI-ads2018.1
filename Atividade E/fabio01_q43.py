"""	Questão: Lista E 43
	Descrição: Escreva um algoritmo que, tendo como dados de entrada 2 pontos 
	quaisquer no plano, ponto1 (x1,y1) e ponto2 (x2,y2), escreva a distância 
	entre eles, conforme fórmula abaixo.
"""

def main():
	# entrada
	a = int(input("Digite o valor de A: "))
	b = int(input("Digite o valor de B: "))
	c = int(input("Digite o valor de C: "))
	d = int(input("Digite o valor de D: "))
	e = int(input("Digite o valor de E: "))
	f = int(input("Digite o valor de F: "))
	
	# calculos, operacoes, processamento
	x = (((c*e)-(b*f)) + ((a*e)-(b*d)))
	y = (((a*f)-(c*d)) + ((a*e)-(b*d)))
	
	# saida
	print("Valor de X: %i" % x)
	print("Valor de Y: %i" % y)

	
if __name__ == '__main__':
	main()