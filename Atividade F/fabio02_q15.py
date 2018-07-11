"""	Questão: Lista E 02
	Descrição: Leia a quantidade de horas aula dadas por dois professores e o 
	valor por hora recebido por cada um. Escreva na tela qual dos professores 
	tem salário total maior.
"""

def main():
	# entrada
	horas_aula_prof1 = int(input("Digite a quantidade de horas aula dadas do 1º Professor(a): "))
	valor_hora_prof1 = float(input("Digite o valor da hora de uma aula do 1º Professor(a): "))

	horas_aula_prof2 = int(input("Digite a quantidade de horas aula dadas do 2º Professor(a): "))
	valor_hora_prof2 = float(input("Digite o valor da hora de uma aula do 2º Professor(a): "))

	# calculos, operacoes, processamento
	if horas_aula_prof1 * valor_hora_prof1 > horas_aula_prof2 * valor_hora_prof2:
		resultado = "1º Professor(a) tem o maior salário"
	else:
		resultado = "2º Professor(a) tem o maior salário"

	# saida
	print(resultado)


if __name__ == '__main__':
	main()