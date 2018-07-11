"""	Questão: Lista E 02
	Descrição: Leia 5 (cinco) números inteiros e escreva o maior e o menor deles. 
	Considere que todos os valores são diferentes.
"""

def main():
	# entrada
	numero1 = input("Digite o primeiro numero: ")
	numero2 = input("Digite o segundo numero: ")
	numero3 = input("Digite o terceiro numero: ")
	numero4 = input("Digite o quarto numero: ")
	numero5 = input("Digite o quinto numero: ")
	

	# calculos, operacoes, processamento
	maior = max(numero1, numero2, numero3, numero4, numero5)
	menor = min(numero1, numero2, numero3, numero4, numero5)


	# saida
	print("O maior número e: {}\nO menor número e: {}".format(maior, menor))


if __name__ == '__main__':
	main()