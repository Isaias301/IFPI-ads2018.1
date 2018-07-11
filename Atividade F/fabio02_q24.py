"""	Questão: Lista E 02
	Descrição: Leia os coeficientes (A, B e C) de uma equações de 2° grau e escreva suas raízes. 
	Vale lembrar que o coeficiente A deve ser diferente de 0 (zero).
"""

def main():
	# entrada
	a = int(input("Digite o primeiro coeficiente: "))
	b = int(input("Digite o segundos coeficiente: "))
	c = int(input("Digite o terceiro coeficiente: "))
	
	# calculos, operacoes, processamento
	resultado = raizes(a, b, c) 

	# saida
	print("Raizes: {}, {}".format(resultado[0], resultado[1]))


def raizes(a, b, c):
	if a != 0:
		return b, c
	else:
		return "Invalido"


if __name__ == '__main__':
	main()