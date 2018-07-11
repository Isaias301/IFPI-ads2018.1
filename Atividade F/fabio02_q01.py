"""	Questão: Lista E 02
	Descrição: Leia 3 (três) números, verifique e escreva quantos números 
	iguais existem entre os números.
"""

def main():
	# entrada
	numero1 = input("Digite o primeiro numero: ")
	numero2 = input("Digite o segundo numero: ")
	numero3 = input("Digite o terceiro numero: ")

	# calculos, operacoes, processamento
	numeros_iguais = verificar_igualdade(numero1, numero2, numero3)

	# saida
	print("Existe {} números iguais".format(numeros_iguais))

	
def verificar_igualdade(numero1, numero2, numero3):
	if numero1 == numero2 == numero3:
		return 3
	elif numero1 == numero2 or numero3 == numero2 or numero1 == numero3:
		return 2
	else:
		return 0	


if __name__ == '__main__':
	main()