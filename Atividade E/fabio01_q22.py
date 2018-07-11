"""	Questão: Lista E 22
	Descrição: Leia um valor em km, calcule e escreva o equivalente em m.
"""

def main():
	# entrada
	valor_km = float(input("Digite um valor em km: "))
	

	# calculos, operacoes, processamento
	metros = valor_km * 1000


	# saida
	print('Valor em metros: %.2f m' % metros)

	
if __name__ == '__main__':
	main()