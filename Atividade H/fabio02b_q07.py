"""	Questão: Lista 02 B
	Descrição: As Organizações Tabajara resolveram dar um aumento de salário aos 
	seus colaboradores e lhe contrataram para desenvolver o programa que calculará os 
	reajustes. Escreva um algoritmo que leia o salário de um colaborador e o reajuste 
	segundo o seguinte critério, baseado no salário atual:

	salários até R$ 280,00 (incluindo) : aumento de 20%
	salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
	salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
	salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
		o salário antes do reajuste;
		o percentual de aumento aplicado;
		o valor do aumento;
		o novo salário, após o aumento.	
"""

def main():
	# entrada
	salario = float(input("Salario atual: "))

	if salario <= 280:
		percentual = 20
		aumento = ((percentual/100)*salario)
		salario_atual = aumento+salario
	elif salario > 280 and salario < 700:
		percentual = 15
		aumento = ((percentual/100)*salario)
		salario_atual = aumento+salario
	elif salario >= 1500:
		percentual = 5
		aumento = ((percentual/100)*salario)
		salario_atual = aumento+salario

	print("Salario: %.2f" % salario)
	print("Percentual de aumento aplicado: {}".format(percentual))
	print("Valor do aumento: %.2f" % aumento)
	print("Novo salário, após o aumento: %.2f" % salario_atual)


if __name__ == '__main__':
	main()