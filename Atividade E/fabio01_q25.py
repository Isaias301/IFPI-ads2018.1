"""	Questão: Lista E 25
	Descrição: Leia um número inteiro de metros, calcule e escreva 
	quantos Km e quantos metros ele corresponde.
"""

def main():
	# entrada
	valor_metros = int(input("Digite um valor em metros: "))
	

	# calculos, operacoes, processamento
	valor_km = valor_metros / 1000


	# saida
	print('Valor em km: %i km' % valor_km)
	print('Corresponde a: %i m' % valor_metros)

	
if __name__ == '__main__':
	main()