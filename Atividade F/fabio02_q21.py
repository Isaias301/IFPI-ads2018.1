"""	Questão: Lista E 02
	Descrição: Realize arredondamentos de números utilizando a regra usual da matemática: 
	se a parte fracionaria for maior do que ou igual a 0,5, o numero é arredondado para 
	o inteiro imediatamente superior, caso contrario, é arredondado para o inteiro 
	imediatamente inferior.
"""

def main():
	# entrada
	numero = float(input("Digite um numero: "))
	
	
	# calculos, operacoes, processamento
	if numero > 0: 
		resultado = round(numero)
	else:
		resultado = "Número inválido"

	# saida
	print(resultado)



if __name__ == '__main__':
	main()