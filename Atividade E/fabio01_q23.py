"""	Questão: Lista E 23
	Descrição: Leia um valor em kg (quilograma), calcule e escreva o equivalente em g (grama).
"""

def main():
	# entrada
	valor_kg = float(input("Digite um valor em kg: "))
	

	# calculos, operacoes, processamento
	grama = valor_kg * 1000


	# saida
	print('Valor em gramas: %.2f g' % grama)

	
if __name__ == '__main__':
	main()