"""	Questão: Lista E 02
	Descrição: Leia 2 (dois) números, verifique e escreva o 
	menor e o maior entre os números lidos.
"""

def main():
	# entrada
	primeiro_numero = input("Digite o primeiro numero: ")
	segundo_numero = input("Digite o segundo numero: ")
	

	# calculos, operacoes, processamento
	resultado = maior_menor_numero(primeiro_numero, segundo_numero)


	# saida
	print("O maior número e: {}\nO menor número e: {}".format(resultado[0], resultado[1]))

def maior_menor_numero(n1, n2):
	if n1 > n2:
		return n1, n2
	elif n2 > n1:
		return n2, n1
	else:
		return False

if __name__ == '__main__':
	main()