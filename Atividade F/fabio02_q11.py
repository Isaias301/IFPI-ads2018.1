"""	Questão: Lista E 02
	Descrição: Leia quatro números (opção, num 1, num2, num3) e que escreva o 
	valor de num1 se opção igual a 1; o valor de num2 se opção for igual a 2; 
	e o valor de num3 se opção for igual a 3. Os únicos valores possíveis para a 
	variável opção são 1, 2 e 3.
"""

def main():
	# entrada
	opcao = int(input("Digite uma opção entre 1 a 3: "))
	num1 = int(input("Digite um numero entre 1 a 3: "))
	num2 = int(input("Digite um numero entre 1 a 3: "))
	num3 = int(input("Digite um numero entre 1 a 3: "))

	# calculos, operacoes, processamento	
	resultado = valida_data(opcao, num1, num2, num3)

	# saida
	print(resultado)


def valida_data(opcao, num1, num2, num3):

	if opcao == 1:
		return num1
	elif opcao == 2:
		return num2
	elif opcao == 3:
		return num3
	else:
		return "Opção inválida"


if __name__ == '__main__':
	main()