"""	Questão: Lista E 36
	Descrição: Leia a idade de uma pessoa expressa em anos, 
	meses e dias e escreva-a expressa apenas em dias.
"""

def main():
	# entrada
	data_nascimento = input("Digite sua data de nascimento, Ex: 1991/04/01: ")
	

	# calculos, operacoes, processamento
	"""
		Recebo a data de nascimento em formato de string logo apos
		trato a mesma para pegar as posições que desejo realizar o calculo.
		Ano: data_nascimento[:4]
		Mes: data_nascimento[5:7]
		Dia: data_nascimento[8::]

	"""
	idade_em_dias = int(data_nascimento[:4]) * 365 + int(data_nascimento[5:7]) * 30 + int(data_nascimento[8:])
	

	# saida
	print("Idade em dias: %i" % idade_em_dias)

	
if __name__ == '__main__':
	main()