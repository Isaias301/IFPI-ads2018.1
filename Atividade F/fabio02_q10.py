"""	Questão: Lista E 02
	Descrição: Leia uma data (dia, mês e ano), verifique e escreva se a 
	data é ou não válida.
"""

def main():
	# entrada
	data = input("Digite a data atual Ex: 06/07/2018: ")
	

	# calculos, operacoes, processamento	
	resultado = valida_data(ano = int(data[6:]), mes = int(data[3:5]), dia = int(data[0:2]))

	# saida
	print(resultado)


def valida_data(ano, mes, dia):

	if ano == 2018 and mes < 12 and dia <= 30 and dia > 1:
		return "Data valida"
	else:
		return "Data inválida"
	

if __name__ == '__main__':
	main()