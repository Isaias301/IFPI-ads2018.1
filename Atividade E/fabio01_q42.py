"""	Questão: Lista E 42
	Descrição: Escreva um algoritmo que, tendo como dados de entrada 2 pontos 
	quaisquer no plano, ponto1 (x1,y1) e ponto2 (x2,y2), escreva a distância 
	entre eles, conforme fórmula abaixo.
"""
import math

def main():
	# entrada
	x1 = int(input("Digite o valor de X1: "))
	x2 = int(input("Digite o valor de X2: "))
	y1 = int(input("Digite o valor de Y1: "))
	y2 = int(input("Digite o valor de Y2: "))
	
	# calculos, operacoes, processamento
	distancia = math.sqrt(((x2 - x1)**2 + (y2 - y1)**2))
	
	# saida
	print("Distancia entre os pontos: %.2f" % distancia)

	
if __name__ == '__main__':
	main()