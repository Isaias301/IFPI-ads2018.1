"""	Questão: Lista 02 B
	Descrição: Leia um número inteiro menor que 1000 e imprima a quantidade de centenas, 
	dezenas e unidades do número. Observando os termos no plural a colocação do "e", 
	da vírgula entre outros. Exemplos:
	
	326 = 3 centenas, 2 dezenas e 6 unidades
	12 = 1 dezena e 2 unidades
"""

def main():
	# entrada
	numero = str(input())
	
	print("{} = {} centenas, {} dezenas, {} unidades".format(numero, numero[0], numero[1], numero[2]))
		

if __name__ == '__main__':
	main()