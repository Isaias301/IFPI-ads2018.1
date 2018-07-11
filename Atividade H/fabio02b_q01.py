"""	Questão: Lista 02 B
	Descrição: Leia um número e mostre na tela se o número é positivo ou negativo.
"""

def main():
	# entrada
	numero = int(input("Digite um numero: "))

	# saida
	print("Positivo" if numero%2 == 0 else "Negativo")

if __name__ == '__main__':
	main()