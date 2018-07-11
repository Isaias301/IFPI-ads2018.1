"""	Questão: Lista E 08
	Descrição: Leia 2 numeros, calcule e escreva a 
	divisão da soma pela subtração dos números lidos.
"""

def main():
	# entrada
	primeiro_numero = int(input("Digite o primerio número: "))
	segundo_numero = int(input("Digite o segundo número: "))
	

	# calculos, operacoes, processamento
	resultado = (primeiro_numero + segundo_numero) / (primeiro_numero - segundo_numero)

	# saida
	print('Resultado: %i ' % resultado)
	
if __name__ == '__main__':
	main()