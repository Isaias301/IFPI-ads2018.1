"""	Questão: Lista 02 B
	Descrição: Leia o preço de três produtos e informe qual produto deve ser comprado, 
	sabendo que a decisão é sempre pelo mais barato.
"""

def main():
	# entrada
	p1 = float(input("Digite o preço do 1º produto: "))
	p2 = float(input("Digite o preço do 2º produto: "))
	p3 = float(input("Digite o preço do 3º produto: "))

	# processamento
	if p1 < p2 and p1 < p3:
		print("Mais barato e: {}".format(p1))
	elif p2 < p1 and p2 < p3:
		print("Mais barato e: {}".format(p2))
	else:
		print("Mais barato e: {}".format(p3))

if __name__ == '__main__':
	main()