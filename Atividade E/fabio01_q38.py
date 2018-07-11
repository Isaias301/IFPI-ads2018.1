"""	Questão: Lista E 38
	Descrição: Leia 2 (duas) frações (numerador e denominador), 
	calcule e escreva a soma destas frações, escrevendo o resultado em forma de fração.
"""

def main():
	# entrada
	numerador_fracao1 = int(input("Digite o numerador da primeira fracao: "))
	denominador_fracao1 = int(input("Digite o denominador da primeira fracao: "))
	numerador_fracao2 = int(input("Digite o numerador da segunda fracao: "))
	denominador_fracao2 = int(input("Digite o denominador da segunda fracao: "))

	# calculos, operacoes, processamento
	
	
	if denominador_fracao1 == denominador_fracao2:
	    numerador_resultado = numerador_fracao1 + numerador_fracao2
	    denominador_resultado = denominador_fracao1

	else:
		numerador_resultado = (numerador_fracao1 * denominador_fracao2) + (numerador_fracao2 * denominador_fracao1)
		denominador_resultado = ((denominador_fracao1 * denominador_fracao2) + (denominador_fracao2 * denominador_fracao1)) / 2
		 

	# saida
	print("Fracao: %i/%i" % (numerador_resultado, denominador_resultado))

	
if __name__ == '__main__':
	main()