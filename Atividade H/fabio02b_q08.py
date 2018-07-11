"""	Questão: Lista 02 B
	Descrição: 
"""

def main():
	# entrada
	valor_hora = float(input("Valor da hora: "))
	horas_trabalhadas = float(input("Horas trabalhadas: "))

	salario = valor_hora*horas_trabalhadas

	print("Salário Bruto: %.2f" % salario)


	if salario <= 1500:
		ir = (5/100)*salario
		print("(-) IR (5%)            : R$ {}".format(ir))
	elif salario <= 2500:
		ir = (10/100)*salario
		print("(-) IR (10%)           : R$ {}".format(ir))
	elif salario > 2500:
		ir = (20/100)*salario
		print("(-) IR (20%):          : R$ {}".format(ir))
	
	inss = (10/100)*salario
	fgts = (11/100)*salario
	tota_descontos = ir + inss
	salario_liquido = salario - tota_descontos
	print("(-) INSS (10%)         : R$ {}".format(inss))
	print("FGTS (11%)             : R$ {}".format(fgts))
	print("Total de descontos     : R$ {}".format(tota_descontos))
	print("Salário Liquido:       : R$ {}".format(salario_liquido))
		


if __name__ == '__main__':
	main()