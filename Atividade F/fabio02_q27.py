"""	Questão: Lista E 02
	Descrição: Determine a idade de uma pessoa, em anos, meses e dias, dadas a data 
	(dia, mês e ano) do seu nascimento e a data (dia, mês e ano) atual.
"""

def main():
	# entrada
	data_nascimento = input("Digite a data de seu nascimento: Ex: 21/05/2018: ")
	data_atual = input("Digite a data atual: Ex: 21/05/2018: ")

	
	# calculos, operacoes, processamento
	anos = int(data_atual[6:]) - int(data_nascimento[6:])
	meses = (anos*365) / 12
	dias = anos*365

	# saida
	print("Voce tem: %i anos de vida." % anos)
	print("Voce tem: %i mese de vida." % meses)
	print("Voce tem: %i dias de vida." % dias)


if __name__ == '__main__':
	main()