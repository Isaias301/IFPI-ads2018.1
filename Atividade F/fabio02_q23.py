"""	Questão: Lista E 02
	Descrição: Leia 2 datas (cada data é composta por 3 variáveis inteiras: dia, mês e ano) 
	e escreva qual delas é a mais recente.
"""

def main():
	# entrada
	data1 = input("Digite a primeira data, Ex: 21/05/2018: ")
	data2 = input("Digite segunda data, Ex: 21/05/2018: ")
	
	# calculos, operacoes, processamento
	resultado = verifica_data(data1, data2) 

	# saida
	print("A data mais recente e: {}".format(resultado))


def verifica_data(data1, data2):
			#dia		 #dia					#mes				#mes			#ano			#ano
	if int(data1[:2]) > int(data2[:2]) and int(data1[3:5]) > int(data2[3:5]) and int(data1[6:]) > int(data2[6:]):
		return data1
	else:
		return data2


if __name__ == '__main__':
	main()