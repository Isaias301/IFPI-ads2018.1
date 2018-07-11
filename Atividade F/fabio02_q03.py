"""	Questão: Lista E 02
	Descrição: Leia 3 (três) números, verifique e escreva o maior entre os números lidos.
"""

def main():
	# entrada
	primeiro_numero = int(input("Digite o primeiro numero: "))
	segundo_numero = int(input("Digite o segundo numero: "))
	terceiro_numero = int(input("Digite o terceiro numero: "))

	# calculos, operacoes, processamento
	resultado = maior_numero(primeiro_numero, segundo_numero, terceiro_numero)


	# saida
	print(resultado)

def maior_numero(n1, n2, n3):
	if n1 > n2:
		return n1
	elif n1 > n3:
		return n1

	elif n2 > n1:
		return n2
	elif n2 > n3:
		return n2

	elif n3 > n1:
		return n3
	elif n3 > n2:
		return n3
		
	else:
		return False

if __name__ == '__main__':
	main()