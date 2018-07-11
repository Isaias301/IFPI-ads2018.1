"""	Questão: Lista E 34
	Descrição: Leia 3 números, calcule e escreva a média dos números.
"""

def main():
	# entrada
	primeiro_numero = float(input("Digite o primeiro numero: "))
	segundo_numero = float(input("Digite o segundo numero: "))
	terceiro_numero = float(input("Digite o terceiro numero: "))

	# calculos, operacoes, processamento
	media = primeiro_numero + segundo_numero + terceiro_numero / 3
	

	# saida
	print("Media: %.2f" % media)

	
if __name__ == '__main__':
	main()