"""	Questão: Lista E 05
	Descrição: Leia um número inteiro(3 digitos), calcule e escreva a soma de seus elementos (C + D + U)
"""

def main():
	# entrada
	numero = input("Digite um número inteiro de três digitos: ")
	
	# calculos, operacoes, processamento
	a = int(numero[:1])
	b = int(numero[:2])
	c = int(numero[:3])

	soma_dos_elementos = a + b + c

	# saida
	print('Resultado: %i' % b)

if __name__ == '__main__':
	main()