"""	Questão: Lista E 26
	Descrição: Leia um número inteiro de dias, calcule e escreva 
	quantas semanas e quantos dias ele corresponde.
"""

def main():
	# entrada
	numero_de_dias = int(input("Digite um número de dias: "))
	

	# calculos, operacoes, processamento
	semanas = numero_de_dias / 7
	mod_semanas = numero_de_dias % 7
	dias = mod_semanas


	# saida
	print('Semana: %i' % semanas)
	print('Dias: %i' % dias)
	

if __name__ == '__main__':
	main()