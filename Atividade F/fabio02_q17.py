"""	Questão: Lista E 02
	Descrição: Leia valores inteiros em duas variáveis distintas e se o resto da divisão da 
	primeira pela segunda for 1 escreva a soma dessas variáveis mais o resto da divisão; 
	
	se for 2 escreva se o primeiro e o segundo valor são pares ou ímpares;

	se for igual a 3 multiplique a soma dos valores lidos pelo primeiro; 

	se for igual a 4 divida a soma dos números lidos pelo segundo, se este for diferente de 
	zero. Em qualquer outra situação escreva o quadrado dos números lidos.
"""

def main():
	# entrada
	valor1 = int(input("Digite o primeiro valor: "))
	valor2 = int(input("Digite o segundo valor: "))

	# calculos, operacoes, processamento
	resultado = processamento(valor1, valor2)

	# saida
	print(resultado)


def processamento(valor1, valor2):
	resto = valor1 % valor2
	if resto == 1:
		return "Soma das variaveis mais o resto da divisão {}".format(resto + valor1 + valor2)
	elif resto == 2:
		if valor1 % 2 == 0 and valor2 % 2 == 0:
			return "Os dois valores sao pares"
		else:
			return "Os dois valores sao impares"
	elif resto == 3:
		return "Multiplicacao da soma dois dois valores pelo primeiro valor: {}".format((valor1 + valor2)*valor1)
	elif resto == 4 and valor2 != 0:
		return "Soma dos numeros lidos pelo segundo: {}".format((valor1 + valor2)+valor2)
	else:
		return "Quandado do primeiro valor: {}\nQuandado do segundo valor: {}".format(valor1**2, valor2**2)


if __name__ == '__main__':
	main()