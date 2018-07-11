"""	Questão: Lista E 39
	Descrição: Leia três números inteiros e positivos (A, B, C) e 
	calcule a seguinte expressão:
"""

def main():
	# entrada
	A = int(input("Digite o primeiro numero: "))
	B = int(input("Digite o segundo numero: "))
	C = int(input("Digite o terceiro numero: "))

	# calculos, operacoes, processamento
	if A < 0 and B < 0 and C < 0:
	    print("Números invalidos.")
	else:
		R = (A + B) ** 2
		S = (B + C) ** 2
		D = (R + S) / 2
	# saida
	print("Resultado: %i" % D)

	
if __name__ == '__main__':
	main()