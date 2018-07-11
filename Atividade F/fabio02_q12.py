"""	Questão: Lista E 02
	Descrição: Leia 1 (um) número inteiro e escreva se este número é par ou impar.
"""

def main():
	# entrada
	numero = int(input("Digite um numero: "))
	

	# calculos, operacoes, processamento
	resultado = impar_par(numero)

	# saida
	print(resultado)


def impar_par(numero):
	if numero % 2 == 0:
		return "Numero par"
	else:
		return "Numero impar"

if __name__ == '__main__':
	main()