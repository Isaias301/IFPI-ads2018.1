"""	Questão: Lista E 33
	Descrição: Leia um número inteiro (3 dígitos), calcule e escreva a soma do 
	número com seu inverso. (Ex.: número = 532 ; inverso = 235 ; soma = 532 + 235 = 767).
"""

def main():
	# entrada
	numero = input("Digite um numero de 3 digitos: ")
	

	# calculos, operacoes, processamento
	soma = int(numero) + int(numero[::-1])
	

	# saida
	print("Soma: %i" % soma)

	
if __name__ == '__main__':
	main()