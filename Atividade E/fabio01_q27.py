"""	Questão: Lista E 27
	Descrição: Leia um número inteiro de segundos, calcule e escreva 
	quantas horas, quantos minutos e quantos segundos ele corresponde.
"""

def main():
	# entrada
	numero_em_segundos = int(input("Digite um número em segundos: "))
	

	# calculos, operacoes, processamento
	horas = numero_em_segundos / 3600
	mod_horas = numero_em_segundos % 3600

	minutos = mod_horas / 60
	mod_minutos = mod_horas % 60

	segundos = mod_minutos
	

	# saida
	print('Horas: %i: ' % horas)
	print('Minutos: %i: ' % minutos)
	print('Segundos: %i: ' % segundos)
	

	
if __name__ == '__main__':
	main()