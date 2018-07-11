"""	Questão: Lista E 31
	Descrição: Leia um número inteiro (4 dígitos binários), 
	calcule e escreva o equivalente na base decimal.
"""

def main():
	# entrada
	numero_binario = input("Digite um numero binario: ")
	

	# calculos, operacoes, processamento
	primeira_posicao = int(numero_binario[0])
	segunda_posicao = int(numero_binario[1])
	terceira_posicao = int(numero_binario[2])
	quarta_posicao = int(numero_binario[3])
	numero_na_base_dez = 2**0*quarta_posicao + 2**1*terceira_posicao + 2**2*segunda_posicao + 2**3*primeira_posicao
	

	# saida
	print("Numero %s na base 10: %i" % (numero_binario ,numero_na_base_dez))

	
if __name__ == '__main__':
	main()