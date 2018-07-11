"""	Questão: Lista E 24
	Descrição: Leia um valor em m, calcule e escreva o equivalente em cm.
"""

def main():
	# entrada
	valor_metros = float(input("Digite um valor em metros: "))
	

	# calculos, operacoes, processamento
	valor_centimetros = valor_metros * 100


	# saida
	print('Valor em centimetros: %.2f cm' % valor_centimetros)

	
if __name__ == '__main__':
	main()