"""	Questão: Lista E 10
	Descrição: Leia 2 números inteiros, calcule e 
		escreva o quociente e o resto da divisão do 1º pelo 2º
"""

def main():
	# entrada
	primeiro_numero = int(input("Digite o primerio número: "))
	segundo_numero = int(input("Digite o segundo número: "))
	

	# calculos, operacoes, processamento
	quociente = primeiro_numero / segundo_numero
	resto = primeiro_numero % segundo_numero

	# saida
	print('Quociente: %i ' % quociente)
	print('Resto: %i ' % resto)
	
if __name__ == '__main__':
	main()