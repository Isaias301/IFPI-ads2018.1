"""	Questão: Lista E 02
	Descrição: Leia 1 (um) número de 2 (dois) dígitos, 
	verifique e escreva se o algarismo da dezena é igual 
	ou diferente do algarismo da unidade.
"""

def main():
	# entrada
	dezena, unidade = input("Digite numero de dois digitos: ")
	

	# calculos, operacoes, processamento
	resultado = verifica_maior_menor(dezena, unidade)


	# saida
	print(resultado)

def verifica_maior_menor(dezena, unidade):
	if dezena > unidade:
		return "Dezena e maior"
	else:
		return "Unidade menor"

if __name__ == '__main__':
	main()