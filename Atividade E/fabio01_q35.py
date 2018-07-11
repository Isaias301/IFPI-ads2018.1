"""	Questão: Lista E 35
	Descrição: Leia um número inteiro (4 dígitos), calcule e escreva a soma 
	dos elementos que o compõem. Ex.: número = 9534 ; soma = 9+5+3+4 = 21.
"""

def main():
	# entrada
	numero1, numero2, numero3, numero4 = input("Digite um numero: ")


	# calculos, operacoes, processamento
	soma = int(numero1) + int(numero2) + int(numero3) + int(numero4)

	# saida
	print("Soma: %i" % soma)

	
if __name__ == '__main__':
	main()