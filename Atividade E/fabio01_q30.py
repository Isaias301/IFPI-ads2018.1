"""	Questão: Lista E 30
	Descrição: Leia um número inteiro de minutos, calcule e escreva quantos dias, 
	quantas horas e quantos minutos ele corresponde.
"""

def main():
	# entrada
	valor_em_minutos = float(input("Digite um valor em minutos: "))
	

	# calculos, operacoes, processamento
	valor_dias = valor_em_minutos / 60
	mod_dias = valor_em_minutos % 60

	valor_horas = mod_dias / 60
	mod_horas = mod_dias % 60

	valor_minutos = mod_horas


	# saida
	print("Dias: %i" % valor_dias)
	print("Horas: %i" % valor_horas)
	print("Minutos: %i" % valor_minutos)

	
if __name__ == '__main__':
	main()