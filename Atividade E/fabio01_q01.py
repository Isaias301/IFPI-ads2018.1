"""	Questão: Lista E 01
	Descrição: Leia a velociade em m/s, calcule e escreva esta velocidade em km/h. (Vkm = Vm/s * 3.6)
"""

def main():
	# entrada
	velocidade_ms = float(input("Digite uma velocidade em M/S: "))

	# calculos, operacoes, processamento
	vkm_h = velocidade_ms * 3.6

	# saida
	print('Resultado: %f Km/h' % vkm_h)

if __name__ == '__main__':
	main()