"""	Questão: Lista E 02
	Descrição: Leia 3 (três) números e escreva-os em ordem crescente.
"""

def main():
	# entrada
	numero = input("Digite numero de tres digitos: ")
	

	# calculos, operacoes, processamento
	resultado = ordem_crescente(numero)

	# saida
	print("{}, {}, {}".format(resultado[0], resultado[1], resultado[2]))

def ordem_crescente(numero):
	return sorted(numero, reverse=True)

if __name__ == '__main__':
	main()