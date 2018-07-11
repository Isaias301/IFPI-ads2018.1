"""	Questão: Lista E 44
	Descrição: Sabendo que latão é constituído de 70% de cobre e 30% de zinco, 
	escreva um algoritmo que calcule a quantidade de cada um desses componentes 
	para se obter certa quantidade de latão (em kg), informada pelo usuário.
"""
import math

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