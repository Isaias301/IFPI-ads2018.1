"""	Questão: Lista E 02
	Descrição: Existem números de 4 dígitos (entre 1000 e 9999) que obedecem à seguinte 
	característica: se dividirmos o número em dois números de dois dígitos, um composto 
	pela dezena e pela unidade, e outro pelo milhar e pela centena, se somarmos estes dois 
	novos números gerando um terceiro, o quadrado deste terceiro número é exatamente o 
	número original de quatro dígitos. Por exemplo: 2025 -> dividindo: 20 e 25 -> somando 
	temos 45 -> 45 2 = 2025.
"""
from math import sqrt

def main():
	# entrada
	numero = input("Digite um número de 4 digitos: ")
	
	# calculos, operacoes, processamento
	resultado = verifica_numero(numero)

	# saida
	print(resultado)
	

def verifica_numero(numero):
	return (int(numero[2:]) + int(numero[:2]))**2
		
		
if __name__ == '__main__':
	main()