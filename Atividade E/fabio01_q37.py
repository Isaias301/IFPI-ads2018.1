"""	Questão: Lista E 37
	Descrição: Leia a idade de uma pessoa expressa em 
	dias e escreva-a expressa em anos, meses e dias.
"""

def main():
	# entrada
	idade_em_dias = int(input("Digite sua idade em dias: "))
	

	# calculos, operacoes, processamento
	idade = idade_em_dias / 365	
	mod_meses = idade_em_dias % 365

	meses = mod_meses / 30
	mod_dias = mod_meses % 30
	
	dias = mod_dias
	# saida
	print("Idade : %i/%i/%i" % (idade, meses, dias))

	
if __name__ == '__main__':
	main()