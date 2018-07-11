"""	Questão: Lista E 32
	Descrição: Leia um número inteiro (3 dígitos), calcule e escreva a 
	diferença entre o número e seu inverso.
"""

def main():
	# entrada
	numero = input("Digite um numero inteiro de 3 digitos: ")
	

	# calculos, operacoes, processamento

	diferenca = int(numero) % int(numero[::-1])
	
	

	# saida
	print("Diferenca: %i" % diferenca)

	
if __name__ == '__main__':
	main()