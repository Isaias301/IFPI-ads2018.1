"""	Questão: Lista E 41
	Descrição: O custo ao consumidor de um carro novo é a soma do 
	custo de fábrica com a percentagem do distribuidor e dos impostos 
	(aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor
	seja de 28% e os impostos de 45%, escreva um algoritmo que leia o custo de 
	fábrica de um carro e escreva o custo ao consumidor.
"""

def main():
	# entrada
	custo_de_fabrica = int(input("Custo de fabrica: "))
	
	# calculos, operacoes, processamento
	valor_final_do_carro = ((28/100)*custo_de_fabrica + (45/100)*custo_de_fabrica) + custo_de_fabrica
	
	# saida
	print("Você comprara o carro por: R$ %.2f" % valor_final_do_carro)

	
if __name__ == '__main__':
	main()