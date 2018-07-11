"""	Questão: Lista E 45
	Descrição: Um algoritmo para gerenciar os saques de um caixa eletrônico deve possuir 
	algum mecanismo para decidir o numero de notas de cada valor que deve ser disponibilizado 
	para o cliente que realizou o saque. Um possível critério seria o da "distribuição ótima" 
	no sentido de que as notas de menor valor disponíveis fossem distribuídas em número 
	mínimo possível. Por exemplo, se a maquina só dispõe de notas de R$ 50, de R$ 10, 
	de R$ 5 e de R$ 1, para uma quantia solicitada de R$ 87, o algoritmo deveria indicar 
	uma nota de R$ 50, três notas de R$ 10, uma nota de R$ 5 e duas notas de R$ 1. 
	Escreva um algoritmo que receba o valor da quantia solicitada e retorne a distribuição 
	das notas de acordo com o critério da distribuição ótima.
"""

def main():
	# entrada
	valor_do_saque = int(input("Digite o valor do saque: "))
	
	
	# calculos, operacoes, processamento
	nota50 = 0
	nota20 = 0
	nota10 = 0
	nota5 = 0
	nota1 = 1
	while(valor_do_saque > 50):
		valor_do_saque = valor_do_saque - 50
		nota50 = nota50 + 1

	while(valor_do_saque > 20):
		valor_do_saque = valor_do_saque - 20
		nota20 = nota20 + 1

	while(valor_do_saque > 10):
		valor_do_saque = valor_do_saque - 10
		nota10 = nota10 + 1

	while(valor_do_saque > 5):
		valor_do_saque = valor_do_saque - 5
		nota5 = nota5 + 1

	while(valor_do_saque > 1):
		valor_do_saque = valor_do_saque - 1
		nota1 = nota1 + 1


	# saida
	print("Você recebera: \n%i notas de R$ 50,00 \n%i notas de R$ 20,00 \n%i notas de R$ 10,00 \n%i notas de R$ 5,00  \n%i notas de R$ 1,00" % (nota50, nota20, nota20, nota10, nota1))
	

	
if __name__ == '__main__':
	main()