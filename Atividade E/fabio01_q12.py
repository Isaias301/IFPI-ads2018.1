"""	Questão: Lista E 12
	Descrição: Leia o salario de um trabalhador e escreva 
	seu novo salario com um aumento de 25%.
"""

def main():
	# entrada
	salario = float(input("Digite seu salário: "))
	
	
	# calculos, operacoes, processamento
	novo_salario = (( 25 / 100 ) * salario) + salario

	# saida
	print('Novo salario: R$ %.2f' % novo_salario)

	
if __name__ == '__main__':
	main()