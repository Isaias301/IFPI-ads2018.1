"""	Questão: Lista E 07
	Descrição: Leia 3 numeros, calcule e escreva a soma dos 2 primeiros e a 
	diferença entre os 2 últimos.
"""

def main():
	# entrada
	primeiro_numero = float(input("Digite o primerio número: "))
	segundo_numero = float(input("Digite o segundo número: "))
	terceiro_numero = float(input("Digite o terceiro número: "))
	

	# calculos, operacoes, processamento
	soma = primeiro_numero + segundo_numero
	diferenca = soma % terceiro_numero

	# saida
	print('Soma: %i ' % soma)
	print('Diferença: %i ' % diferenca)

if __name__ == '__main__':
	main()