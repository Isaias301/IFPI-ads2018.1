"""	Questão: Lista E 02
	Descrição: Leia 5 (cinco) números inteiros, calcule a sua média e 
	escreva os que são maiores que a média.
"""

def main():
	# entrada
	num1 = int(input("Digite o primeiro numero: "))
	num2 = int(input("Digite o segundo numero: "))
	num3 = int(input("Digite o terceiro numero: "))
	num4 = int(input("Digite o quarto numero: "))
	num5 = int(input("Digite o quinto numero: "))
	

	# calculos, operacoes, processamento
	media = (num1 + num2 + num3 + num4 + num5)/5
	if num1 > media:
		print(num1)
	if num2 > media:
		print(num2)
	if num3 > media:
		print(num3)
	if num4 > media:
		print(num4)
	if num5 > media:
		print(num5)



if __name__ == '__main__':
	main()