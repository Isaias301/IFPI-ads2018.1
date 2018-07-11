"""	Questão: Lista 02 B
	Descrição: Leia um número e escreva se o número é inteiro ou decimal.
"""

def main():
	# entrada

	numero = input()

	try:
		res = numero.split(".")

		if len(res) == 1:
			print("inteiro")
		elif len(res) > 1:
			print("decimal")
	except:
		print("Error interno.")


if __name__ == '__main__':
	main()