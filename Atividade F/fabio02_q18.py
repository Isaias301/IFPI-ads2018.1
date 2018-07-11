"""	Questão: Lista E 02
	Descrição: Leia dois valores e uma das seguintes operações a serem executadas 
	(codificadas da seguinte forma: 1 – Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão).
	Calcule e escreva o resultado dessa operação sobre os dois valores lidos.
"""

def main():
	# entrada
	valor1 = float(input("Digite um valor: "))
	valor2 = float(input("Digite outro valor: "))
	operacao = int(input("Escolha uma das opções abaixo\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n\nDigite a operação desejada: "))

	# calculos, operacoes, processamento
	resultado = operacacao(valor1, valor2, operacao)

	# saida
	print(resultado)


def operacacao(valor1, valor2, operacao):
	if operacao == 1:
		return valor1 + valor2
	elif operacao == 2:
		return valor1 - valor2
	elif operacao == 3:
		return valor1 * valor2
	elif operacao == 4:
		return valor1 / valor2
	else:
		return "Operação inválida"


if __name__ == '__main__':
	main()