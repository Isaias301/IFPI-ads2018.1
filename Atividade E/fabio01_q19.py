"""	Questão: Lista E 19
	Descrição: Leia o valor do raio de uma esfera, calcule e escreva seu volume.
"""

def main():
	# entrada
	raio_esfera = float(input("Digite o valor do raio da esfera: "))
	

	# calculos, operacoes, processamento
	volume_esfera = ((4 * 3.14 * raio_esfera ** 3) / 3)


	# saida
	print('Volume da esfera: %.2f' % volume_esfera)

	
if __name__ == '__main__':
	main()