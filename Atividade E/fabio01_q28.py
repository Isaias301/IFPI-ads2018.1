"""	Questão: Lista E 28
	Descrição: Leia um número inteiro de horas, calcule e escreva quantas semanas, 
	quantos dias e quantas horas ele corresponde.
"""

def main():
	# entrada
	numero_em_horas = int(input("Digite um número em horas: "))
	

	# calculos, operacoes, processamento
	semanas = numero_em_horas / 168
	mod_semanas = numero_em_horas % 168

	dias = mod_semanas / 24
	mod_dias = mod_semanas % 24

	horas = mod_dias

	# saida
	print('Semanas: %i ' % semanas)
	print('Dias: %i ' % dias)
	print('Horas: %i ' % horas)

	
if __name__ == '__main__':
	main()