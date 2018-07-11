"""	Questão: Lista E 02
	Descrição: Um número é um quadrado perfeito quando a raiz quadrada do número é igual à 
	soma das dezenas formadas pelos seus dois primeiros e dois últimos dígitos.
	Exemplo: √9801 = 99 = 98 + 01. O número 9801 é um quadrado perfeito.
	
	Escreva um algoritmo que leia um número de 4 dígitos e verifique se ele é um quadrado 
	perfeito.
"""
from math import sqrt

def main():
	# entrada
	numero = input("Digite um número de 4 digitos: ")
	
	# calculos, operacoes, processamento
	resultado = quadrado_perfeito(numero)

	# saida
	print(resultado)
	

def quadrado_perfeito(numero):
	if sqrt(int(numero)) == int(numero[2:]) + int(numero[:2]):
		return "Quadrado perfeito."
	else:
		return "Não e um quadrado perfeito."


if __name__ == '__main__':
	main()